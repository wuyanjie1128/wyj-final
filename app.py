import os
import uuid
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from openai import OpenAI
import alibabacloud_oss_v2 as oss
from alibabacloud_oss_v2.models import PutObjectRequest
import config
from animal_data import ANIMAL_CATEGORIES, ANIMALS_DATA, get_animals_by_category, get_animal_detail

app = Flask(__name__)
app.config.from_object('config')

# 确保临时上传文件夹存在
os.makedirs(config.UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    """检查文件扩展名是否允许"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS


def upload_to_oss(local_file_path, object_name):
    """上传文件到阿里云OSS"""
    try:
        # 配置OSS客户端
        cfg = oss.config.load_default()
        cfg.credentials_provider = oss.credentials.StaticCredentialsProvider(
            access_key_id=config.OSS_ACCESS_KEY_ID,
            access_key_secret=config.OSS_ACCESS_KEY_SECRET
        )
        cfg.region = config.OSS_REGION
        cfg.endpoint = config.OSS_ENDPOINT

        # 创建OSS客户端
        client = oss.Client(cfg)

        # 上传文件
        result = client.put_object_from_file(
            PutObjectRequest(
                bucket=config.OSS_BUCKET,
                key=object_name
            ),
            local_file_path
        )

        # 生成文件的公共访问URL
        file_url = f"https://{config.OSS_BUCKET}.{config.OSS_ENDPOINT}/{object_name}"
        
        return {
            'success': True,
            'url': file_url,
            'etag': result.etag
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


def identify_animal(image_url):
    """使用Qwen视觉模型识别图片中的动物"""
    try:
        client = OpenAI(
            api_key=config.DASHSCOPE_API_KEY,
            base_url=config.DASHSCOPE_BASE_URL,
        )

        completion = client.chat.completions.create(
            model=config.QWEN_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url
                            },
                        },
                        {
                            "type": "text",
                            "text": """请仔细观察这张图片，如果图片中有动物，请按以下格式详细介绍：

1. 动物名称（中文和学名）
2. 主要特征
3. 生活习性
4. 栖息地
5. 有趣的事实

如果图片中没有动物，请说明图片中的主要内容。"""
                        },
                    ],
                },
            ],
        )
        
        return {
            'success': True,
            'content': completion.choices[0].message.content
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


@app.route('/')
def index():
    """主页 - 显示动物分类和上传功能"""
    return render_template('index.html', categories=ANIMAL_CATEGORIES)


@app.route('/category/<category_id>')
def category(category_id):
    """动物分类页面"""
    if category_id not in ANIMAL_CATEGORIES:
        return "分类不存在", 404
    
    category_info = ANIMAL_CATEGORIES[category_id]
    animals = get_animals_by_category(category_id)
    
    return render_template('category.html', 
                         category_id=category_id,
                         category_info=category_info, 
                         animals=animals)


@app.route('/animal/<animal_id>')
def animal_detail(animal_id):
    """动物详情页面"""
    animal = get_animal_detail(animal_id)
    
    if not animal:
        return "动物不存在", 404
    
    category_info = ANIMAL_CATEGORIES[animal['category']]
    
    return render_template('animal_detail.html', 
                         animal_id=animal_id,
                         animal=animal, 
                         category_info=category_info)


@app.route('/upload', methods=['POST'])
def upload_file():
    """处理文件上传和动物识别"""
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': '没有文件上传'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'success': False, 'error': '没有选择文件'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({
            'success': False,
            'error': f'不支持的文件格式，仅支持: {", ".join(config.ALLOWED_EXTENSIONS)}'
        }), 400
    
    try:
        # 生成安全的文件名
        filename = secure_filename(file.filename)
        file_ext = filename.rsplit('.', 1)[1].lower()
        unique_filename = f"{uuid.uuid4().hex}.{file_ext}"
        
        # 保存到临时文件夹
        local_path = os.path.join(config.UPLOAD_FOLDER, unique_filename)
        file.save(local_path)
        
        # 上传到OSS
        timestamp = datetime.now().strftime('%Y%m%d')
        oss_object_name = f"animal-images/{timestamp}/{unique_filename}"
        
        upload_result = upload_to_oss(local_path, oss_object_name)
        
        if not upload_result['success']:
            # 清理临时文件
            os.remove(local_path)
            return jsonify({
                'success': False,
                'error': f'上传到OSS失败: {upload_result["error"]}'
            }), 500
        
        image_url = upload_result['url']
        
        # 使用大模型识别动物
        identify_result = identify_animal(image_url)
        
        # 清理临时文件
        os.remove(local_path)
        
        if not identify_result['success']:
            return jsonify({
                'success': False,
                'error': f'识别失败: {identify_result["error"]}'
            }), 500
        
        return jsonify({
            'success': True,
            'image_url': image_url,
            'description': identify_result['content']
        })
        
    except Exception as e:
        # 确保清理临时文件
        if os.path.exists(local_path):
            os.remove(local_path)
        return jsonify({
            'success': False,
            'error': f'处理失败: {str(e)}'
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

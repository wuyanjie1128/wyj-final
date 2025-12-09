# 配置文件 - 存储API密钥和OSS凭证
# 注意：生产环境中应使用环境变量或密钥管理服务

# 阿里云百炼API配置
DASHSCOPE_API_KEY = "sk-c955e076c3c9452187149063ed29807d"
DASHSCOPE_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
QWEN_MODEL = "qwen3-vl-plus"

# 阿里云OSS配置
OSS_ACCESS_KEY_ID = "LTAI5t9Eke5F5JZEtBPmYmyq"
OSS_ACCESS_KEY_SECRET = "Ia5vglPQl2s5NHKiOjyIAvmHdOa0ya"
OSS_REGION = "cn-shanghai"
OSS_ENDPOINT = "oss-cn-shanghai.aliyuncs.com"
OSS_BUCKET = "oss-buckeet-shanghai"

# Flask配置
UPLOAD_FOLDER = "temp_uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size

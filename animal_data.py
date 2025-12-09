# 动物数据库 - 包含分类、数据、科普知识等

ANIMAL_CATEGORIES = {
    "mammals": {
        "name": "哺乳动物",
        "icon": "fa-paw",
        "color": "from-orange-400 to-red-500",
        "description": "温血、胎生、哺乳的脊椎动物",
        "count": 5500
    },
    "birds": {
        "name": "鸟类",
        "icon": "fa-dove",
        "color": "from-blue-400 to-cyan-500",
        "description": "有羽毛、能飞行的温血动物",
        "count": 10000
    },
    "reptiles": {
        "name": "爬行动物",
        "icon": "fa-dragon",
        "color": "from-green-400 to-emerald-500",
        "description": "冷血、有鳞片的卵生动物",
        "count": 10000
    },
    "amphibians": {
        "name": "两栖动物",
        "icon": "fa-frog",
        "color": "from-teal-400 to-green-500",
        "description": "水陆两栖、变态发育的动物",
        "count": 7000
    },
    "fish": {
        "name": "鱼类",
        "icon": "fa-fish",
        "color": "from-indigo-400 to-blue-500",
        "description": "水生、用鳃呼吸的脊椎动物",
        "count": 32000
    },
    "insects": {
        "name": "昆虫",
        "icon": "fa-bug",
        "color": "from-purple-400 to-pink-500",
        "description": "六足、有外骨骼的节肢动物",
        "count": 1000000
    }
}

ANIMALS_DATA = {
    # 哺乳动物
    "giant_panda": {
        "name": "大熊猫",
        "category": "mammals",
        "scientific_name": "Ailuropoda melanoleuca",
        "conservation_status": "易危（VU）",
        "image": "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241022/emyrja/dog_and_girl.jpeg",
        "description": "大熊猫是中国特有种，现存的主要栖息地是中国四川、陕西和甘肃的山区。",
        "characteristics": [
            "体型：体长120-180厘米，体重80-120公斤",
            "外观：黑白相间的皮毛，圆脸，大黑眼圈",
            "寿命：野生约20年，人工饲养可达30年",
            "食性：主要以竹子为食（99%），偶尔吃肉"
        ],
        "habitat": "温带森林，海拔2600-3500米的竹林",
        "distribution": "中国四川、陕西、甘肃",
        "population": "野生约1864只（2014年数据）",
        "facts": [
            "大熊猫每天要吃12-38公斤竹子",
            "新生大熊猫只有100克重，相当于妈妈体重的1/900",
            "大熊猫的第六指（伪拇指）帮助它们抓握竹子",
            "大熊猫是中国的国宝，也是世界自然基金会的标志"
        ],
        "threats": [
            "栖息地破碎化",
            "气候变化影响竹子生长",
            "繁殖率低"
        ]
    },
    "tiger": {
        "name": "老虎",
        "category": "mammals",
        "scientific_name": "Panthera tigris",
        "conservation_status": "濒危（EN）",
        "image": "https://images.unsplash.com/photo-1561731216-c3a4d99437d5?w=800",
        "description": "老虎是世界上最大的猫科动物，拥有强大的力量和敏捷的身手。",
        "characteristics": [
            "体型：体长140-280厘米，体重90-306公斤",
            "外观：橙黄色毛皮配黑色条纹，腹部白色",
            "寿命：野生约10-15年，人工饲养可达20年",
            "食性：肉食性，捕食鹿、野猪等大型哺乳动物"
        ],
        "habitat": "热带雨林、温带森林、草原",
        "distribution": "亚洲（印度、中国、俄罗斯等）",
        "population": "全球约3900只野生老虎",
        "facts": [
            "老虎是独居动物，领地意识强",
            "老虎的条纹是独特的，如同人类指纹",
            "老虎可以一跃跳过5米高度",
            "老虎的吼声可传播3公里"
        ],
        "threats": [
            "非法狩猎和盗猎",
            "栖息地丧失",
            "人虎冲突"
        ]
    },
    "elephant": {
        "name": "非洲象",
        "category": "mammals",
        "scientific_name": "Loxodonta africana",
        "conservation_status": "易危（VU）",
        "image": "https://images.unsplash.com/photo-1564760055775-d63b17a55c44?w=800",
        "description": "非洲象是陆地上最大的哺乳动物，以其智慧和社会性著称。",
        "characteristics": [
            "体型：高3-4米，体重可达6000公斤",
            "外观：灰色皮肤，大耳朵，长鼻子",
            "寿命：可达60-70年",
            "食性：草食性，每天吃150公斤植物"
        ],
        "habitat": "草原、森林、沙漠边缘",
        "distribution": "撒哈拉以南非洲",
        "population": "约41.5万只",
        "facts": [
            "大象是高度社会化动物，由母象领导族群",
            "大象怀孕期长达22个月",
            "大象使用次声波通讯，可传播数公里",
            "大象有极好的记忆力"
        ],
        "threats": [
            "象牙盗猎",
            "栖息地减少",
            "人象冲突"
        ]
    },
    
    # 鸟类
    "eagle": {
        "name": "金雕",
        "category": "birds",
        "scientific_name": "Aquila chrysaetos",
        "conservation_status": "无危（LC）",
        "image": "https://images.unsplash.com/photo-1611689342806-0863700ce1e4?w=800",
        "description": "金雕是北半球最大的猛禽之一，以其卓越的狩猎技巧闻名。",
        "characteristics": [
            "翼展：180-234厘米",
            "体重：3-6.5公斤",
            "寿命：野生约30年，人工饲养可达50年",
            "食性：肉食性，捕食兔子、土拨鼠等"
        ],
        "habitat": "山地、高原、草原",
        "distribution": "北半球温带和亚寒带",
        "population": "全球约30万只",
        "facts": [
            "金雕俯冲速度可达每小时320公里",
            "视力是人类的8倍",
            "可以抓起15公斤的猎物",
            "终身配偶制"
        ],
        "threats": [
            "栖息地破坏",
            "人为干扰",
            "食物链污染"
        ]
    },
    "penguin": {
        "name": "帝企鹅",
        "category": "birds",
        "scientific_name": "Aptenodytes forsteri",
        "conservation_status": "近危（NT）",
        "image": "https://images.unsplash.com/photo-1551986782-d0169b3f8fa7?w=800",
        "description": "帝企鹅是企鹅家族中体型最大的成员，生活在南极极端环境中。",
        "characteristics": [
            "身高：可达120厘米",
            "体重：22-45公斤",
            "寿命：约20年",
            "食性：以鱼类、鱿鱼、甲壳类为食"
        ],
        "habitat": "南极冰架和周围海域",
        "distribution": "南极洲",
        "population": "约60万只",
        "facts": [
            "可潜水至500米深度",
            "在零下40度的严冬孵蛋",
            "雄性企鹅孵蛋期间禁食100多天",
            "企鹅不会飞，但游泳速度可达36公里/小时"
        ],
        "threats": [
            "气候变化导致海冰减少",
            "海洋污染",
            "过度捕捞影响食物来源"
        ]
    },
    
    # 爬行动物
    "crocodile": {
        "name": "尼罗鳄",
        "category": "reptiles",
        "scientific_name": "Crocodylus niloticus",
        "conservation_status": "无危（LC）",
        "image": "https://images.unsplash.com/photo-1535083783855-76ae62b2914e?w=800",
        "description": "尼罗鳄是非洲最大的爬行动物，也是最危险的鳄鱼之一。",
        "characteristics": [
            "体长：可达5-6米",
            "体重：可达750公斤",
            "寿命：70-100年",
            "食性：肉食性，捕食鱼类、鸟类、哺乳动物"
        ],
        "habitat": "河流、湖泊、沼泽",
        "distribution": "撒哈拉以南非洲",
        "population": "约25-50万只",
        "facts": [
            "咬合力可达22000牛顿",
            "可在水下憋气2小时",
            "母鳄会照顾幼鳄长达2年",
            "在地球上生存了2亿多年"
        ],
        "threats": [
            "栖息地丧失",
            "人类活动干扰",
            "气候变化"
        ]
    },
    
    # 两栖动物
    "tree_frog": {
        "name": "红眼树蛙",
        "category": "amphibians",
        "scientific_name": "Agalychnis callidryas",
        "conservation_status": "无危（LC）",
        "image": "https://images.unsplash.com/photo-1564349683136-77e08dba1ef7?w=800",
        "description": "红眼树蛙以其鲜艳的红色眼睛和绿色皮肤而闻名，是热带雨林的标志性物种。",
        "characteristics": [
            "体长：4-7厘米",
            "体重：7-14克",
            "寿命：5年",
            "食性：昆虫、小型无脊椎动物"
        ],
        "habitat": "热带雨林",
        "distribution": "中美洲",
        "population": "数量稳定",
        "facts": [
            "鲜艳的颜色用于惊吓捕食者",
            "脚趾有吸盘可攀爬植物",
            "主要在夜间活动",
            "卵产在叶片上，孵化后掉入水中"
        ],
        "threats": [
            "雨林砍伐",
            "气候变化",
            "宠物贸易"
        ]
    },
    
    # 鱼类
    "shark": {
        "name": "大白鲨",
        "category": "fish",
        "scientific_name": "Carcharodon carcharias",
        "conservation_status": "易危（VU）",
        "image": "https://images.unsplash.com/photo-1560275619-4662e36fa65c?w=800",
        "description": "大白鲨是海洋中最大的掠食性鱼类，处于食物链顶端。",
        "characteristics": [
            "体长：4-6米",
            "体重：680-1100公斤",
            "寿命：70年以上",
            "食性：肉食性，捕食鱼类、海豹、海豚"
        ],
        "habitat": "温带和热带海域",
        "distribution": "全球各大洋",
        "population": "不足3500只",
        "facts": [
            "游泳速度可达56公里/小时",
            "可探测到百万分之一的血液浓度",
            "有300多颗锯齿状牙齿",
            "每年仅发生约10起攻击人类事件"
        ],
        "threats": [
            "过度捕捞",
            "误捕",
            "海洋污染"
        ]
    },
    
    # 昆虫
    "butterfly": {
        "name": "帝王蝶",
        "category": "insects",
        "scientific_name": "Danaus plexippus",
        "conservation_status": "濒危（EN）",
        "image": "https://images.unsplash.com/photo-1526336024174-e58f5cdd8e13?w=800",
        "description": "帝王蝶以其壮观的跨大陆迁徙而闻名，是昆虫界的长距离飞行冠军。",
        "characteristics": [
            "翼展：8.9-10.2厘米",
            "体重：0.5克",
            "寿命：迁徙代可达8个月",
            "食性：幼虫吃乳草，成虫吸食花蜜"
        ],
        "habitat": "草原、田野、花园",
        "distribution": "北美、中美洲",
        "population": "数量急剧下降",
        "facts": [
            "每年迁徙距离可达4800公里",
            "四代蝴蝶完成一个迁徙周期",
            "体内含有毒素，捕食者不敢吃",
            "可以利用地磁导航"
        ],
        "threats": [
            "栖息地丧失",
            "农药使用",
            "气候变化"
        ]
    }
}

# 根据类别获取动物列表
def get_animals_by_category(category):
    return {k: v for k, v in ANIMALS_DATA.items() if v['category'] == category}

# 获取动物详情
def get_animal_detail(animal_id):
    return ANIMALS_DATA.get(animal_id)

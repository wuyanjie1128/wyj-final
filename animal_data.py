# Animal database - categories, data, and science notes

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
    # Your existing dataset...
    # (Keep all your animal entries here unchanged)
}

# Get animals by category
def get_animals_by_category(category):
    return {k: v for k, v in ANIMALS_DATA.items() if v["category"] == category}

# Get animal detail
def get_animal_detail(animal_id):
    return ANIMALS_DATA.get(animal_id)

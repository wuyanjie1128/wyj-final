# Featured Animal Database (English)
# A curated set of representative animals for each category.
# Global coverage is provided by GBIF in the app.

ANIMAL_CATEGORIES = {
    "mammals": {
        "name": "Mammals",
        "icon": "fa-paw",
        "color": "from-orange-400 to-red-500",
        "description": (
            "Warm-blooded vertebrates characterized by hair or fur, milk production, "
            "and typically live birth. Mammals range from tiny insectivores to the "
            "largest whales and show complex behaviors and diverse ecological roles."
        ),
        "count": 5500
    },
    "birds": {
        "name": "Birds",
        "icon": "fa-dove",
        "color": "from-blue-400 to-cyan-500",
        "description": (
            "Feathered, warm-blooded vertebrates with beaks. Many species fly, while "
            "others are specialized for running or swimming. Birds are essential for "
            "pollination, seed dispersal, and ecosystem balance."
        ),
        "count": 10000
    },
    "reptiles": {
        "name": "Reptiles",
        "icon": "fa-dragon",
        "color": "from-green-400 to-emerald-500",
        "description": (
            "Cold-blooded vertebrates usually covered in scales. Most lay eggs, and many "
            "are key predators in their habitats. They inhabit deserts, forests, wetlands, "
            "and oceans."
        ),
        "count": 10000
    },
    "amphibians": {
        "name": "Amphibians",
        "icon": "fa-frog",
        "color": "from-teal-400 to-green-500",
        "description": (
            "Moist-skinned vertebrates that often transition between aquatic and terrestrial "
            "life stages. They are highly sensitive to environmental changes and are important "
            "indicators of ecosystem health."
        ),
        "count": 7000
    },
    "fish": {
        "name": "Fish",
        "icon": "fa-fish",
        "color": "from-indigo-400 to-blue-500",
        "description": (
            "Aquatic vertebrates that breathe mostly through gills. They include jawless, "
            "cartilaginous, and bony fish with extraordinary adaptations to reefs, rivers, "
            "deep seas, and polar waters."
        ),
        "count": 32000
    },
    "insects": {
        "name": "Insects",
        "icon": "fa-bug",
        "color": "from-purple-400 to-pink-500",
        "description": (
            "Six-legged arthropods with exoskeletons. The most diverse animal group on Earth. "
            "They are vital for pollination, decomposition, and food webs."
        ),
        "count": 1000000
    }
}


def _animal(
    name,
    category,
    scientific_name,
    status,
    image,
    description,
    habitat="Various (see description)",
    distribution="Worldwide (varies by species)",
    population="Varies",
    characteristics=None,
    facts=None,
    threats=None
):
    return {
        "name": name,
        "category": category,
        "scientific_name": scientific_name,
        "conservation_status": status,
        "image": image,
        "description": description,
        "characteristics": characteristics or [],
        "habitat": habitat,
        "distribution": distribution,
        "population": population,
        "facts": facts or [],
        "threats": threats or []
    }


# Expanded featured set (representative, not exhaustive)
ANIMALS_DATA = {
    # Mammals
    "ferret": _animal(
        "Ferret", "mammals", "Mustela putorius furo", "Domesticated",
        "https://images.unsplash.com/photo-1540573133985-87b6da6d54a9?w=800",
        "A domesticated mustelid known for a slender body, playful behavior, and curiosity.",
        habitat="Human care; historically derived from European polecats",
        distribution="Worldwide (domesticated)",
        facts=["Often confused with weasels, mink, and polecats in photos."]
    ),
    "giant_panda": _animal(
        "Giant Panda", "mammals", "Ailuropoda melanoleuca", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1540573133985-87b6da6d54a9?w=800",
        "A bamboo specialist endemic to China with distinctive black-and-white fur.",
        habitat="Temperate mountain forests with bamboo",
        distribution="China"
    ),
    "tiger": _animal(
        "Tiger", "mammals", "Panthera tigris", "Endangered (EN)",
        "https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=800",
        "The largest cat species, a powerful solitary predator with unique stripe patterns.",
        habitat="Forests, grasslands, wetlands",
        distribution="Asia"
    ),
    "african_elephant": _animal(
        "African Bush Elephant", "mammals", "Loxodonta africana", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=800",
        "The largest land mammal, known for intelligence and complex social structure.",
        habitat="Savannas, forests",
        distribution="Sub-Saharan Africa"
    ),
    "lion": _animal(
        "Lion", "mammals", "Panthera leo", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1546182990-1b5e9a5f6c7f?w=800",
        "A social big cat living in prides, dominating many African savannas.",
        habitat="Savannas and grasslands",
        distribution="Africa; small population in India"
    ),
    "polar_bear": _animal(
        "Polar Bear", "mammals", "Ursus maritimus", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1525869916826-972885c91c1e?w=800",
        "A sea-ice-dependent predator superbly adapted to Arctic conditions.",
        habitat="Arctic sea ice and coasts",
        distribution="Arctic Circle"
    ),
    "red_panda": _animal(
        "Red Panda", "mammals", "Ailurus fulgens", "Endangered (EN)",
        "https://images.unsplash.com/photo-1526336024174-7c8d9e0f1a2b?w=800",
        "A forest-dwelling mammal often confused with raccoons due to facial markings.",
        habitat="Temperate forests with bamboo",
        distribution="Himalayas and southwestern China"
    ),
    "raccoon": _animal(
        "Raccoon", "mammals", "Procyon lotor", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=800",
        "An adaptable omnivore known for a mask-like face and dexterous paws.",
        habitat="Forests, wetlands, urban areas",
        distribution="North America; introduced elsewhere"
    ),
    "sea_otter": _animal(
        "Sea Otter", "mammals", "Enhydra lutris", "Endangered (EN) in some regions",
        "https://images.unsplash.com/photo-1540573133985-4d7d1a1f5c1f?w=800",
        "A marine otter famous for tool use and dense fur.",
        habitat="Coastal kelp forests",
        distribution="North Pacific"
    ),
    "river_otter": _animal(
        "North American River Otter", "mammals", "Lontra canadensis", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1540573133985-4d7d1a1f5c1f?w=800",
        "A freshwater otter with playful behavior, often confused with sea otters in photos.",
        habitat="Rivers, lakes, wetlands",
        distribution="North America"
    ),

    # Birds
    "golden_eagle": _animal(
        "Golden Eagle", "birds", "Aquila chrysaetos", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1611689342806-0863700ce1e4?w=800",
        "A powerful raptor with exceptional vision and hunting ability.",
        habitat="Mountains and open country",
        distribution="Northern Hemisphere"
    ),
    "emperor_penguin": _animal(
        "Emperor Penguin", "birds", "Aptenodytes forsteri", "Near Threatened (NT)",
        "https://images.unsplash.com/photo-1551986782-d0169b3f8fa7?w=800",
        "The largest penguin species, breeding during the Antarctic winter.",
        habitat="Antarctic sea ice",
        distribution="Antarctica"
    ),
    "peregrine_falcon": _animal(
        "Peregrine Falcon", "birds", "Falco peregrinus", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1540573133985-64c1e8f4c6d0?w=800",
        "Famous for being the fastest animal in a hunting dive.",
        habitat="Cliffs, cities, open landscapes",
        distribution="Worldwide"
    ),
    "ostrich": _animal(
        "Ostrich", "birds", "Struthio camelus", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-9b1c2d3e4f5a?w=800",
        "The largest living bird, flightless but an exceptional runner.",
        habitat="Savannas and semi-deserts",
        distribution="Africa"
    ),

    # Reptiles
    "nile_crocodile": _animal(
        "Nile Crocodile", "reptiles", "Crocodylus niloticus", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1535083783855-76ae62b2914e?w=800",
        "A formidable freshwater predator and one of Africa’s largest reptiles.",
        habitat="Rivers, lakes, wetlands",
        distribution="Sub-Saharan Africa"
    ),
    "komodo_dragon": _animal(
        "Komodo Dragon", "reptiles", "Varanus komodoensis", "Endangered (EN)",
        "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=800",
        "The largest living lizard, an apex predator on a few Indonesian islands.",
        habitat="Dry forests and savannas",
        distribution="Indonesia"
    ),

    # Amphibians
    "red_eyed_tree_frog": _animal(
        "Red-Eyed Tree Frog", "amphibians", "Agalychnis callidryas", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1564349683136-77e08dba1ef7?w=800",
        "A vivid rainforest frog whose bright colors can startle predators.",
        habitat="Tropical rainforests",
        distribution="Central America"
    ),
    "axolotl": _animal(
        "Axolotl", "amphibians", "Ambystoma mexicanum", "Critically Endangered (CR)",
        "https://images.unsplash.com/photo-1583511655942-70c5d7b0e0d4?w=800",
        "A neotenic salamander that retains larval features throughout life.",
        habitat="Freshwater canals and lakes",
        distribution="Mexico"
    ),

    # Fish
    "great_white_shark": _animal(
        "Great White Shark", "fish", "Carcharodon carcharias", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1560275619-4662e36fa65c?w=800",
        "A powerful marine predator playing a key role in ocean ecosystems.",
        habitat="Temperate coastal and offshore waters",
        distribution="Worldwide"
    ),
    "seahorse": _animal(
        "Seahorse", "fish", "Hippocampus (genus)", "Varies by species",
        "https://images.unsplash.com/photo-1526336024174-33cc44dd55ee?w=800",
        "Unique fish known for male pregnancy and upright posture.",
        habitat="Seagrass beds and reefs",
        distribution="Worldwide"
    ),

    # Insects
    "monarch_butterfly": _animal(
        "Monarch Butterfly", "insects", "Danaus plexippus", "Endangered (EN)",
        "https://images.unsplash.com/photo-1526336024174-e58f5cdd8e13?w=800",
        "Famous for long-distance migration and dependence on milkweed.",
        habitat="Fields, gardens, grasslands",
        distribution="North America and beyond"
    ),
    "honey_bee": _animal(
        "Western Honey Bee", "insects", "Apis mellifera", "Managed/Domesticated",
        "https://images.unsplash.com/photo-1472141521881-95d0e87e2e39?w=800",
        "A key pollinator essential to agriculture and natural ecosystems.",
        habitat="Varied",
        distribution="Worldwide"
    ),
}


def get_animals_by_category(category):
    return {k: v for k, v in ANIMALS_DATA.items() if v["category"] == category}


def get_animal_detail(animal_id):
    return ANIMALS_DATA.get(animal_id)

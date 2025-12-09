# Featured Animal Database (English)
# This is a curated set of representative animals.
# The "Global Animal Encyclopedia" tab covers massive species coverage via GBIF + Wikipedia.

ANIMAL_CATEGORIES = {
    "mammals": {
        "name": "Mammals",
        "icon": "fa-paw",
        "color": "from-orange-400 to-red-500",
        "description": (
            "Warm-blooded vertebrates characterized by hair or fur, "
            "live birth in most species, and milk production for feeding young. "
            "Mammals occupy nearly every habitat on Earth and show complex social "
            "behavior, advanced cognition, and diverse diets."
        ),
        "count": 5500
    },
    "birds": {
        "name": "Birds",
        "icon": "fa-dove",
        "color": "from-blue-400 to-cyan-500",
        "description": (
            "Feathered, warm-blooded vertebrates with beaks and lightweight skeletons. "
            "Many species can fly; others are exceptional runners or swimmers. "
            "Birds play key roles in pollination, seed dispersal, and ecosystem balance."
        ),
        "count": 10000
    },
    "reptiles": {
        "name": "Reptiles",
        "icon": "fa-dragon",
        "color": "from-green-400 to-emerald-500",
        "description": (
            "Cold-blooded vertebrates typically covered in scales or scutes. "
            "Most lay eggs, though some give live birth. "
            "Reptiles are important predators and prey across deserts, forests, "
            "wetlands, and marine environments."
        ),
        "count": 10000
    },
    "amphibians": {
        "name": "Amphibians",
        "icon": "fa-frog",
        "color": "from-teal-400 to-green-500",
        "description": (
            "Moist-skinned vertebrates that often begin life in water and transition "
            "to land through metamorphosis. "
            "They are sensitive indicators of environmental health and are threatened "
            "by habitat loss, pollution, and disease."
        ),
        "count": 7000
    },
    "fish": {
        "name": "Fish",
        "icon": "fa-fish",
        "color": "from-indigo-400 to-blue-500",
        "description": (
            "Aquatic vertebrates that breathe primarily through gills. "
            "Fish include jawless, cartilaginous, and bony groups with remarkable "
            "adaptations for deep sea, coral reefs, rivers, and polar waters."
        ),
        "count": 32000
    },
    "insects": {
        "name": "Insects",
        "icon": "fa-bug",
        "color": "from-purple-400 to-pink-500",
        "description": (
            "Six-legged arthropods with segmented bodies and exoskeletons. "
            "They represent the most diverse animal group on Earth. "
            "Insects are essential for pollination, decomposition, and food webs, "
            "though some species are agricultural pests or disease vectors."
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


ANIMALS_DATA = {
    # -------------------
    # Mammals (12)
    # -------------------
    "giant_panda": _animal(
        "Giant Panda", "mammals", "Ailuropoda melanoleuca", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1540573133985-87b6da6d54a9?w=800",
        "An iconic bamboo specialist native to China, known for its black-and-white coat and gentle behavior.",
        habitat="Temperate mountain forests with dense bamboo",
        distribution="China",
        characteristics=[
            "Pseudo-thumb for gripping bamboo",
            "Low-energy lifestyle adapted to a fibrous diet"
        ],
        facts=[
            "A symbol of global wildlife conservation."
        ],
        threats=["Habitat fragmentation", "Climate impacts on bamboo"]
    ),
    "tiger": _animal(
        "Tiger", "mammals", "Panthera tigris", "Endangered (EN)",
        "https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=800",
        "The largest cat species, a powerful solitary predator with unique stripe patterns.",
        habitat="Forests, grasslands, wetlands",
        distribution="Asia",
        threats=["Poaching", "Habitat loss"]
    ),
    "african_elephant": _animal(
        "African Bush Elephant", "mammals", "Loxodonta africana", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=800",
        "The largest land mammal, highly intelligent and essential for shaping savanna and forest ecosystems.",
        habitat="Savannas, forests",
        distribution="Sub-Saharan Africa",
        threats=["Ivory poaching", "Human-elephant conflict"]
    ),
    "gray_wolf": _animal(
        "Gray Wolf", "mammals", "Canis lupus", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1546182990-8b3b1b3b5b5d?w=800",
        "A social, pack-living apex predator with complex communication and cooperative hunting.",
        habitat="Forests, tundra, grasslands",
        distribution="North America, Europe, Asia"
    ),
    "polar_bear": _animal(
        "Polar Bear", "mammals", "Ursus maritimus", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1525869916826-972885c91c1e?w=800",
        "A sea-ice-dependent predator superbly adapted to Arctic conditions.",
        habitat="Arctic sea ice and coasts",
        distribution="Arctic Circle",
        threats=["Sea-ice loss"]
    ),
    "chimpanzee": _animal(
        "Chimpanzee", "mammals", "Pan troglodytes", "Endangered (EN)",
        "https://images.unsplash.com/photo-1540573133985-4d7d1a1f5c1f?w=800",
        "One of humans’ closest relatives, known for tool use and rich social life.",
        habitat="Tropical forests and woodlands",
        distribution="Central and West Africa",
        threats=["Habitat loss", "Illegal trade"]
    ),
    "blue_whale": _animal(
        "Blue Whale", "mammals", "Balaenoptera musculus", "Endangered (EN)",
        "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800",
        "The largest animal ever known to have lived, feeding mainly on krill.",
        habitat="Open oceans",
        distribution="Worldwide"
    ),
    "bottlenose_dolphin": _animal(
        "Bottlenose Dolphin", "mammals", "Tursiops truncatus", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1500375592092-40eb2168fd21?w=800",
        "Highly intelligent marine mammal with complex vocal communication.",
        habitat="Coastal and offshore waters",
        distribution="Worldwide"
    ),
    "lion": _animal(
        "Lion", "mammals", "Panthera leo", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1546182990-bb0d2c3e8b7b?w=800",
        "A social big cat that lives in prides and dominates many African savanna ecosystems.",
        habitat="Savannas and grasslands",
        distribution="Sub-Saharan Africa, small population in India"
    ),
    "red_kangaroo": _animal(
        "Red Kangaroo", "mammals", "Osphranter rufus", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-3d3f1c9f9e9a?w=800",
        "The largest marsupial, adapted to Australia's arid interior.",
        habitat="Semi-arid and arid landscapes",
        distribution="Australia"
    ),
    "platypus": _animal(
        "Platypus", "mammals", "Ornithorhynchus anatinus", "Near Threatened (NT)",
        "https://images.unsplash.com/photo-1601758125946-6ec2ef64daf8?w=800",
        "A unique egg-laying mammal with a duck-like bill and electroreception.",
        habitat="Rivers and freshwater systems",
        distribution="Eastern Australia, Tasmania"
    ),
    "koala": _animal(
        "Koala", "mammals", "Phascolarctos cinereus", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1526336024174-0d1f4a3b5d2e?w=800",
        "A eucalyptus specialist with a low-energy lifestyle and strong tree dependence.",
        habitat="Eucalyptus forests",
        distribution="Australia"
    ),

    # -------------------
    # Birds (10)
    # -------------------
    "golden_eagle": _animal(
        "Golden Eagle", "birds", "Aquila chrysaetos", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1611689342806-0863700ce1e4?w=800",
        "One of the most powerful raptors, with exceptional vision and hunting ability.",
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
        "Famous for being the fastest animal in a dive.",
        habitat="Cliffs, cities, open landscapes",
        distribution="Worldwide"
    ),
    "bald_eagle": _animal(
        "Bald Eagle", "birds", "Haliaeetus leucocephalus", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1500375592092-8b1c3a1f5c6f?w=800",
        "A large fish-eating raptor and national symbol of the United States.",
        habitat="Near lakes, rivers, coasts",
        distribution="North America"
    ),
    "scarlet_macaw": _animal(
        "Scarlet Macaw", "birds", "Ara macao", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1540573133985-1fdc1b7b5c3f?w=800",
        "A brilliantly colored parrot of tropical forests.",
        habitat="Lowland rainforests",
        distribution="Central and South America"
    ),
    "ostrich": _animal(
        "Ostrich", "birds", "Struthio camelus", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-9b1c2d3e4f5a?w=800",
        "The largest living bird, flightless but an exceptional runner.",
        habitat="Savannas and semi-deserts",
        distribution="Africa"
    ),
    "albatross": _animal(
        "Wandering Albatross", "birds", "Diomedea exulans", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1500375592092-0b1c2d3e4f5a?w=800",
        "A master of long-distance ocean flight with the largest wingspan of any bird.",
        habitat="Open Southern Ocean",
        distribution="Southern Hemisphere"
    ),
    "snowy_owl": _animal(
        "Snowy Owl", "birds", "Bubo scandiacus", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1540573133985-2b3c4d5e6f7a?w=800",
        "A striking white owl adapted to Arctic tundra.",
        habitat="Tundra",
        distribution="Arctic regions"
    ),
    "hummingbird": _animal(
        "Ruby-throated Hummingbird", "birds", "Archilochus colubris", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-7c8d9e0f1a2b?w=800",
        "A tiny bird capable of hovering and rapid wingbeats.",
        habitat="Woodlands, gardens",
        distribution="North America"
    ),
    "mute_swan": _animal(
        "Mute Swan", "birds", "Cygnus olor", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1500375592092-3c4d5e6f7a8b?w=800",
        "A large waterbird known for elegant appearance.",
        habitat="Lakes and slow rivers",
        distribution="Europe and introduced elsewhere"
    ),

    # -------------------
    # Reptiles (8)
    # -------------------
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
    "green_sea_turtle": _animal(
        "Green Sea Turtle", "reptiles", "Chelonia mydas", "Endangered (EN)",
        "https://images.unsplash.com/photo-1544551763-7f2a9b4c1b3e?w=800",
        "A large marine turtle that shifts toward herbivory as it matures.",
        habitat="Tropical and subtropical seas",
        distribution="Worldwide"
    ),
    "king_cobra": _animal(
        "King Cobra", "reptiles", "Ophiophagus hannah", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=800",
        "The world’s longest venomous snake, known for feeding on other snakes.",
        habitat="Forests and agricultural edges",
        distribution="South and Southeast Asia"
    ),
    "gila_monster": _animal(
        "Gila Monster", "reptiles", "Heloderma suspectum", "Near Threatened (NT)",
        "https://images.unsplash.com/photo-1526336024174-1a2b3c4d5e6f?w=800",
        "A slow-moving venomous lizard adapted to arid environments.",
        habitat="Deserts and scrublands",
        distribution="Southwestern United States, Mexico"
    ),
    "anaconda": _animal(
        "Green Anaconda", "reptiles", "Eunectes murinus", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-2a3b4c5d6e7f?w=800",
        "One of the heaviest snakes, semi-aquatic and an ambush predator.",
        habitat="Swamps and rivers",
        distribution="South America"
    ),
    "iguana": _animal(
        "Green Iguana", "reptiles", "Iguana iguana", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-3a4b5c6d7e8f?w=800",
        "A large arboreal lizard that is mostly herbivorous.",
        habitat="Tropical forests",
        distribution="Central and South America"
    ),
    "chameleon": _animal(
        "Panther Chameleon", "reptiles", "Furcifer pardalis", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-4a5b6c7d8e9f?w=800",
        "Famous for color changes and independently moving eyes.",
        habitat="Forests and shrublands",
        distribution="Madagascar"
    ),

    # -------------------
    # Amphibians (8)
    # -------------------
    "red_eyed_tree_frog": _animal(
        "Red-Eyed Tree Frog", "amphibians", "Agalychnis callidryas", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1564349683136-77e08dba1ef7?w=800",
        "A vivid rainforest frog whose bright colors help deter predators.",
        habitat="Tropical rainforests",
        distribution="Central America"
    ),
    "axolotl": _animal(
        "Axolotl", "amphibians", "Ambystoma mexicanum", "Critically Endangered (CR)",
        "https://images.unsplash.com/photo-1583511655942-70c5d7b0e0d4?w=800",
        "A neotenic salamander that retains larval features throughout life.",
        habitat="Freshwater lakes and canals",
        distribution="Mexico (historically Lake Xochimilco)"
    ),
    "poison_dart_frog": _animal(
        "Poison Dart Frog", "amphibians", "Dendrobatidae (family)", "Varies by species",
        "https://images.unsplash.com/photo-1526336024174-5a6b7c8d9e0f?w=800",
        "Small, brightly colored frogs with powerful toxins in some species.",
        habitat="Tropical forests",
        distribution="Central and South America"
    ),
    "american_bullfrog": _animal(
        "American Bullfrog", "amphibians", "Lithobates catesbeianus", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-6a7b8c9d0e1f?w=800",
        "A large frog that is both a predator and an invasive species in some regions.",
        habitat="Ponds, lakes, slow rivers",
        distribution="North America; introduced elsewhere"
    ),
    "fire_salamander": _animal(
        "Fire Salamander", "amphibians", "Salamandra salamandra", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-7a8b9c0d1e2f?w=800",
        "A striking black-and-yellow salamander associated with European forests.",
        habitat="Moist woodlands",
        distribution="Europe"
    ),
    "glass_frog": _animal(
        "Glass Frog", "amphibians", "Centrolenidae (family)", "Varies by species",
        "https://images.unsplash.com/photo-1526336024174-8a9b0c1d2e3f?w=800",
        "Known for translucent skin that can reveal internal organs.",
        habitat="Cloud forests near streams",
        distribution="Central and South America"
    ),
    "toad": _animal(
        "Common Toad", "amphibians", "Bufo bufo", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-9a0b1c2d3e4f?w=800",
        "A robust toad with strong terrestrial adaptations.",
        habitat="Forests, gardens, farmland",
        distribution="Europe"
    ),
    "newt": _animal(
        "Eastern Newt", "amphibians", "Notophthalmus viridescens", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-0a1b2c3d4e5f?w=800",
        "A small salamander with a complex life cycle.",
        habitat="Ponds and surrounding forests",
        distribution="Eastern North America"
    ),

    # -------------------
    # Fish (10)
    # -------------------
    "great_white_shark": _animal(
        "Great White Shark", "fish", "Carcharodon carcharias", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1560275619-4662e36fa65c?w=800",
        "A powerful marine predator playing an important role in ocean ecosystems.",
        habitat="Temperate coastal and offshore waters",
        distribution="Worldwide"
    ),
    "whale_shark": _animal(
        "Whale Shark", "fish", "Rhincodon typus", "Endangered (EN)",
        "https://images.unsplash.com/photo-1544551763-7f2a9b4c1b3e?w=800",
        "The largest fish on Earth, a gentle filter-feeder.",
        habitat="Warm tropical seas",
        distribution="Worldwide"
    ),
    "clownfish": _animal(
        "Clownfish", "fish", "Amphiprioninae (subfamily)", "Varies by species",
        "https://images.unsplash.com/photo-1516685018646-549d2d0b0f24?w=800",
        "Famous for symbiosis with sea anemones.",
        habitat="Coral reefs",
        distribution="Indo-Pacific"
    ),
    "blue_tang": _animal(
        "Blue Tang", "fish", "Paracanthurus hepatus", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1544551763-92b8b3b6f0f5?w=800",
        "A bright reef fish that grazes on algae.",
        habitat="Coral reefs",
        distribution="Indo-Pacific"
    ),
    "salmon": _animal(
        "Atlantic Salmon", "fish", "Salmo salar", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-11aa22bb33cc?w=800",
        "A migratory fish that moves between ocean and freshwater to spawn.",
        habitat="Rivers and North Atlantic",
        distribution="North Atlantic region"
    ),
    "betta": _animal(
        "Siamese Fighting Fish", "fish", "Betta splendens", "Vulnerable (VU)",
        "https://images.unsplash.com/photo-1526336024174-22bb33cc44dd?w=800",
        "A popular aquarium fish known for vivid colors and territorial behavior.",
        habitat="Slow-moving freshwater",
        distribution="Southeast Asia"
    ),
    "seahorse": _animal(
        "Seahorse", "fish", "Hippocampus (genus)", "Varies by species",
        "https://images.unsplash.com/photo-1526336024174-33cc44dd55ee?w=800",
        "Unique fish with male pregnancy and upright posture.",
        habitat="Seagrass beds and reefs",
        distribution="Worldwide"
    ),
    "manta_ray": _animal(
        "Giant Manta Ray", "fish", "Mobula birostris", "Endangered (EN)",
        "https://images.unsplash.com/photo-1544551763-05f0c5e6c7d8?w=800",
        "A large filter-feeding ray with advanced cognitive behaviors.",
        habitat="Open ocean and coastal waters",
        distribution="Tropical and subtropical seas"
    ),
    "piranha": _animal(
        "Red-bellied Piranha", "fish", "Pygocentrus nattereri", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-44dd55ee66ff?w=800",
        "A freshwater fish known for strong jaws and opportunistic feeding.",
        habitat="Rivers and floodplains",
        distribution="South America"
    ),
    "coelacanth": _animal(
        "Coelacanth", "fish", "Latimeria chalumnae", "Critically Endangered (CR)",
        "https://images.unsplash.com/photo-1526336024174-55ee66ff77aa?w=800",
        "A rare deep-sea fish once thought extinct, often called a 'living fossil'.",
        habitat="Deep marine caves",
        distribution="Western Indian Ocean"
    ),

    # -------------------
    # Insects (12)
    # -------------------
    "monarch_butterfly": _animal(
        "Monarch Butterfly", "insects", "Danaus plexippus", "Endangered (EN)",
        "https://images.unsplash.com/photo-1526336024174-e58f5cdd8e13?w=800",
        "Famous for long-distance migration and dependence on milkweed.",
        habitat="Fields, gardens, grasslands",
        distribution="North America and beyond"
    ),
    "honey_bee": _animal(
        "Western Honey Bee", "insects", "Apis mellifera", "Domesticated/Managed",
        "https://images.unsplash.com/photo-1472141521881-95d0e87e2e39?w=800",
        "A key pollinator species essential to agriculture and natural ecosystems.",
        habitat="Varied",
        distribution="Worldwide"
    ),
    "ladybug": _animal(
        "Seven-spotted Ladybird", "insects", "Coccinella septempunctata", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=800",
        "A beneficial predator of aphids and other crop pests.",
        habitat="Gardens, fields",
        distribution="Europe; introduced elsewhere"
    ),
    "dragonfly": _animal(
        "Emperor Dragonfly", "insects", "Anax imperator", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-66ff77aa88bb?w=800",
        "A fast aerial hunter with aquatic larvae.",
        habitat="Lakes and ponds",
        distribution="Europe, North Africa"
    ),
    "praying_mantis": _animal(
        "European Mantis", "insects", "Mantis religiosa", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-77aa88bb99cc?w=800",
        "A sit-and-wait predator known for its folded forelegs.",
        habitat="Grasslands and shrubs",
        distribution="Europe, Asia, Africa"
    ),
    "stag_beetle": _animal(
        "Stag Beetle", "insects", "Lucanus cervus", "Near Threatened (NT)",
        "https://images.unsplash.com/photo-1526336024174-88bb99cc00dd?w=800",
        "Large beetle with impressive mandibles in males.",
        habitat="Woodlands",
        distribution="Europe"
    ),
    "atlas_moth": _animal(
        "Atlas Moth", "insects", "Attacus atlas", "Least Concern (LC)",
        "https://images.unsplash.com/photo-1526336024174-99cc00dd11ee?w=800",
        "One of the largest moths by wing surface area.",
        habitat="Tropical forests",
        distribution="South and Southeast Asia"
    ),
    "firefly": _animal(
        "Common Firefly", "insects", "Lampyridae (family)", "Varies by species",
        "https://images.unsplash.com/photo-1526336024174-aabbccddeeff?w=800",
        "Bioluminescent beetles that use light for communication and mating.",
        habitat="Moist fields and forests",
        distribution="Worldwide"
    ),
    "leafcutter_ant": _animal(
        "Leafcutter Ant", "insects", "Atta (genus)", "Varies by species",
        "https://images.unsplash.com/photo-1526336024174-bbccddeeff00?w=800",
        "Farms fungus using harvested leaves, forming complex societies.",
        habitat="Tropical forests",
        distribution="Central and South America"
    ),
    "silkworm": _animal(
        "Silkworm", "insects", "Bombyx mori", "Domesticated",
        "https://images.unsplash.com/photo-1526336024174-ccddee001122?w=800",
        "A domesticated moth species central to silk production.",
        habitat="Human-managed",
        distribution="Worldwide (domesticated)"
    ),
    "mosquito": _animal(
        "Aedes Mosquito", "insects", "Aedes (genus)", "Varies by species",
        "https://images.unsplash.com/photo-1526336024174-ddee00112233?w=800",
        "Important disease vectors; ecology varies widely among species.",
        habitat="Areas with standing water",
        distribution="Worldwide"
    ),
    "grasshopper": _animal(
        "Desert Locust", "insects", "Schistocerca gregaria", "Agricultural pest",
        "https://images.unsplash.com/photo-1526336024174-ee0011223344?w=800",
        "A locust species capable of massive swarms affecting agriculture.",
        habitat="Semi-arid regions",
        distribution="Africa, Middle East, South Asia"
    ),
}


# Get animals by category
def get_animals_by_category(category):
    return {k: v for k, v in ANIMALS_DATA.items() if v["category"] == category}


# Get animal detail
def get_animal_detail(animal_id):
    return ANIMALS_DATA.get(animal_id)

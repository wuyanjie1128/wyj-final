# Animal database - categories, featured animals, and science notes

ANIMAL_CATEGORIES = {
    "mammals": {
        "name": "Mammals",
        "icon": "fa-paw",
        "color": "from-orange-400 to-red-500",
        "description": "Warm-blooded vertebrates that give live birth and nurse their young.",
        "count": 5500
    },
    "birds": {
        "name": "Birds",
        "icon": "fa-dove",
        "color": "from-blue-400 to-cyan-500",
        "description": "Feathered warm-blooded vertebrates; many species can fly.",
        "count": 10000
    },
    "reptiles": {
        "name": "Reptiles",
        "icon": "fa-dragon",
        "color": "from-green-400 to-emerald-500",
        "description": "Cold-blooded vertebrates with scales; most lay eggs.",
        "count": 10000
    },
    "amphibians": {
        "name": "Amphibians",
        "icon": "fa-frog",
        "color": "from-teal-400 to-green-500",
        "description": "Animals that live both in water and on land, typically undergoing metamorphosis.",
        "count": 7000
    },
    "fish": {
        "name": "Fish",
        "icon": "fa-fish",
        "color": "from-indigo-400 to-blue-500",
        "description": "Aquatic vertebrates that breathe with gills.",
        "count": 32000
    },
    "insects": {
        "name": "Insects",
        "icon": "fa-bug",
        "color": "from-purple-400 to-pink-500",
        "description": "Six-legged arthropods with an exoskeleton and extraordinary diversity.",
        "count": 1000000
    }
}

ANIMALS_DATA = {
    # -------------------
    # Mammals
    # -------------------
    "giant_panda": {
        "name": "Giant Panda",
        "category": "mammals",
        "scientific_name": "Ailuropoda melanoleuca",
        "conservation_status": "Vulnerable (VU)",
        "image": "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241022/emyrja/dog_and_girl.jpeg",
        "description": "The giant panda is an iconic species endemic to China, primarily inhabiting mountainous regions of Sichuan, Shaanxi, and Gansu.",
        "characteristics": [
            "Size: 120–180 cm in length; 80–120 kg in weight",
            "Appearance: distinctive black-and-white fur with large eye patches",
            "Lifespan: ~20 years in the wild; up to ~30 years in captivity",
            "Diet: mainly bamboo (~99%), with occasional small animals"
        ],
        "habitat": "Temperate forests with dense bamboo understory at 2,600–3,500 meters",
        "distribution": "China (Sichuan, Shaanxi, Gansu)",
        "population": "~1,864 wild individuals (2014 estimate)",
        "facts": [
            "An adult panda may eat 12–38 kg of bamboo a day.",
            "Newborn pandas weigh around 100 grams—about 1/900 of the mother’s weight.",
            "A specialized wrist bone functions like a ‘pseudo-thumb’ for gripping bamboo.",
            "The giant panda is a global symbol of wildlife conservation."
        ],
        "threats": [
            "Habitat fragmentation",
            "Climate impacts on bamboo growth",
            "Low reproductive rate"
        ]
    },
    "tiger": {
        "name": "Tiger",
        "category": "mammals",
        "scientific_name": "Panthera tigris",
        "conservation_status": "Endangered (EN)",
        "image": "https://images.unsplash.com/photo-1561731216-c3a4d99437d5?w=800",
        "description": "The tiger is the largest cat species, renowned for its strength, stealth, and distinctive stripes.",
        "characteristics": [
            "Length: 140–280 cm; 90–306 kg",
            "Coat: orange with black stripes; white underside",
            "Lifespan: ~10–15 years in the wild; up to ~20 in captivity",
            "Diet: large ungulates such as deer and wild boar"
        ],
        "habitat": "Tropical and temperate forests, grasslands, and wetlands",
        "distribution": "Asia (India, China, Russia, Southeast Asia)",
        "population": "~3,900 wild tigers globally",
        "facts": [
            "Tigers are solitary and strongly territorial.",
            "Stripe patterns are unique to each individual, like fingerprints.",
            "They can leap roughly 5 meters in a single bound.",
            "A tiger’s roar can travel several kilometers."
        ],
        "threats": [
            "Poaching and illegal wildlife trade",
            "Habitat loss",
            "Human–tiger conflict"
        ]
    },
    "elephant": {
        "name": "African Bush Elephant",
        "category": "mammals",
        "scientific_name": "Loxodonta africana",
        "conservation_status": "Vulnerable (VU)",
        "image": "https://images.unsplash.com/photo-1564760055775-d63b17a55c44?w=800",
        "description": "The African bush elephant is the largest land mammal, famous for its intelligence, complex social bonds, and ecological importance.",
        "characteristics": [
            "Height: 3–4 m; weight up to ~6,000 kg",
            "Large ears help regulate body temperature",
            "Lifespan: ~60–70 years",
            "Diet: herbivorous; can eat ~150 kg of vegetation per day"
        ],
        "habitat": "Savannas, forests, and semi-arid regions",
        "distribution": "Sub-Saharan Africa",
        "population": "~415,000 individuals (approximate recent estimates)",
        "facts": [
            "Elephant herds are typically led by a matriarch.",
            "Gestation lasts about 22 months—the longest of any land animal.",
            "They communicate using low-frequency sounds that travel long distances.",
            "Their memory and problem-solving abilities are highly advanced."
        ],
        "threats": [
            "Ivory poaching",
            "Habitat loss and fragmentation",
            "Human–elephant conflict"
        ]
    },

    # -------------------
    # Birds
    # -------------------
    "eagle": {
        "name": "Golden Eagle",
        "category": "birds",
        "scientific_name": "Aquila chrysaetos",
        "conservation_status": "Least Concern (LC)",
        "image": "https://images.unsplash.com/photo-1611689342806-0863700ce1e4?w=800",
        "description": "The golden eagle is one of the largest raptors in the Northern Hemisphere, admired for powerful flight and exceptional hunting skills.",
        "characteristics": [
            "Wingspan: 180–234 cm",
            "Weight: 3–6.5 kg",
            "Lifespan: ~30 years in the wild; up to ~50 in captivity",
            "Diet: rabbits, marmots, and other medium-sized animals"
        ],
        "habitat": "Mountains, highlands, open grasslands",
        "distribution": "Northern Hemisphere across temperate and subarctic regions",
        "population": "Estimated ~300,000 globally",
        "facts": [
            "Dive speeds can exceed 300 km/h.",
            "Their vision is many times sharper than humans'.",
            "They may carry prey approaching their own body weight.",
            "Pairs often bond for life."
        ],
        "threats": [
            "Habitat disturbance",
            "Human conflict and persecution",
            "Contaminants in the food chain"
        ]
    },
    "penguin": {
        "name": "Emperor Penguin",
        "category": "birds",
        "scientific_name": "Aptenodytes forsteri",
        "conservation_status": "Near Threatened (NT)",
        "image": "https://images.unsplash.com/photo-1551986782-d0169b3f8fa7?w=800",
        "description": "The emperor penguin is the largest penguin species, uniquely adapted to the extreme cold of Antarctica.",
        "characteristics": [
            "Height: up to ~120 cm",
            "Weight: 22–45 kg",
            "Lifespan: ~20 years",
            "Diet: fish, squid, and krill"
        ],
        "habitat": "Antarctic sea ice and surrounding waters",
        "distribution": "Antarctica",
        "population": "Roughly ~600,000 individuals",
        "facts": [
            "They can dive to about 500 meters.",
            "Breeding occurs during the Antarctic winter.",
            "Males may fast for over 100 days while incubating eggs.",
            "They cannot fly but are powerful swimmers."
        ],
        "threats": [
            "Sea-ice loss linked to climate change",
            "Marine pollution",
            "Overfishing affecting food availability"
        ]
    },

    # -------------------
    # Reptiles
    # -------------------
    "crocodile": {
        "name": "Nile Crocodile",
        "category": "reptiles",
        "scientific_name": "Crocodylus niloticus",
        "conservation_status": "Least Concern (LC)",
        "image": "https://images.unsplash.com/photo-1535083783855-76ae62b2914e?w=800",
        "description": "The Nile crocodile is one of Africa’s largest reptiles and a formidable apex predator in freshwater ecosystems.",
        "characteristics": [
            "Length: up to ~5–6 meters",
            "Weight: up to ~750 kg",
            "Lifespan: ~70–100 years",
            "Diet: fish, birds, and mammals"
        ],
        "habitat": "Rivers, lakes, and wetlands",
        "distribution": "Sub-Saharan Africa",
        "population": "Estimated ~250,000–500,000",
        "facts": [
            "Bite force is among the strongest of any animal.",
            "They can hold their breath underwater for long periods.",
            "Mothers may guard and assist young for extended times.",
            "Crocodilian lineages date back over 200 million years."
        ],
        "threats": [
            "Habitat loss",
            "Human disturbance",
            "Climate-related ecosystem shifts"
        ]
    },

    # -------------------
    # Amphibians
    # -------------------
    "tree_frog": {
        "name": "Red-Eyed Tree Frog",
        "category": "amphibians",
        "scientific_name": "Agalychnis callidryas",
        "conservation_status": "Least Concern (LC)",
        "image": "https://images.unsplash.com/photo-1564349683136-77e08dba1ef7?w=800",
        "description": "Known for its vivid red eyes and bright green body, this frog is a classic symbol of Central American tropical rainforests.",
        "characteristics": [
            "Length: 4–7 cm",
            "Weight: ~7–14 g",
            "Lifespan: ~5 years",
            "Diet: insects and small invertebrates"
        ],
        "habitat": "Tropical rainforests",
        "distribution": "Central America",
        "population": "Stable in many areas",
        "facts": [
            "Bright colors help startle predators.",
            "Toe pads enable strong climbing ability.",
            "Primarily nocturnal.",
            "Eggs are laid on leaves above water; tadpoles drop into water after hatching."
        ],
        "threats": [
            "Deforestation",
            "Climate change",
            "Pet trade"
        ]
    },

    # -------------------
    # Fish
    # -------------------
    "shark": {
        "name": "Great White Shark",
        "category": "fish",
        "scientific_name": "Carcharodon carcharias",
        "conservation_status": "Vulnerable (VU)",
        "image": "https://images.unsplash.com/photo-1560275619-4662e36fa65c?w=800",
        "description": "A powerful ocean predator, the great white shark occupies a top position in marine food webs.",
        "characteristics": [
            "Length: ~4–6 meters (sometimes larger)",
            "Weight: ~680–1,100 kg",
            "Lifespan: likely several decades",
            "Diet: fish, seals, sea lions, and occasionally dolphins"
        ],
        "habitat": "Temperate and subtropical coastal and offshore waters",
        "distribution": "Worldwide",
        "population": "Believed to be relatively low compared to historic levels",
        "facts": [
            "They can detect extremely small traces of blood in water.",
            "Rows of serrated teeth are continuously replaced.",
            "They use electroreception to sense prey.",
            "Most interactions with humans are non-fatal and rare compared to overall ocean use."
        ],
        "threats": [
            "Overfishing",
            "Bycatch",
            "Marine pollution"
        ]
    },

    # -------------------
    # Insects
    # -------------------
    "butterfly": {
        "name": "Monarch Butterfly",
        "category": "insects",
        "scientific_name": "Danaus plexippus",
        "conservation_status": "Endangered (EN)",
        "image": "https://images.unsplash.com/photo-1526336024174-e58f5cdd8e13?w=800",
        "description": "Famous for its spectacular long-distance migration, the monarch is one of the most studied butterflies in the world.",
        "characteristics": [
            "Wingspan: 8.9–10.2 cm",
            "Weight: ~0.5 g",
            "Migratory generation can live up to ~8 months",
            "Larvae feed on milkweed; adults drink nectar"
        ],
        "habitat": "Grasslands, fields, gardens",
        "distribution": "North America and parts of Central America",
        "population": "Declining in many regions",
        "facts": [
            "Migration journeys can span thousands of kilometers.",
            "Multiple generations complete a full annual migration cycle.",
            "Milkweed-derived toxins help deter predators.",
            "They likely use a combination of sun compass and magnetic cues for navigation."
        ],
        "threats": [
            "Loss of milkweed habitat",
            "Pesticide use",
            "Climate change impacts on migration and overwintering sites"
        ]
    }
}

# Get animals by category
def get_animals_by_category(category):
    return {k: v for k, v in ANIMALS_DATA.items() if v["category"] == category}

# Get animal detail
def get_animal_detail(animal_id):
    return ANIMALS_DATA.get(animal_id)

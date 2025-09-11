QUESTIONS = {
    "cleaning_products": [
        {
            "question": "What type of cleaning products do you primarily use?",
            "options": [
                {"text": "Conventional chemical cleaners", "score": 0},
                {"text": "Mix of conventional and eco-friendly", "score": 5},
                {"text": "Certified eco-friendly products", "score": 8},
                {"text": "Natural/homemade solutions (vinegar, baking soda)", "score": 10}
            ],
            "tooltip": "Chemical cleaners can contain neonicotinoids and other harmful compounds that affect pollinator nervous systems when they enter water systems or become airborne."
        },
        {
            "question": "How do you dispose of cleaning product containers?",
            "options": [
                {"text": "Regular trash", "score": 0},
                {"text": "Recycling when possible", "score": 5},
                {"text": "Use refill stations/Zero waste options", "score": 10}
            ],
            "tooltip": "Improper disposal can lead to chemical leaching into soil and water, affecting pollinator habitats and food sources."
        },
        {
            "question": "What's your approach to fragrance in cleaning products?",
            "options": [
                {"text": "Strong artificial fragrances", "score": 0},
                {"text": "Light artificial fragrances", "score": 3},
                {"text": "Natural essential oils", "score": 7},
                {"text": "Unscented products", "score": 10}
            ],
            "tooltip": "Artificial fragrances can confuse pollinators and interfere with their ability to find flowers and food sources."
        }
    ],
    "outdoor_practices": [
        {
            "question": "How do you clean outdoor spaces?",
            "options": [
                {"text": "Chemical pressure washing", "score": 0},
                {"text": "Water only", "score": 5},
                {"text": "Natural cleaning methods", "score": 10}
            ],
            "tooltip": "Chemical runoff from outdoor cleaning directly impacts soil quality and nearby pollinator habitats."
        },
        {
            "question": "What's your approach to cleaning outdoor furniture?",
            "options": [
                {"text": "Heavy-duty chemical cleaners", "score": 0},
                {"text": "Mild soap and water", "score": 5},
                {"text": "Natural solutions (vinegar/baking soda)", "score": 10}
            ],
            "tooltip": "Residues from furniture cleaning products can transfer to visiting pollinators and affect nearby plants."
        },
        {
            "question": "How do you handle outdoor window cleaning?",
            "options": [
                {"text": "Chemical window cleaners", "score": 0},
                {"text": "Commercial eco-friendly products", "score": 5},
                {"text": "Vinegar and water solution", "score": 10}
            ],
            "tooltip": "Window cleaning products can create toxic films that are harmful to insects landing on windows or nearby surfaces."
        }
    ],
    "indoor_practices": [
        {
            "question": "What is your approach to pest control?",
            "options": [
                {"text": "Chemical pesticides", "score": 0},
                {"text": "Natural deterrents", "score": 5},
                {"text": "Prevention and non-toxic methods", "score": 10}
            ],
            "tooltip": "Pesticides are one of the biggest threats to pollinator populations, affecting both target and beneficial insects."
        },
        {
            "question": "How do you clean indoor plants?",
            "options": [
                {"text": "Chemical leaf shine products", "score": 0},
                {"text": "Damp cloth only", "score": 7},
                {"text": "Natural methods (diluted neem oil, water)", "score": 10}
            ],
            "tooltip": "Products used on indoor plants can transfer to outdoor environments through air circulation and affect visiting pollinators."
        },
        {
            "question": "What's your approach to air freshening?",
            "options": [
                {"text": "Chemical air fresheners/sprays", "score": 0},
                {"text": "Natural room sprays", "score": 5},
                {"text": "Essential oil diffusers", "score": 7},
                {"text": "Natural ventilation/plants", "score": 10}
            ],
            "tooltip": "Air fresheners can contain chemicals that persist in the environment and affect pollinator behavior when they escape outdoors."
        }
    ]
}

MAX_SCORE = sum(max(option["score"] for option in question["options"]) 
                for section in QUESTIONS.values() 
                for question in section)
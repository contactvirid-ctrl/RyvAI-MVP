# generic_templates_v2.py

templates = {
    "children": {
        "Technique": [
            {
                "id": "CH_TECH_01",
                "durationMinutes": 30,
                "sections": [
                    {"name": "Warm-up", "allowedCategories": ["warmup"], "exerciseCount": 3},
                    {"name": "Technique", "allowedCategories": ["technique"], "exerciseCount": 4},
                    {"name": "Play / Coordination", "allowedCategories": ["coordination"], "exerciseCount": 3},
                    {"name": "Strength", "allowedCategories": ["strength"], "exerciseCount": 2}
                ]
            }
        ],
        "Strength": [
            {
                "id": "CH_STR_01",
                "durationMinutes": 30,
                "sections": [
                    {"name": "Warm-up", "allowedCategories": ["warmup"], "exerciseCount": 3},
                    {"name": "Strength", "allowedCategories": ["strength"], "exerciseCount": 5},
                    {"name": "Play / Coordination", "allowedCategories": ["coordination"], "exerciseCount": 3},
                    {"name": "Technique", "allowedCategories": ["technique"], "exerciseCount": 2}
                ]
            }
        ],
        "Speed": [
            {
                "id": "CH_SPEED_01",
                "durationMinutes": 30,
                "sections": [
                    {"name": "Warm-up", "allowedCategories": ["warmup"], "exerciseCount": 3},
                    {"name": "Speed / Plyometrics", "allowedCategories": ["speed","plyometrics"], "exerciseCount": 4},
                    {"name": "Play / Coordination", "allowedCategories": ["coordination"], "exerciseCount": 3},
                    {"name": "Technique", "allowedCategories": ["technique"], "exerciseCount": 2}
                ]
            }
        ],
        "Mixed": [
            {
                "id": "CH_MIX_01",
                "durationMinutes": 30,
                "sections": [
                    {"name": "Warm-up", "allowedCategories": ["warmup"], "exerciseCount": 3},
                    {"name": "Technique", "allowedCategories": ["technique"], "exerciseCount": 3},
                    {"name": "Strength", "allowedCategories": ["strength"], "exerciseCount": 3},
                    {"name": "Speed / Plyometrics", "allowedCategories": ["speed","plyometrics"], "exerciseCount": 3},
                    {"name": "Coordination / Play", "allowedCategories": ["coordination"], "exerciseCount": 2}
                ]
            }
        ]
    },

    "beginner": {
        "Technique": [
            {
                "id": "BG_TECH_01",
                "durationMinutes": 45,
                "sections": [
                    {"name": "Warm-up", "allowedCategories": ["warmup"], "exerciseCount": 5},
                    {"name": "Technique", "allowedCategories": ["technique"], "exerciseCount": 6},
                    {"name": "Strength", "allowedCategories": ["strength"], "exerciseCount": 3},
                    {"name": "Plyometrics", "allowedCategories": ["plyometrics"], "exerciseCount": 3}
                ]
            }
        ],
        "Strength": [
            {
                "id": "BG_STR_01",
                "durationMinutes": 45,
                "sections": [
                    {"name": "Warm-up", "allowedCategories": ["warmup"], "exerciseCount": 5},
                    {"name": "Strength", "allowedCategories": ["strength"], "exerciseCount": 6},
                    {"name": "Technique", "allowedCategories": ["technique"], "exerciseCount": 3},
                    {"name": "Plyometrics", "allowedCategories": ["plyometrics"], "exerciseCount": 3}
                ]
            }
        ],
        "Speed": [
            {
                "id": "BG_SPEED_01",
                "durationMinutes": 45,
                "sections": [
                    {"name": "Warm-up", "allowedCategories": ["warmup"], "exerciseCount": 5},
                    {"name": "Speed / Plyometrics", "allowedCategories": ["speed","plyometrics"], "exerciseCount": 6},
                    {"name": "Technique", "allowedCategories": ["technique"], "exerciseCount": 3},
                    {"name": "Strength", "allowedCategories": ["strength"], "exerciseCount": 3}
                ]
            }
        ],
        "Mixed": [
            {
                "id": "BG_MIX_01",
                "durationMinutes": 45,
                "sections": [
                    {"name": "Warm-up", "allowedCategories": ["warmup"], "exerciseCount": 5},
                    {"name": "Technique", "allowedCategories": ["technique"], "exerciseCount": 4},
                    {"name": "Strength", "allowedCategories": ["strength"], "exerciseCount": 4},
                    {"name": "Speed / Plyometrics", "allowedCategories": ["speed","plyometrics"], "exerciseCount": 4}
                ]
            }
        ]
    },

    "intermediate": {
        "Technique": [
            {
                "id": "IM_TECH_01",
                "durationMinutes": 60,
                "sections": [
                    {"name": "Warm-up", "allowedCategories": ["warmup"], "exerciseCount": 6},
                    {"name": "Technique", "allowedCategories": ["technique"], "exerciseCount": 8},
                    {"name": "Strength", "allowedCategories": ["strength"], "exerciseCount": 4},
                    {"name": "Plyometrics", "allowedCategories": ["plyometrics"], "exerciseCount": 4}
                ]
            }
        ],
        "Strength": [
            {
                "id": "IM_STR_01",
                "durationMinutes": 60,
                "sections": [
                    {"name": "Warm-up", "allowedCategories": ["warmup"], "exerciseCount": 6},
                    {"name": "Strength", "allowedCategories": ["strength"], "exerciseCount": 8},
                    {"name": "Technique", "allowedCategories": ["technique"], "exerciseCount": 4},
                    {"name": "Plyometrics", "allowedCategories": ["plyometrics"], "exerciseCount": 4}
                ]
            }
        ],
        "Speed": [
            {
                "id": "IM_SPEED_01",
                "durationMinutes": 60,
                "sections": [
                    {"name": "Warm-up", "allowedCategories": ["warmup"], "exerciseCount": 6},
                    {"name": "Speed / Plyometrics", "allowedCategories": ["speed","plyometrics"], "exerciseCount": 8},
                    {"name": "Technique", "allowedCategories": ["technique"], "exerciseCount": 4},
                    {"name": "Strength", "allowedCategories": ["strength"], "exerciseCount": 4}
                ]
            }
        ],
        "Mixed": [
            {
                "id": "IM_MIX_01",
                "durationMinutes": 60,
                "sections": [
                    {"name": "Warm-up", "allowedCategories": ["warmup"], "exerciseCount": 6},
                    {"name": "Technique", "allowedCategories": ["technique"], "exerciseCount": 5},
                    {"name": "Strength", "allowedCategories": ["strength"], "exerciseCount": 5},
                    {"name": "Speed / Plyometrics", "allowedCategories": ["speed","plyometrics"], "exerciseCount": 5}
                ]
            }
        ]
    }
}

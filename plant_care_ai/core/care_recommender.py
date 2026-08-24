"""
core/care_recommender.py — Knowledge base and care recommendation engine.

Maps each plant class label to disease information and care advice.
"""

from typing import Any, Dict, List, Optional

from utils.logger import get_logger

logger = get_logger(__name__)

# ─── Knowledge Base ───────────────────────────────────────────────────────────
# Each entry maps a class label to a full care/treatment profile.
KNOWLEDGE_BASE: Dict[str, Dict[str, Any]] = {
    # ── Apple ──────────────────────────────────────────────────────────────────
    "Apple___Apple_scab": {
        "display_name": "Apple Scab",
        "description": (
            "Apple scab is a common fungal disease caused by Venturia inaequalis. "
            "It produces olive-green to black lesions on leaves and fruit, "
            "leading to premature defoliation and reduced fruit quality."
        ),
        "causes": "Fungal pathogen Venturia inaequalis, favored by cool, wet spring weather.",
        "symptoms": [
            "Olive-green to dark brown spots on upper leaf surfaces.",
            "Velvety lesions on lower leaf surfaces.",
            "Distorted or cracked fruit with corky lesions.",
            "Premature leaf and fruit drop.",
        ],
        "treatment": {
            "chemical": [
                "Apply captan fungicide (1.5–2 lb/100 gal) every 7–10 days during wet periods.",
                "Myclobutanil (Rally) provides systemic protection — apply at green tip stage.",
                "Mancozeb is effective as a protectant at 1.5–2 lb/acre.",
            ],
            "organic": [
                "Copper-based fungicides (copper hydroxide) applied preventively.",
                "Sulfur sprays every 7–14 days; avoid use above 90°F.",
                "Neem oil spray (2%) — apply early morning to avoid leaf burn.",
            ],
            "cultural": [
                "Rake and destroy fallen leaves to eliminate overwintering inoculum.",
                "Prune trees to improve air circulation and reduce humidity.",
                "Plant scab-resistant apple varieties (e.g., Redfree, Liberty, Freedom).",
            ],
        },
        "watering": (
            "Water at the base of the tree; avoid wetting foliage. "
            "Deep water 1–2 times weekly; allow soil to dry slightly between waterings."
        ),
        "sunlight": "Full sun (6–8 hours/day). Sunlight helps dry foliage and reduces fungal spread.",
        "fertilizer": (
            "Apply balanced 10-10-10 fertilizer in early spring. "
            "Avoid excessive nitrogen which promotes lush, susceptible growth."
        ),
        "prevention": [
            "Select scab-resistant varieties when replanting.",
            "Apply preventive fungicide before rain events in spring.",
            "Maintain good orchard sanitation year-round.",
            "Monitor weather forecasts and use infection risk models (e.g., RIMpro).",
        ],
    },

    "Apple___Black_rot": {
        "display_name": "Apple Black Rot",
        "description": (
            "Black rot is caused by the fungus Botryosphaeria obtusa. "
            "It attacks fruit, leaves, and bark, causing mummified fruit "
            "and cankers that can girdle and kill branches."
        ),
        "causes": "Fungal pathogen Botryosphaeria obtusa; spores spread via rain splash and insects.",
        "symptoms": [
            "Small purple spots (frogeye leaf spot) on leaves with brown centers.",
            "Fruit rot starting at blossom end, turning black and shriveled.",
            "Reddish-brown cankers on bark that can expand and girdle branches.",
            "Mummified fruit remaining on the tree through winter.",
        ],
        "treatment": {
            "chemical": [
                "Thiophanate-methyl (Topsin-M) applied at petal fall and repeat every 10–14 days.",
                "Captan fungicide as a protective spray throughout the season.",
                "Myclobutanil for both leaf spot and fruit rot control.",
            ],
            "organic": [
                "Copper fungicide sprays during dormant and early growing season.",
                "Prune and dispose of infected wood to reduce spore sources.",
            ],
            "cultural": [
                "Prune out all cankers and infected wood; disinfect pruning tools with 70% alcohol.",
                "Remove mummified fruit from the tree and ground.",
                "Avoid wounding trees which provide entry points for the pathogen.",
            ],
        },
        "watering": (
            "Drip or furrow irrigation preferred. "
            "Avoid overhead irrigation that wets foliage and spreads spores."
        ),
        "sunlight": "Full sun required for air circulation and drying of foliage.",
        "fertilizer": (
            "Balanced fertilization; excess nitrogen increases disease susceptibility. "
            "Test soil and amend accordingly."
        ),
        "prevention": [
            "Remove all mummified fruit and dead wood during dormant pruning.",
            "Apply protective fungicide at key growth stages.",
            "Manage fire blight wounds which serve as secondary entry points.",
        ],
    },

    "Apple___Cedar_apple_rust": {
        "display_name": "Cedar Apple Rust",
        "description": (
            "Cedar apple rust is caused by Gymnosporangium juniperi-virginianae, "
            "a fungus that requires two hosts: eastern red cedar (juniper) and apple. "
            "It produces bright orange spots on apple leaves."
        ),
        "causes": "Fungal pathogen Gymnosporangium juniperi-virginianae with alternating hosts.",
        "symptoms": [
            "Bright orange-yellow spots on upper leaf surfaces in spring.",
            "Tube-like structures (aecia) on lower leaf surfaces.",
            "Premature defoliation in severe infections.",
            "Orange gelatinous spore horns on juniper galls in wet weather.",
        ],
        "treatment": {
            "chemical": [
                "Myclobutanil (Eagle, Rally) — most effective systemic option.",
                "Propiconazole (Banner Maxx) applied at pink bud stage.",
                "Fenarimol sprays beginning at silver tip through petal fall.",
            ],
            "organic": [
                "Sulfur-based fungicides applied preventively.",
                "Copper sprays during dormant period on junipers.",
            ],
            "cultural": [
                "Remove nearby juniper/red cedar trees within 1 mile if feasible.",
                "Plant rust-resistant apple varieties.",
                "Apply fungicides before infection periods in spring.",
            ],
        },
        "watering": "Normal deep watering schedule; keep foliage dry.",
        "sunlight": "Full sun for at least 6 hours daily.",
        "fertilizer": "Moderate fertilization; avoid over-fertilizing with nitrogen.",
        "prevention": [
            "Plant resistant varieties such as Williams Pride or Pristine.",
            "Remove juniper galls before orange sporulation in spring.",
            "Time fungicide applications based on weather and host phenology.",
        ],
    },

    "Apple___healthy": {
        "display_name": "Healthy Apple",
        "description": "Your apple plant appears healthy! Maintain good cultural practices to keep it thriving.",
        "causes": "N/A — plant is healthy.",
        "symptoms": ["No disease symptoms detected."],
        "treatment": {
            "chemical": ["No treatment required."],
            "organic": ["Continue organic preventive practices."],
            "cultural": ["Maintain regular pruning and sanitation."],
        },
        "watering": (
            "Deep water weekly during growing season (1–1.5 inches/week). "
            "Reduce in winter. Water at base; avoid wetting foliage."
        ),
        "sunlight": "Full sun — minimum 6–8 hours of direct sunlight daily.",
        "fertilizer": (
            "Apply 10-10-10 balanced fertilizer in early spring (March–April). "
            "Young trees: 1/4 lb per year of tree age; mature trees: 1 lb/inch trunk diameter."
        ),
        "prevention": [
            "Inspect trees weekly for early signs of disease or pests.",
            "Prune in late winter to improve air circulation.",
            "Apply dormant oil spray to control overwintering insects.",
            "Maintain proper soil pH (6.0–7.0) with regular soil testing.",
        ],
    },

    # ── Tomato ─────────────────────────────────────────────────────────────────
    "Tomato___Late_blight": {
        "display_name": "Tomato Late Blight",
        "description": (
            "Late blight is caused by the oomycete Phytophthora infestans, "
            "the same pathogen responsible for the Irish potato famine. "
            "It spreads rapidly in cool, wet conditions and can destroy a crop within days."
        ),
        "causes": "Oomycete Phytophthora infestans; spread by wind-borne spores in cool, wet weather.",
        "symptoms": [
            "Large, irregular, water-soaked lesions on leaves that turn brown.",
            "White, fuzzy sporulation on leaf undersides in humid conditions.",
            "Brown-black greasy lesions on stems.",
            "Firm, brown rot on green or ripe fruit.",
            "Rapid plant collapse under epidemic conditions.",
        ],
        "treatment": {
            "chemical": [
                "Chlorothalonil (Bravo, Daconil) — broad-spectrum protectant; apply every 5–7 days.",
                "Mancozeb protective spray before infection.",
                "Cymoxanil + mancozeb combination for kickback activity (Curzate).",
                "Metalaxyl-based fungicides (Ridomil Gold) — use sparingly to avoid resistance.",
            ],
            "organic": [
                "Copper-based fungicides (copper sulfate, copper hydroxide) every 5–7 days.",
                "Bacillus subtilis (Serenade) as a biological fungicide — preventive only.",
            ],
            "cultural": [
                "Remove and destroy all infected plant material immediately.",
                "Avoid overhead irrigation; water at the base.",
                "Stake and cage plants to improve air flow.",
                "Do not compost infected material — bag and discard.",
            ],
        },
        "watering": (
            "Drip irrigation at base only. Never wet foliage. "
            "Water in the morning so any moisture dries quickly."
        ),
        "sunlight": "Full sun minimum 8 hours daily. Good air circulation is critical.",
        "fertilizer": (
            "Balanced NPK at planting; switch to low-nitrogen, high-potassium after flowering "
            "to promote fruit and disease resistance."
        ),
        "prevention": [
            "Plant late-blight-resistant varieties (Mountain Merit, Defiant, Iron Lady).",
            "Rotate crops — avoid planting tomatoes or potatoes in the same spot for 3+ years.",
            "Monitor weather forecasts; apply fungicide before high-risk periods.",
            "Destroy all volunteer potato/tomato plants.",
        ],
    },

    "Tomato___Early_blight": {
        "display_name": "Tomato Early Blight",
        "description": (
            "Early blight is caused by Alternaria solani and is one of the most common "
            "tomato diseases. It typically appears on older, lower leaves first and "
            "progresses upward, producing characteristic 'bullseye' lesions."
        ),
        "causes": "Fungal pathogen Alternaria solani; favored by warm, humid conditions.",
        "symptoms": [
            "Dark brown spots with concentric rings (bullseye pattern) on lower leaves.",
            "Yellow halo surrounding the lesions.",
            "Lesions on stems and fruit near the stem end.",
            "Premature yellowing and defoliation of lower leaves.",
        ],
        "treatment": {
            "chemical": [
                "Chlorothalonil every 7–10 days starting at first symptom.",
                "Azoxystrobin (Quadris) — systemic and curative, apply every 14 days.",
                "Mancozeb for protectant activity.",
            ],
            "organic": [
                "Copper-based spray every 7 days.",
                "Neem oil (2%) spray early morning every 7–14 days.",
                "Bacillus subtilis (Serenade) as preventive biological control.",
            ],
            "cultural": [
                "Remove affected lower leaves as soon as symptoms appear.",
                "Mulch heavily to prevent soil splash onto leaves.",
                "Rotate crops annually.",
            ],
        },
        "watering": (
            "Water at soil level using drip irrigation. "
            "Consistent moisture — avoid wet/dry extremes that stress plants."
        ),
        "sunlight": "Full sun; good air circulation reduces humidity around leaves.",
        "fertilizer": (
            "Regular balanced fertilization. Stressed, nutrient-deficient plants are more susceptible. "
            "Side-dress with compost or balanced fertilizer mid-season."
        ),
        "prevention": [
            "Plant certified disease-free seed or transplants.",
            "Space plants adequately (24–36 inches apart).",
            "Apply preventive fungicide when conditions favor disease.",
            "Remove plant debris at end of season.",
        ],
    },

    "Tomato___healthy": {
        "display_name": "Healthy Tomato",
        "description": "Your tomato plant looks healthy! Keep up excellent growing practices.",
        "causes": "N/A — plant is healthy.",
        "symptoms": ["No disease symptoms detected."],
        "treatment": {
            "chemical": ["No treatment required."],
            "organic": ["Continue preventive organic practices."],
            "cultural": ["Maintain staking, pruning, and sanitation."],
        },
        "watering": (
            "1–2 inches of water per week. "
            "Water deeply and consistently at the base. "
            "Inconsistent watering causes blossom end rot."
        ),
        "sunlight": "8+ hours of full sun daily for best fruit production.",
        "fertilizer": (
            "Starter fertilizer at planting; calcium nitrate side-dress when fruits set; "
            "tomato-specific fertilizer (5-10-10) during fruiting stage."
        ),
        "prevention": [
            "Inspect plants weekly for early pest and disease signs.",
            "Stake or cage for support and air circulation.",
            "Mulch to retain moisture and prevent soil splash.",
            "Rotate crops every season.",
        ],
    },

    # ── Potato ─────────────────────────────────────────────────────────────────
    "Potato___Late_blight": {
        "display_name": "Potato Late Blight",
        "description": (
            "The same Phytophthora infestans pathogen that devastates tomatoes also "
            "causes potato late blight. Under epidemic conditions, an entire field "
            "can be destroyed in days."
        ),
        "causes": "Oomycete Phytophthora infestans; spreads rapidly in cool, wet, foggy weather.",
        "symptoms": [
            "Water-soaked, irregular dark lesions on leaves and stems.",
            "White cottony growth on undersides of leaves in humid conditions.",
            "Dark brown rot penetrating tubers from skin inward.",
            "Entire plant collapse in severe epidemics.",
        ],
        "treatment": {
            "chemical": [
                "Metalaxyl (Ridomil) + mancozeb combination applied every 7–10 days.",
                "Cymoxanil-based products for both protectant and curative activity.",
                "Fluopicolide (Presidio) systemic fungicide for resistant strains.",
            ],
            "organic": [
                "Copper sulfate or Bordeaux mixture every 5–7 days.",
                "Biofungicides containing Bacillus subtilis or Trichoderma spp.",
            ],
            "cultural": [
                "Destroy infected haulm before harvest to prevent tuber infection.",
                "Harvest in dry conditions; cure tubers properly.",
                "Do not store tubers showing any signs of blight.",
            ],
        },
        "watering": (
            "Avoid overhead irrigation. Use furrow or drip irrigation. "
            "Allow foliage to dry between watering events."
        ),
        "sunlight": "Full sun; avoid planting in frost pockets or poorly drained areas.",
        "fertilizer": (
            "Balanced NPK at planting. Adequate potassium improves disease resistance. "
            "Avoid excessive nitrogen."
        ),
        "prevention": [
            "Plant certified disease-free seed potatoes.",
            "Choose resistant varieties (Sarpo Mira, Sarpo Axona).",
            "Rotate crops — do not plant potatoes/tomatoes in the same plot within 3 years.",
            "Remove and destroy all volunteer potato plants and debris.",
        ],
    },

    "Potato___Early_blight": {
        "display_name": "Potato Early Blight",
        "description": (
            "Potato early blight is caused by Alternaria solani, affecting leaves "
            "primarily and reducing photosynthesis, leading to reduced tuber yield."
        ),
        "causes": "Fungal pathogen Alternaria solani; favored by warm days, cool nights, and wet foliage.",
        "symptoms": [
            "Dark brown concentric-ring (target) spots on lower, older leaves.",
            "Yellow chlorotic area surrounding lesions.",
            "Premature defoliation starting from bottom of plant.",
            "Surface lesions on tubers in severe cases.",
        ],
        "treatment": {
            "chemical": [
                "Chlorothalonil every 7–10 days starting at first symptom appearance.",
                "Azoxystrobin or trifloxystrobin fungicides.",
            ],
            "organic": [
                "Copper hydroxide spray every 7 days.",
                "Neem oil preventive spray.",
            ],
            "cultural": [
                "Remove infected foliage promptly.",
                "Mulch to prevent soil splash.",
                "Ensure adequate plant spacing.",
            ],
        },
        "watering": "Drip or furrow irrigation; avoid wetting foliage.",
        "sunlight": "Full sun with good air movement around plants.",
        "fertilizer": "Adequate nitrogen and potassium; balanced fertilization reduces stress.",
        "prevention": [
            "Use certified seed potatoes.",
            "Rotate crops annually.",
            "Apply preventive fungicide at first sign of disease.",
        ],
    },

    "Potato___healthy": {
        "display_name": "Healthy Potato",
        "description": "Your potato plant is healthy! Maintain good practices throughout the growing season.",
        "causes": "N/A — plant is healthy.",
        "symptoms": ["No disease symptoms detected."],
        "treatment": {
            "chemical": ["No treatment required."],
            "organic": ["Continue preventive organic practices."],
            "cultural": ["Hill soil around stems to protect developing tubers."],
        },
        "watering": (
            "1–2 inches per week consistently. "
            "Drip irrigation preferred; avoid wetting foliage. "
            "Reduce watering 2 weeks before harvest."
        ),
        "sunlight": "Full sun — 6–8 hours daily. Good drainage is essential.",
        "fertilizer": (
            "High phosphorus at planting (10-20-20). "
            "Side-dress nitrogen at hilling stage. "
            "Avoid excess nitrogen which promotes foliage over tuber growth."
        ),
        "prevention": [
            "Use certified disease-free seed potatoes.",
            "Hill plants when 6–8 inches tall to protect tubers from light and blight.",
            "Monitor for Colorado potato beetle weekly.",
            "Rotate with non-solanaceous crops.",
        ],
    },

    # ── Grape ──────────────────────────────────────────────────────────────────
    "Grape___Black_rot": {
        "display_name": "Grape Black Rot",
        "description": (
            "Grape black rot, caused by Guignardia bidwellii, destroys leaves, "
            "shoots, and fruit. Infected berries turn into hard, black, shriveled mummies."
        ),
        "causes": "Fungal pathogen Guignardia bidwellii; splashing rain spreads spores.",
        "symptoms": [
            "Small, tan leaf spots with dark borders.",
            "Reddish-brown lesions on shoots.",
            "Infected green berries shriveling into black, mummified fruit.",
        ],
        "treatment": {
            "chemical": [
                "Myclobutanil (Rally) from budbreak through 4–5 weeks after bloom.",
                "Mancozeb protective spray pre-bloom.",
            ],
            "organic": ["Copper-based sprays throughout the season."],
            "cultural": [
                "Remove all mummified fruit from vines and ground.",
                "Prune to improve air circulation.",
            ],
        },
        "watering": "Drip irrigation only; avoid wetting foliage and fruit.",
        "sunlight": "Full sun; orient rows for maximum air flow.",
        "fertilizer": "Balanced fertilization; excess nitrogen promotes susceptible tissue.",
        "prevention": [
            "Remove mummies before bud break.",
            "Apply fungicide at key growth stages.",
            "Train vines for open canopy.",
        ],
    },

    "Grape___healthy": {
        "display_name": "Healthy Grape",
        "description": "Your grapevine is healthy! Continue excellent vineyard management.",
        "causes": "N/A — plant is healthy.",
        "symptoms": ["No disease symptoms detected."],
        "treatment": {
            "chemical": ["No treatment required."],
            "organic": ["Continue preventive spray program."],
            "cultural": ["Annual dormant pruning to maintain vine structure."],
        },
        "watering": "Deep water weekly; established vines are drought-tolerant once established.",
        "sunlight": "Full sun — 7+ hours daily essential for fruit ripening.",
        "fertilizer": "Low-nitrogen fertilizer; excess nitrogen delays fruit ripening.",
        "prevention": [
            "Annual dormant pruning.",
            "Preventive fungicide program from budbreak.",
            "Monitor for powdery and downy mildew.",
        ],
    },

    # ── Corn ───────────────────────────────────────────────────────────────────
    "Corn_(maize)___healthy": {
        "display_name": "Healthy Corn",
        "description": "Your corn plant is healthy! Continue good agronomic practices.",
        "causes": "N/A — plant is healthy.",
        "symptoms": ["No disease symptoms detected."],
        "treatment": {
            "chemical": ["No treatment required."],
            "organic": ["Continue organic soil management."],
            "cultural": ["Ensure adequate plant spacing for air circulation."],
        },
        "watering": "1–1.5 inches per week; critical during silking and tasseling.",
        "sunlight": "Full sun — 8 hours minimum.",
        "fertilizer": (
            "Heavy nitrogen feeder: side-dress with nitrogen at knee-high stage. "
            "Starter fertilizer at planting."
        ),
        "prevention": [
            "Rotate with non-corn crops every year.",
            "Scout for corn earworm and rootworm.",
            "Use disease-resistant hybrids.",
        ],
    },

    "Corn_(maize)___Northern_Leaf_Blight": {
        "display_name": "Northern Corn Leaf Blight",
        "description": (
            "Northern corn leaf blight (NCLB), caused by Exserohilum turcicum, "
            "produces long, cigar-shaped lesions that can significantly reduce yield."
        ),
        "causes": "Fungal pathogen Exserohilum turcicum; spreads in cool, wet, humid conditions.",
        "symptoms": [
            "Long (1–6 inch), cigar/canoe-shaped tan to gray lesions on leaves.",
            "Lesions may have wavy, irregular margins.",
            "Grayish-green sporulation within lesions in humid weather.",
            "Premature plant senescence in severe cases.",
        ],
        "treatment": {
            "chemical": [
                "Azoxystrobin, propiconazole, or pyraclostrobin fungicides at VT/R1 stage.",
                "Triazole fungicides provide good control.",
            ],
            "organic": ["Copper-based sprays; limited effectiveness on corn."],
            "cultural": [
                "Rotate corn with non-host crops.",
                "Bury infected residue through tillage.",
            ],
        },
        "watering": "Consistent irrigation; avoid excessive moisture on foliage.",
        "sunlight": "Full sun with adequate plant spacing.",
        "fertilizer": "Adequate fertilization reduces plant stress and disease impact.",
        "prevention": [
            "Plant NCLB-resistant hybrids.",
            "Crop rotation.",
            "Fungicide application at tassel if conditions favor disease.",
        ],
    },

    # ── Pepper ─────────────────────────────────────────────────────────────────
    "Pepper,_bell___healthy": {
        "display_name": "Healthy Bell Pepper",
        "description": "Your bell pepper plant is healthy! Maintain consistent care for best yield.",
        "causes": "N/A — plant is healthy.",
        "symptoms": ["No disease symptoms detected."],
        "treatment": {
            "chemical": ["No treatment required."],
            "organic": ["Continue preventive organic practices."],
            "cultural": ["Stake plants when loaded with fruit."],
        },
        "watering": (
            "1–2 inches per week consistently. "
            "Inconsistent watering causes blossom end rot and fruit drop."
        ),
        "sunlight": "Full sun — 6–8 hours daily.",
        "fertilizer": "High phosphorus at planting; balanced NPK throughout season.",
        "prevention": [
            "Mulch to retain moisture and prevent soil splash.",
            "Inspect weekly for aphids and whiteflies.",
        ],
    },

    "Pepper,_bell___Bacterial_spot": {
        "display_name": "Pepper Bacterial Spot",
        "description": (
            "Bacterial spot on peppers is caused by Xanthomonas campestris pv. vesicatoria. "
            "It causes water-soaked lesions that turn brown with a yellow halo, "
            "affecting leaves and fruit."
        ),
        "causes": "Bacterial pathogen Xanthomonas; spreads via rain splash and infected seed.",
        "symptoms": [
            "Small, water-soaked spots becoming raised brown lesions.",
            "Yellow halo around lesions on leaves.",
            "Raised, wart-like spots on fruit.",
            "Severe defoliation under epidemic conditions.",
        ],
        "treatment": {
            "chemical": [
                "Copper hydroxide + mancozeb combination spray every 5–7 days.",
                "Bactericide applications starting at first symptom.",
            ],
            "organic": [
                "Copper-based sprays preventively.",
                "Avoid working in plants when wet.",
            ],
            "cultural": [
                "Remove and destroy infected plant material.",
                "Avoid overhead irrigation.",
            ],
        },
        "watering": "Drip irrigation at base; avoid wetting foliage.",
        "sunlight": "Full sun; good air circulation.",
        "fertilizer": "Balanced fertilization; excess nitrogen promotes susceptible tissue.",
        "prevention": [
            "Use certified disease-free transplants.",
            "Rotate crops annually.",
            "Disinfect tools between plants.",
        ],
    },
}

# ─── Generic Fallback ─────────────────────────────────────────────────────────
GENERIC_HEALTHY_ENTRY: Dict[str, Any] = {
    "display_name": "Healthy Plant",
    "description": "Your plant appears healthy! Maintain consistent care.",
    "causes": "N/A — plant is healthy.",
    "symptoms": ["No disease symptoms detected."],
    "treatment": {
        "chemical": ["No chemical treatment required."],
        "organic": ["Continue organic preventive practices."],
        "cultural": ["Maintain regular inspection and good cultural practices."],
    },
    "watering": "Water consistently based on species requirements; avoid overwatering.",
    "sunlight": "Provide species-appropriate light conditions.",
    "fertilizer": "Balanced fertilization based on plant species needs.",
    "prevention": [
        "Inspect plants weekly.",
        "Maintain good air circulation.",
        "Practice crop rotation.",
        "Remove dead or diseased plant material promptly.",
    ],
}

GENERIC_DISEASE_ENTRY: Dict[str, Any] = {
    "display_name": "Plant Disease Detected",
    "description": (
        "A plant disease has been detected. Consult your local agricultural "
        "extension office for species-specific treatment recommendations."
    ),
    "causes": "Fungal, bacterial, or viral pathogen — consult extension services.",
    "symptoms": ["Abnormal coloration, spots, wilting, or lesions on plant tissue."],
    "treatment": {
        "chemical": ["Consult local extension service for labeled fungicide/bactericide."],
        "organic": ["Copper-based sprays as a broad-spectrum preventive measure."],
        "cultural": [
            "Remove infected plant tissue.",
            "Improve air circulation.",
            "Avoid overhead watering.",
        ],
    },
    "watering": "Avoid wetting foliage; use drip irrigation at the base.",
    "sunlight": "Ensure adequate sunlight for plant recovery.",
    "fertilizer": "Maintain balanced nutrition; avoid excess nitrogen.",
    "prevention": [
        "Rotate crops regularly.",
        "Use certified disease-free planting material.",
        "Scout fields and gardens regularly.",
    ],
}


def _build_recommendations_list(entry: Dict[str, Any]) -> List[Dict[str, str]]:
    """Build a flat list of {category, text} recommendation dicts from an entry."""
    recs = []

    # Treatment
    for method, items in entry.get("treatment", {}).items():
        category = f"Treatment ({method.capitalize()})"
        for text in items:
            recs.append({"category": category, "text": text})

    # Care
    for field, cat in [
        ("watering", "Watering"),
        ("sunlight", "Sunlight"),
        ("fertilizer", "Fertilizer"),
    ]:
        val = entry.get(field, "")
        if val:
            recs.append({"category": cat, "text": val})

    # Prevention
    for text in entry.get("prevention", []):
        recs.append({"category": "Prevention", "text": text})

    return recs


def get_recommendation(
    label: str,
    confidence: float,
    health_score: int,
    severity: str,
) -> Dict[str, Any]:
    """
    Build the full recommendation JSON object for a given class label.

    Args:
        label: Predicted class label.
        confidence: Model confidence [0.0, 1.0].
        health_score: Computed health score 0–100.
        severity: LOW / MEDIUM / HIGH.

    Returns:
        Structured recommendation dict.
    """
    if label in KNOWLEDGE_BASE:
        entry = KNOWLEDGE_BASE[label]
    elif "healthy" in label.lower():
        logger.warning("Label '%s' not in knowledge base — using generic healthy entry.", label)
        entry = GENERIC_HEALTHY_ENTRY
    else:
        logger.warning("Label '%s' not in knowledge base — using generic disease entry.", label)
        entry = GENERIC_DISEASE_ENTRY

    recs = _build_recommendations_list(entry)

    return {
        "condition": label,
        "display_name": entry.get("display_name", label),
        "description": entry.get("description", ""),
        "causes": entry.get("causes", ""),
        "symptoms": entry.get("symptoms", []),
        "severity": severity,
        "health_score": health_score,
        "confidence": round(confidence, 4),
        "recommendations": recs,
    }


def list_all_labels() -> List[str]:
    """Return all labels present in the knowledge base."""
    return list(KNOWLEDGE_BASE.keys())

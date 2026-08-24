"""
core/species.py — Plant species knowledge base with basic botanical data.
"""

from typing import Dict, Any, List, Optional

SPECIES_DB: Dict[str, Dict[str, Any]] = {
    "Apple": {
        "scientific_name": "Malus domestica",
        "family": "Rosaceae",
        "type": "Fruit tree",
        "native_region": "Central Asia",
        "description": "Deciduous fruit tree cultivated worldwide.",
        "hardiness_zones": "3–8",
        "mature_height_ft": "10–30 (standard), 8–10 (dwarf)",
        "spacing_ft": "15–30 (standard), 6–10 (dwarf)",
        "bloom_time": "Spring (April–May)",
        "fruit_season": "Summer–Autumn (July–October depending on variety)",
        "soil_preference": "Well-drained loam, pH 6.0–7.0",
        "water_requirements": "Medium — 1 inch/week",
        "sun_requirements": "Full sun (6–8 hours)",
        "common_pests": ["Codling moth", "Apple maggot", "Aphids", "Scale insects"],
        "common_diseases": ["Apple scab", "Fire blight", "Powdery mildew", "Cedar apple rust"],
    },
    "Tomato": {
        "scientific_name": "Solanum lycopersicum",
        "family": "Solanaceae",
        "type": "Annual vegetable",
        "native_region": "South America (Andes region)",
        "description": "Warm-season annual vegetable; world's most popular garden vegetable.",
        "hardiness_zones": "Annual (grown 3–11)",
        "mature_height_ft": "3–6 (determinate), 6–10+ (indeterminate)",
        "spacing_ft": "2–3",
        "bloom_time": "Summer (June–September)",
        "fruit_season": "Summer–Autumn (July–October)",
        "soil_preference": "Rich, well-drained soil, pH 6.0–6.8",
        "water_requirements": "High — 1–2 inches/week consistently",
        "sun_requirements": "Full sun (8+ hours)",
        "common_pests": ["Tomato hornworm", "Whitefly", "Aphids", "Spider mites"],
        "common_diseases": ["Early blight", "Late blight", "Fusarium wilt", "Bacterial spot"],
    },
    "Potato": {
        "scientific_name": "Solanum tuberosum",
        "family": "Solanaceae",
        "type": "Root vegetable",
        "native_region": "South America (Peru/Bolivia)",
        "description": "Cool-season vegetable grown for its starchy tubers.",
        "hardiness_zones": "Annual — grows best in cool climates",
        "mature_height_ft": "2–3",
        "spacing_ft": "1–1.5 (in-row), 3 (between rows)",
        "bloom_time": "Summer",
        "fruit_season": "Late summer–autumn (70–120 days after planting)",
        "soil_preference": "Loose, well-drained loam, pH 4.8–5.5 (slightly acidic)",
        "water_requirements": "Medium — 1–2 inches/week",
        "sun_requirements": "Full sun (6+ hours)",
        "common_pests": ["Colorado potato beetle", "Aphids", "Wireworm", "Nematodes"],
        "common_diseases": ["Late blight", "Early blight", "Scab", "Blackleg"],
    },
    "Grape": {
        "scientific_name": "Vitis vinifera / Vitis labrusca",
        "family": "Vitaceae",
        "type": "Perennial vine",
        "native_region": "Mediterranean / Eastern North America",
        "description": "Perennial woody vine cultivated for fruit and wine production.",
        "hardiness_zones": "4–10 (varies by variety)",
        "mature_height_ft": "15–30 (vine length)",
        "spacing_ft": "8 (in-row), 10–12 (between rows)",
        "bloom_time": "Spring (May–June)",
        "fruit_season": "Late summer–autumn (August–October)",
        "soil_preference": "Well-drained, loamy, pH 5.5–6.5",
        "water_requirements": "Low–Medium once established; drip preferred",
        "sun_requirements": "Full sun (7+ hours)",
        "common_pests": ["Grape berry moth", "Japanese beetle", "Leafhoppers"],
        "common_diseases": ["Powdery mildew", "Downy mildew", "Black rot", "Botrytis"],
    },
    "Corn": {
        "scientific_name": "Zea mays",
        "family": "Poaceae",
        "type": "Annual grain crop",
        "native_region": "Mesoamerica (Mexico)",
        "description": "Major cereal crop; grown for grain, silage, and fresh consumption.",
        "hardiness_zones": "Annual — grown in zones 4–11",
        "mature_height_ft": "5–12",
        "spacing_ft": "0.5–1 (in-row), 2.5–3 (between rows)",
        "bloom_time": "Summer (tasseling 65–80 days after planting)",
        "fruit_season": "Mid-summer–autumn",
        "soil_preference": "Well-drained, fertile loam, pH 5.8–6.8",
        "water_requirements": "High — 1–1.5 inches/week; critical at silking",
        "sun_requirements": "Full sun (8+ hours)",
        "common_pests": ["Corn earworm", "European corn borer", "Rootworm"],
        "common_diseases": ["Northern leaf blight", "Southern rust", "Gray leaf spot"],
    },
}


def get_species_info(species_name: str) -> Optional[Dict[str, Any]]:
    """
    Retrieve species information by name.

    Args:
        species_name: Common plant name (e.g., "Apple", "Tomato").

    Returns:
        Species info dict or None if not found.
    """
    # Try exact match first
    if species_name in SPECIES_DB:
        return SPECIES_DB[species_name]

    # Case-insensitive search
    lower = species_name.lower()
    for key, val in SPECIES_DB.items():
        if key.lower() == lower:
            return val

    return None


def extract_species_from_label(label: str) -> Optional[str]:
    """
    Extract the plant species name from a class label.

    Class labels typically follow the pattern: "Species___Condition".

    Args:
        label: Class label string.

    Returns:
        Species string or None if not parseable.
    """
    if "___" in label:
        raw_species = label.split("___")[0]
        # Normalize: "Corn_(maize)" → "Corn", "Pepper,_bell" → "Pepper"
        species = raw_species.split("_(")[0].split(",")[0].strip()
        return species
    return None


def list_all_species() -> List[str]:
    """Return all species names in the knowledge base."""
    return list(SPECIES_DB.keys())

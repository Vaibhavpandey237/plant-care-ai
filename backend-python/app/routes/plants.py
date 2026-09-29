"""
app/routes/plants.py — Web route for plant species browser page.
"""

from flask import Blueprint, render_template
from core.species import SPECIES_DB
from core.care_recommender import KNOWLEDGE_BASE

plants_bp = Blueprint("plants", __name__)


@plants_bp.route("/plants", methods=["GET"])
def plants():
    """Render the plant species browser."""
    species_list = [
        {"name": name, **info}
        for name, info in SPECIES_DB.items()
    ]
    return render_template("plants.html", species_list=species_list,
                           kb_count=len(KNOWLEDGE_BASE))

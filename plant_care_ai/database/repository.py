"""
database/repository.py — CRUD operations for diagnoses.
"""

import json
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from database.db import get_connection
from utils.logger import get_logger

logger = get_logger(__name__)


def _row_to_dict(row) -> Dict[str, Any]:
    """Convert a sqlite3.Row to a plain dict, deserializing JSON fields."""
    d = dict(row)
    for key in ("all_predictions", "recommendations"):
        if isinstance(d.get(key), str):
            try:
                d[key] = json.loads(d[key])
            except (json.JSONDecodeError, TypeError):
                pass
    return d


def create_user(username: str, email: str, password_hash: str) -> Dict[str, Any]:
    """Create a new user record."""
    conn = get_connection()
    try:
        with conn:
            cursor = conn.execute(
                """
                INSERT INTO users (username, email, password_hash, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (username.strip(), email.strip().lower(), password_hash, datetime.now(timezone.utc).isoformat()),
            )
            user_id = cursor.lastrowid
        return get_user_by_id(user_id)
    finally:
        conn.close()


def get_user_by_email(email: str) -> Optional[Dict[str, Any]]:
    """Fetch user dict by email address."""
    conn = get_connection()
    try:
        row = conn.execute(
            "SELECT * FROM users WHERE email = ?", (email.strip().lower(),)
        ).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def get_user_by_username(username: str) -> Optional[Dict[str, Any]]:
    """Fetch user dict by username."""
    conn = get_connection()
    try:
        row = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username.strip(),)
        ).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def get_user_by_id(user_id: int) -> Optional[Dict[str, Any]]:
    """Fetch user dict by primary key."""
    conn = get_connection()
    try:
        row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def create_contact_message(name: str, email: str, subject: str, message: str) -> Dict[str, Any]:
    """Save a contact us message to the database."""
    conn = get_connection()
    try:
        with conn:
            cursor = conn.execute(
                """
                INSERT INTO contact_messages (name, email, subject, message, created_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (name.strip(), email.strip().lower(), subject.strip(), message.strip(), datetime.now(timezone.utc).isoformat()),
            )
            msg_id = cursor.lastrowid
        return {"id": msg_id, "name": name, "email": email, "subject": subject}
    finally:
        conn.close()


def create_diagnosis(
    image_name: str,
    image_path: str,
    top_prediction: str,
    top_confidence: float,
    all_predictions: List[Dict],
    health_score: int,
    severity: str,
    recommendations: Dict,
    user_id: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Insert a new diagnosis record and return the created row as a dict.
    """
    conn = get_connection()
    try:
        with conn:
            cursor = conn.execute(
                """
                INSERT INTO diagnoses
                    (user_id, image_name, image_path, top_prediction, top_confidence,
                     all_predictions, health_score, severity, recommendations, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    image_name,
                    image_path,
                    top_prediction,
                    top_confidence,
                    json.dumps(all_predictions, ensure_ascii=False),
                    health_score,
                    severity,
                    json.dumps(recommendations, ensure_ascii=False),
                    datetime.now(timezone.utc).isoformat(),
                ),
            )
            row_id = cursor.lastrowid
        return get_diagnosis_by_id(row_id)
    finally:
        conn.close()


def get_diagnosis_by_id(diagnosis_id: int) -> Optional[Dict[str, Any]]:
    """
    Fetch a single diagnosis by ID.

    Args:
        diagnosis_id: Primary key of the record.

    Returns:
        Dict or None if not found.
    """
    conn = get_connection()
    try:
        row = conn.execute(
            "SELECT * FROM diagnoses WHERE id = ?", (diagnosis_id,)
        ).fetchone()
        return _row_to_dict(row) if row else None
    finally:
        conn.close()


def list_diagnoses(
    page: int = 1, per_page: int = 20, user_id: Optional[int] = None
) -> Dict[str, Any]:
    """
    Return a paginated list of diagnoses ordered by newest first.
    Optionally scoped to user_id.
    """
    conn = get_connection()
    try:
        offset = (page - 1) * per_page
        if user_id is not None:
            total = conn.execute("SELECT COUNT(*) FROM diagnoses WHERE user_id = ?", (user_id,)).fetchone()[0]
            rows = conn.execute(
                "SELECT * FROM diagnoses WHERE user_id = ? ORDER BY created_at DESC LIMIT ? OFFSET ?",
                (user_id, per_page, offset),
            ).fetchall()
        else:
            total = conn.execute("SELECT COUNT(*) FROM diagnoses").fetchone()[0]
            rows = conn.execute(
                "SELECT * FROM diagnoses ORDER BY created_at DESC LIMIT ? OFFSET ?",
                (per_page, offset),
            ).fetchall()

        items = [_row_to_dict(r) for r in rows]
        pages = max(1, (total + per_page - 1) // per_page)
        return {
            "diagnoses": items,
            "items": items,
            "total": total,
            "page": page,
            "per_page": per_page,
            "pages": pages,
        }
    finally:
        conn.close()


def delete_diagnosis(diagnosis_id: int) -> bool:
    """
    Delete a diagnosis by ID.

    Args:
        diagnosis_id: Primary key of the record to delete.

    Returns:
        True if a row was deleted, False if not found.
    """
    conn = get_connection()
    try:
        with conn:
            cursor = conn.execute(
                "DELETE FROM diagnoses WHERE id = ?", (diagnosis_id,)
            )
        return cursor.rowcount > 0
    finally:
        conn.close()


def get_stats(user_id: Optional[int] = None) -> Dict[str, Any]:
    """
    Compute summary statistics for the dashboard.
    Optionally scoped to user_id.
    """
    conn = get_connection()
    try:
        where_clause = " WHERE user_id = ?" if user_id is not None else ""
        params = (user_id,) if user_id is not None else ()

        total = conn.execute(f"SELECT COUNT(*) FROM diagnoses{where_clause}", params).fetchone()[0]
        
        healthy_where = " WHERE top_prediction LIKE '%healthy%'"
        if user_id is not None:
            healthy_where += " AND user_id = ?"
        healthy_count = conn.execute(f"SELECT COUNT(*) FROM diagnoses{healthy_where}", params).fetchone()[0]
        
        diseased_count = total - healthy_count

        top_disease_where = " WHERE top_prediction NOT LIKE '%healthy%'"
        if user_id is not None:
            top_disease_where += " AND user_id = ?"
        top_disease_row = conn.execute(
            f"""
            SELECT top_prediction, COUNT(*) AS cnt
            FROM diagnoses
            {top_disease_where}
            GROUP BY top_prediction
            ORDER BY cnt DESC
            LIMIT 1
            """,
            params,
        ).fetchone()
        top_disease = top_disease_row["top_prediction"] if top_disease_row else "N/A"

        healthy_pct = round((healthy_count / total * 100), 1) if total > 0 else 0.0

        return {
            "total": total,
            "healthy_count": healthy_count,
            "diseased_count": diseased_count,
            "healthy_pct": healthy_pct,
            "top_disease": top_disease,
        }
    finally:
        conn.close()


def export_all_to_list() -> List[Dict[str, Any]]:
    """
    Return all diagnoses as a list of dicts for CSV export.

    Returns:
        List of all diagnosis dicts ordered by newest first.
    """
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT * FROM diagnoses ORDER BY created_at DESC"
        ).fetchall()
        return [_row_to_dict(r) for r in rows]
    finally:
        conn.close()

from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.get("/users")
def get_user(name: str):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    # Intentional SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE name='{name}'"
    cursor.execute(query)

    return {"data": cursor.fetchall()}
import sqlite3
import os

DB_PATH = "database/memes.db"

def init_db():

    os.makedirs(
        "database",
        exist_ok=True
    )

    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS meme_analysis(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        extracted_text TEXT,
        analysis TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def save_analysis(
    extracted_text,
    analysis
):

    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO meme_analysis
        (
            extracted_text,
            analysis
        )
        VALUES (?,?)
        """,
        (
            extracted_text,
            analysis
        )
    )

    conn.commit()
    conn.close()

def get_history():

    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM meme_analysis
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data
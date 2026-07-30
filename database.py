
import sqlite3
from datetime import date
DATABASE = "predictions.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            disease TEXT,
            confidence REAL,
            image TEXT,
            prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def save_prediction(disease, confidence, image):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO predictions
        (disease,confidence,image)

        VALUES(?,?,?)

    """,(disease,confidence,image))

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM predictions

        ORDER BY id DESC

    """)

    rows=cursor.fetchall()

    conn.close()

    return rows

def get_dashboard_stats():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Total Predictions
    cursor.execute("SELECT COUNT(*) FROM predictions")
    total = cursor.fetchone()[0]

    # Average Confidence
    cursor.execute("SELECT AVG(confidence) FROM predictions")
    avg = cursor.fetchone()[0]

    if avg is None:
        avg = 0

    avg = round(avg, 2)

    # Disease Types
    cursor.execute("SELECT COUNT(DISTINCT disease) FROM predictions")
    diseases = cursor.fetchone()[0]

    # Today's Predictions
    today = date.today().isoformat()

    cursor.execute("""
        SELECT COUNT(*)
        FROM predictions
        WHERE DATE(prediction_time)=?
    """, (today,))

    today_count = cursor.fetchone()[0]

    conn.close()

    return {
        "total": total,
        "average": avg,
        "diseases": diseases,
        "today": today_count
    }
def get_disease_distribution():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT disease,
               COUNT(*)
        FROM predictions
        GROUP BY disease
        ORDER BY COUNT(*) DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data
def delete_prediction(prediction_id):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM predictions WHERE id=?",
        (prediction_id,)
    )

    conn.commit()
    conn.close()
def get_prediction_trend():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DATE(prediction_time),
               COUNT(*)
        FROM predictions
        GROUP BY DATE(prediction_time)
        ORDER BY DATE(prediction_time)
    """)

    data = cursor.fetchall()

    conn.close()

    return data
def get_recent_predictions(limit=5):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM predictions
        ORDER BY id DESC
        LIMIT ?
    """,(limit,))

    data = cursor.fetchall()

    conn.close()

    return data
def get_most_common_disease():

    conn=sqlite3.connect(DATABASE)

    cursor=conn.cursor()

    cursor.execute("""

    SELECT disease,COUNT(*)

    FROM predictions

    GROUP BY disease

    ORDER BY COUNT(*) DESC

    LIMIT 1

    """)

    row=cursor.fetchone()

    conn.close()

    if row:

        return row

    return ("None",0)
def get_best_prediction():

    conn=sqlite3.connect(DATABASE)

    cursor=conn.cursor()

    cursor.execute("""

    SELECT disease,confidence

    FROM predictions

    ORDER BY confidence DESC

    LIMIT 1

    """)

    row=cursor.fetchone()

    conn.close()

    if row:

        return row

    return ("None",0)
from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# connection string k PostgreSQL (Render)
DB_URL = "postgresql://health_5cnc_user:AYpumENKLgHM2yw3gCFQiHNe4GnkbGLA@dpg-d4u4quili9vc7387ebs0-a.frankfurt-postgres.render.com/health_5cnc"

def get_connection():
    return psycopg2.connect(DB_URL, sslmode="require")

@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/weightform")
def weightform():
    return render_template("weightform.html")

@app.route("/showall")
def showall():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT kg FROM weight")
    rows = cursor.fetchall()
    conn.close()

    weights = [row[0] for row in rows]
    return render_template("showall.html", weights=weights)

@app.route("/store")
def store():
    weight = request.args.get("weight")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weight (kg) VALUES (%s)", (weight,))
    conn.commit()
    conn.close()

    return render_template("store.html", weight=weight)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

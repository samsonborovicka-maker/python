from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/weightform")
def weightform():
    return render_template("weightform.html")

@app.route("/showall")
def showall():
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "../health_py.db"))
    cursor = conn.cursor()

    # načtení všech hodnot z tabulky
    cursor.execute("SELECT kg FROM weight")
    rows = cursor.fetchall()
    conn.close()

    # rows je list tuple [(77,), (66,), ...]
    weights = [row[0] for row in rows]

    return render_template("showall.html", weights=weights)

@app.route("/store")
def store():
    # získání hodnoty z GET parametru
    weight = request.args.get("weight")

    # připojení k databázi (soubor health_py.db je o úroveň výš)
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "../health_py.db"))
    cursor = conn.cursor()

    # vložení hodnoty do tabulky
    cursor.execute("INSERT INTO weight (kg) VALUES (?)", (weight,))

    # potvrzení změn a zavření spojení
    conn.commit()
    conn.close()

    # předání hodnoty do šablony
    return render_template("store.html", weight=weight)
    
if __name__ == "__main__":
    app.run(debug=True)

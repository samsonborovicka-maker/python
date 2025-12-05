from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/weightform")
def weightform():
    return render_template("weightform.html")

@app.route("/showall")
def showall():
    weights = [111, 95, 102]  # zatím statické pole
    return render_template("showall.html", weights=weights)

@app.route("/store")
def store():
    weight = request.args.get("weight")
    return render_template("store.html", weight=weight)
    
if __name__ == "__main__":
    app.run(debug=True)

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
    return render_template("showall.html")

@app.route("/store")
def store():
    weight = request.args.get("weight")
    return render_template("store.html", weight=weight)
    
if __name__ == "__main__":
    app.run(debug=True)

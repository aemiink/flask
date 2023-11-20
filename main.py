from flask import Flask, render_template

app = Flask(__name__)

@app.route("/derse-katilan-ogrenciler")
def ogrenciler(sayi=5):
    return render_template("index.html",
                           sayi=sayi)

@app.route("/")
def home():
    return render_template("home.html")

app.run(debug=True)

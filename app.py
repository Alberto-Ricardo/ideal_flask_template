from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "12_diciembre_2022_ =)"

@app.route("/hola")
def index():
    flash("Cómo te llamas cuate?")
    return render_template("index.html")

@app.route("/greet", methods =["POST", "GET"])
def greet():
    flash("Hola " + str(request.form['name_input'])+ ", gusto en verte!")
    return render_template("index.html")


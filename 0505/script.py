from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/darbuotojai')
def darbuotojai():
    names = ["Adomas", "Petras", "Martynas", "Karolis"]
    return render_template("darbuotojai.html", workers_array=names)

@app.route('/darbuotojai/<vardas>')
def vardas(vardas):
    return "Vardas: " + vardas

@app.route('/prisijungimas', methods=['GET', 'POST'])
def prisijungimas():
    if request.method == 'POST':
        search = request.args.get('search') # URL parametras
        form_text_name = request.form.get("name") # FORMOS input vardas
        form_text_surname = request.form.get("surname")
        form_text_email = request.form.get("email2")
        return render_template("form_get.html", name=form_text_name, surname=form_text_surname, email=form_text_email, search=search)
    elif request.method == 'GET':
        return render_template("form_post.html")
    return None


def vardas(vardas):
    return "Vardas: " + vardas

@app.route('/darbuotojas/<int:id>')
def darbuotojas(id):
    return """
        <h1>Darbuotojas</h1>
        <div>Darbuotojo vidinis puslapis</div>
        <a href="/darbuotojai">Darbuotojai</a>
    """

app.run()
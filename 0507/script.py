import datetime

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Projektas(db.Model):
    __tablename__ = 'projektas'
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String)
    kaina = db.Column(db.Float)
    sukurimo_data = db.Column(db.DateTime, default=datetime.datetime.now)

    @property
    def kainaSuPVM(self):
        return round(self.kaina * 1.21)

with app.app_context():
    db.create_all()
    p1 = Projektas(id = 1, pavadinimas = "fasttrack", kaina=5000.333)
    p2 = Projektas(id=2, pavadinimas="fasttrack2", kaina=2000.333)
    p3 = Projektas(id=3, pavadinimas="fasttrack3", kaina=3000.333)
    p4 = Projektas(id=4, pavadinimas="fasttrack4", kaina=4000.333)
    db.session.add_all([p1, p2, p3, p4])
    db.session.commit()

@app.route('/')
def home():
    all_projektas = Projektas.query.all()
    return render_template("index.html", all_projektas=all_projektas)

@app.route('/projektas')
def search_projektas():
    search = request.args.get('search')
    if search:
        rows = Projektas.query.filter(Projektas.pavadinimas.ilike(search + "%"))
        # print(rows)
        return render_template("index.html", all_projektas=rows)
    else:
        all_projektas = Projektas.query.all()
        return render_template("index.html", all_projektas=all_projektas)

@app.route('/prideti-projekta', methods=["GET", "POST"])
def prideti_projekta():
    if request.method == 'POST':
        pavadinimas = request.form.get('pavadinimas')
        kaina = float(request.form.get('kaina'))
        naujas_projektas = Projektas(pavadinimas=pavadinimas, kaina=kaina)
        db.session.add(naujas_projektas)
        db.session.commit()
        return redirect(url_for("home"))
    if request.method == 'GET':
        return render_template("form.html")
    return render_template("index.html")

@app.route("/projektas/<int:id>")
def delete_projektas(id):
    projektas = Projektas.query.get(id)
    if projektas:
        db.session.delete(projektas)
        db.session.commit()
    return redirect(url_for("home"))

@app.route('/api/projektas')
def api_search_projektas():
    search = request.args.get('search')
    if search:
        rows = Projektas.query.filter(Projektas.pavadinimas.ilike(search + "%")).all()
    else:
        rows = Projektas.query.all()

    result = [
        {
            "id": projektas.id,
            "pavadinimas": projektas.pavadinimas,
            "kaina": projektas.kaina,
            "kainaSuPVM": projektas.kainaSuPVM
        }
        for projektas in rows
    ]
    return jsonify(result)

if __name__ == '__main__':
    app.run()
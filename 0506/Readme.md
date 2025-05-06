
# Flask ir SQLAlchemy – Duomenų bazės valdymas

Šiame projekte nagrinėjame, kaip kurti duomenų bazę naudojant Flask su SQLAlchemy ORM. Išmokstame pagrindinių duomenų valdymo veiksmų (CRUD) ir papildomo funkcionalumo: paieškos, apskaičiuojamų laukų bei grafinio atvaizdavimo su CSS.

---

## 1. Įvadas

**Pagrindinės sąvokos:**

- **ORM (Object-Relational Mapping):** leidžia dirbti su duomenų baze naudojant Python klases.
- **SQLAlchemy:** populiari ORM biblioteka Python kalboje.
- **CRUD (Create, Read, Update, Delete):** pagrindiniai duomenų valdymo veiksmai.

---

## 2. Flask aplikacijos su SQLAlchemy

### `db_app01.py` – Bazinė duomenų bazės struktūra ir atvaizdavimas

- Sukuria SQLite duomenų bazę `projektai.db`.
- Apibrėžia `Projektas` modelį su laukais:
  - `pavadinimas`
  - `kaina`
  - `sukurimo_data`
- Užkrauna visus projektus ir atvaizduoja juos per HTML šabloną.

```python
class Projektas(db.Model):
    __tablename__ = "projektas"
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String)
    kaina = db.Column(db.Float)
    sukurimo_data = db.Column(db.DateTime, default=datetime.datetime.now)
````

---

### `db_app02_filtravimas.py` – Paieška pagal pavadinimą

* Galima filtruoti projektus pagal `pavadinimą` naudojant `LIKE` SQL užklausą.

```python
search_text = request.args.get("searchlaukelis")
Projektas.query.filter(Projektas.pavadinimas.ilike(search_text + "%"))
```

---

### `db_app03_apskaiciuojamas_laukas.py` – Automatinis PVM apskaičiavimas

* Naudojant `@property`, apskaičiuojamas papildomas laukas `kaina_su_pvm` (21% PVM):

```python
@property
def kaina_su_pvm(self):
    return round(self.kaina * 1.21)
```

---

### `db_app04_visi_CRUD_veiksmai.py` – Pilnas CRUD funkcionalumas

**Pridėti projektą:**

```python
@app.route("/prideti-projekta", methods=["GET", "POST"])
def new_project():
    if request.method == "POST":
        pavadinimas = request.form.get("laukelispavadinimas")
        kaina = float(request.form.get("laukeliskaina"))
        new_project_row = Projektas(pavadinimas, kaina)
        db.session.add(new_project_row)
        db.session.commit()
    return redirect(url_for("home"))
```

**Ištrinti projektą:**

```python
@app.route("/trinti-projekta/<int:project_id>", methods=["POST"])
def delete_project(project_id):
    one_project_row = Projektas.query.get(project_id)
    if one_project_row:
        db.session.delete(one_project_row)
        db.session.commit()
    return redirect(url_for("home"))
```

---

### `db_app5_su_css.py` – Grafinis dizainas su CSS

* Naudojamas HTML šablonas `index_css.html`, kuris leidžia stilingai atvaizduoti projektų sąrašą.

```python
return render_template("index_css.html", projektas_rows=all_rows)
```

---

## 3. Išvados

* **SQLAlchemy** leidžia patogiai valdyti duomenų bazes Flask aplikacijose.
* Įgyvendintos pagrindinės **CRUD** operacijos.
* Pridėta:

  * Paieška pagal pavadinimą
  * Apskaičiuojamas PVM laukas
  * Grafinis sąsajos dizainas naudojant CSS

---

## Paleidimas

1. Įdiek priklausomybes:

   ```bash
   pip install flask flask_sqlalchemy
   ```

2. Paleisk programą:

   ```bash
   python db_app01.py  # arba kita versija, pvz. db_app04_visi_CRUD_veiksmai.py
   ```

3. Atidaryk naršyklėje:

   ```
   http://127.0.0.1:5000
   ```

---


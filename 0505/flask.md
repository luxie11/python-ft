# Flask pagrindai – maršrutai, šablonai ir formos

## 1. Įvadas į Flask

**Flask** yra lengvas Python žiniatinklio programavimo karkasas, kuris leidžia greitai kurti internetines aplikacijas.

### Pagrindinės Flask savybės:
- Paprastas ir lengvai išmokstamas
- Minimalistinė struktūra
- Palaiko Jinja2 šablonų sistemą
- Integracija su HTML formomis

---

## 2. Flask aplikacijų kodas

### f01_hello_world.py

Šiame faile sukuriama paprasčiausia Flask aplikacija su keliais maršrutais.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World from my first Flask webApp!!!\nHOMEPAGE"

@app.route("/news")
def news():
    return "Čia pagrindinis naujienų puslapis"

@app.route("/news/<int:item>")
def news_item(item):
    return f"Čia naujiena NR {item}"

@app.route("/<text>")
def any_route(text):
    return f"Jūs surinkote maršrutą {text} Jokio resurso čia nėra"

if __name__ == "__main__":
    app.run()
````

**Paaiškinimas:**

* `@app.route("/")` – nustato pagrindinį maršrutą (homepage).
* `@app.route("/news")` – apibrėžia naujienų puslapį.
* `@app.route("/news/<int:item>")` – leidžia per URL perduoti naujienos numerį.
* `@app.route("/<text>")` – leidžia įvesti bet kokį tekstą ir grąžinti jį atgal.

---

### f02\_html.py

Šis failas demonstruoja, kaip Flask gali grąžinti HTML turinį tiesiogiai iš Python funkcijų.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Homepage</h1>
    <p>Hello World!!!</p>
    <p><a href='/verslas'>pereiti į verslo skyrių</a></p>
    """
```

**Paaiškinimas:**

* HTML kodas grąžinamas kaip teksto eilutė su `return`.
* `<a href='/verslas'>` – nuoroda į kitą puslapį.

---

### f03\_sablonai.py

Šiame faile naudojami Flask šablonai su `render_template` funkcija.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/vardusarasas")
def names_list():
    names = ["Adomas", "Antanas", "Valdas", "Jonas"]
    return render_template("vardai.html", names_for_template=names)
```

**Paaiškinimas:**

* `render_template("index.html")` – nurodo naudoti HTML šabloną.
* `names_for_template` – perduoda Python sąrašą į HTML šabloną.

---

### f04\_formos.py

Šis failas demonstruoja GET ir POST formų apdorojimą Flask'e.

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    search_text = request.args.get('paieskoslaukelis')
    return render_template("forma_get.html")

@app.route("/login", methods=['post', 'get'])
def login_user():
    if request.method == "GET":
        return render_template("forma_post.html")
    elif request.method == "POST":
        form_text = request.form.get("loginlaukelis")
        return render_template("login_result.html", user_login=form_text)
```

**Paaiškinimas:**

* `request.args.get('paieskoslaukelis')` – gauna GET parametro reikšmę.
* `request.form.get("loginlaukelis")` – gauna POST formos reikšmę.

---

## 3. HTML failai naudojami Flask aplikacijose

### `index.html`

```html
<h1>Sveiki, čia mano naujas puslapis</h1>
<p>Puslapis suprogramuotas naudojant Python Flask framework'ą</p>
```

### `vardai.html`

```html
<h4>Vardai gauti iš Python faile parašyto listo:</h4>
{% for elem in names_for_template %}
<p>{{ elem }}</p>
{% endfor %}
```

### `forma_get.html`

```html
<form action="" method="get">
    <input type="text" name="paieskoslaukelis">
    <input type="submit" value="siųsti paieškos stringą">
</form>
```

### `forma_post.html`

```html
<form action="" method="post">
    <input type="text" name="loginlaukelis">
    <input type="submit" value="prisijungti">
</form>
```

**Paaiškinimas:**

* `method="get"` – duomenys perduodami per URL.
* `method="post"` – duomenys siunčiami nematomai.

---

## Išvados

* Flask suteikia paprastą ir lanksčią platformą žiniatinklio aplikacijoms kurti su Python.
* Galimybė naudoti tiek šablonus, tiek formų apdorojimą leidžia greitai kurti dinamiškas aplikacijas.
* Flask maršrutai ir šablonų sistema yra paprasti ir lengvai išmokstami, tačiau galingi kurti sudėtingesnes aplikacijas.

---




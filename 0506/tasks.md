
###  **Klientas**

```python
class Klientas(db.Model):
    __tablename__ = 'klientas'
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String(100), nullable=False)
    el_pastas = db.Column(db.String(120), unique=True, nullable=False)
    registracijos_data = db.Column(db.DateTime, default=datetime.datetime.now)

    @property
    def vartotojo_kodas(self):
        return f"KLT{self.id:04}"
```

---

### Paaiškinimas:

* `id`: Unikalus kiekvieno kliento ID.
* `vardas`: Kliento vardas (būtinas laukelis).
* `el_pastas`: Kliento el. paštas, turi būti unikalus.
* `registracijos_data`: Automatiškai nustatoma registracijos data.
* `vartotojo_kodas`: Sugeneruojamas kodas, pvz. `KLT0005` – patogu rodyti naudotojui.

---

### **Užduotis 1: Klientų sąrašo atvaizdavimas**

**Tikslas:** Sukurti `/` maršrutą, kuris rodo visus klientus.

**Veiksmai:**

* Sukurk `Klientas` modelį su laukais: `vardas`, `el_pastas`, `registracijos_data`.
* Naudok `Klientas.query.all()` ir atvaizduok `index.html`.

---

### **Užduotis 2: Naujo kliento pridėjimas**

**Tikslas:** Sukurti formą naujam klientui pridėti.

**Veiksmai:**

* Sukurk `/prideti-klienta` maršrutą su `GET` ir `POST`.
* Forma: `vardas`, `el_pastas`.
* `POST` metodu išsaugok įrašą į duomenų bazę.

---

### **Užduotis 3: Kliento paieška pagal vardą**

**Tikslas:** Leisti vartotojui ieškoti klientų pagal vardą.

**Veiksmai:**

* Naudok `request.args.get("search")`.
* Filtruok: `Klientas.query.filter(Klientas.vardas.ilike(search + "%"))`.

---

### **Užduotis 4: Kliento ištrynimas pagal ID**

**Tikslas:** Leisti ištrinti klientą paspaudus mygtuką „Trinti“.

**Veiksmai:**

* Sukurk `/trinti-klienta/<int:id>` maršrutą.
* Ištrink klientą pagal ID.
* Nukreipk atgal į sąrašą.

---

### **Užduotis 5: Kliento kodo rodymas šablone**

**Tikslas:** Kiekvienam klientui rodyti jo automatinį kodą, pvz. `KLT0003`.

**Veiksmai:**

* Modelyje naudok `@property` metodą `vartotojo_kodas`.
* Atvaizduok šį kodą HTML šablone.

---


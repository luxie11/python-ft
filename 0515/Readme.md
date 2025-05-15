# Užduotis: Knygų valdymo aplikacija su Django (su formomis ir views)

---

### Tikslas

Sukurti Django aplikaciją, leidžiančią valdyti knygų sąrašą: pridėti, peržiūrėti, redaguoti ir ištrinti knygas, naudojant tradicines Django formas, views ir templates.

---

### Užduoties aprašymas

1. **Modelis**

Sukurk modelį `Book` su laukais:

* `title` (CharField, max 200)
* `author` (CharField, max 100)
* `year` (IntegerField)

2. **Formos**

Sukurk `forms.py` faile `BookForm` paveldėtą iš `forms.ModelForm`, susietą su `Book` modeliu, naudojant visus laukus.

3. **Views**

Sukurk šias view funkcijas (ar klasines views):

* **Knygų sąrašas** (GET `/books/`) — rodo visas knygas lentelėje.
* **Knygos pridėjimas** (GET/POST `/books/add/`) — rodo tuščią formą pridėjimui, apdoroja formos duomenis ir išsaugo naują įrašą.
* **Knygos redagavimas** (GET/POST `/books/<int:id>/edit/`) — rodo užpildytą formą redagavimui, apdoroja pakeitimus ir išsaugo.
* **Knygos ištrynimas** (POST `/books/<int:id>/delete/`) — ištrina nurodytą knygą, peradresuoja į knygų sąrašą.

4. **Šablonai**

Sukurk HTML šablonus:

* `books_list.html` — rodo knygų sąrašą su nuorodomis redaguoti ir ištrinti.
* `book_form.html` — rodo formą su CSRF žymeniu ir pateikimo mygtuku.

Jeigu reikia papildomu HTML formų ir randate, kur jas panaudoti, galite sukurti šias formas.

5. **URL konfiguracija**

Užregistruok maršrutus `/books/`, `/books/add/`, `/books/<id>/edit/`, `/books/<id>/delete/` atitinkamoms view funkcijoms.

---

### Testavimas

* Atidaryk knygų sąrašo puslapį, patikrink ar matomi visi įrašai.
* Išbandyk pridėti naują knygą, patikrink įrašą duomenų bazėje.
* Išbandyk redaguoti egzistuojančią knygą, patikrink pakeitimus.
* Išbandyk ištrinti knygą, patikrink ar įrašas pašalintas.

---

**Šiuos klausimus reikia ataskyti į Readme.md failą savo projekte.**
### Klausimai savikontrolei

* Kaip Django apdoroja POST užklausas formoms?
* Kodėl būtinas `{% csrf_token %}`?
* Kaip atvaizduoti formos klaidas?
* Kuo skiriasi GET ir POST užklausų apdorojimas view funkcijoje?

---

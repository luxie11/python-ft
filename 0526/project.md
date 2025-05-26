# Django Receptų Projektas 

---

## 1. Autentifikacija

* **Prisijungimas ir registracija:**
  Vartotojai turi susikurti paskyrą ir prisijungti, kad galėtų naudotis programos funkcijomis.

* **Prieigos kontrolė:**
  Tik prisijungę vartotojai gali kurti, redaguoti ir trinti receptus.

* **Vieša prieiga:**
  Neprisijungę vartotojai gali tik peržiūrėti receptų sąrašą ir receptų detales, tačiau negali keisti duomenų.

---

## 2. Vartotojo ryšys su receptais

* Kiekvienas receptas bus susietas su vartotoju, kuris jį sukūrė (pvz., per lauką `created_by`).
* Vartotojas galės redaguoti ir trinti tik savo sukurtus receptus.
* Kiti vartotojai matys visus receptus, bet negalės jų keisti.

---

## 3. Modelių papildymas

* `Recipe` modelyje pridedamas laukas, rodantis recepto savininką (ForeignKey į vartotoją).
* Autentifikacijos valdymas atliekamas naudojant Django standartinę autentifikacijos sistemą (naudotojų registracija, prisijungimas, atsijungimas).

---

## 4. URL maršrutai ir prieigos teisės

| URL                     | Veiksmas                        | Prieiga                |
| ----------------------- | ------------------------------- | ---------------------- |
| `/recipes/`             | Receptų sąrašas                 | Visuomenei             |
| `/recipes/<id>/`        | Recepto detalės                 | Visuomenei             |
| `/recipes/add/`         | Naujo recepto kūrimo forma      | Tik prisijungusiems    |
| `/recipes/<id>/edit/`   | Recepto redagavimo forma        | Tik recepto savininkui |
| `/recipes/<id>/delete/` | Recepto ištrynimo patvirtinimas | Tik recepto savininkui |
| `/accounts/login/`      | Prisijungimo puslapis           | Visuomenei             |
| `/accounts/logout/`     | Atsijungimo veiksmas            | Tik prisijungusiems    |
| `/accounts/signup/`     | Registracijos puslapis          | Visuomenei             |

---

## 5. Funkcionalumo aprašymas su autentifikacija

* **Prisijungę vartotojai** gali pridėti naujus receptus, redaguoti ir trinti tik savo sukurtus receptus.
* **Neprisijungę vartotojai** gali tik peržiūrėti receptų sąrašą ir recepto detales.
* Vartotojo informacija saugoma Django naudotojų modelyje (standartinis `User`).
* Prisijungimas ir registracija gali būti įgyvendinta naudojant Django standartines `django.contrib.auth` priemones ar papildomą paketą, pvz., `django-allauth`.

---

## 6. Vartotojo sąsaja

* Prisijungimo, registracijos, ir atsijungimo nuorodos matomos puslapio viršuje arba meniu.
* Kuriant ar redaguojant receptą, forma rodo vartotojui galimybę įvesti duomenis tik jei jis prisijungęs.
* Jei neprisijungęs, bandymas patekti į recepto kūrimo/redagavimo puslapį nukreipiamas į prisijungimo puslapį.

---

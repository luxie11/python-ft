

###  **1 užduotis: Kainų analizatorius**
**Temos**: sąrašai, ciklai, sąlygos, funkcijos, `input`, `try-except`

**Užduotis**:  
Parašykite programą, kuri:
- Paprašo vartotojo įvesti prekių kainas, atskirtas kableliais (pvz., `12.5, 7.99, 3, 20`).
- Konvertuoja jas į sąrašą `float` tipo reikšmių.
- Apskaičiuoja:
  - Vidutinę kainą
  - Brangiausią prekę
  - Pigiausią prekę
- Jeigu vartotojas įveda netinkamus duomenis, parodyk klaidos pranešimą naudojant `try-except`.

---

###  **2 užduotis: Slaptažodžio stiprumo tikrinimas**  
**Temos**: sąlygos, `input`, funkcijos, `len`, `any`, `string` modulis

**Užduotis**:  
Parašyk funkciją, kuri įvertina slaptažodžio stiprumą pagal šiuos kriterijus:
- Ilgesnis nei 8 simboliai
- Turi bent vieną didžiąją raidę
- Turi bent vieną skaičių
- Turi bent vieną specialų simbolį (pvz., `!@#$%^&*()`)

Išveskite rezultatą:
```plaintext
Jūsų slaptažodis yra: silpnas / vidutinis / stiprus
```

---

###  **3 užduotis: Mini viktorina**  
**Temos**: sąrašai, žodynai, `input`, ciklai, sąlygos

**Užduotis**:  
Sukurk viktoriną su 3 klausimais (naudok žodynų sąrašą):
```python
klausimai = [
    {"klausimas": "Kokia yra sostinė Lietuvos?", "atsakymas": "Vilnius"},
    {"klausimas": "Kiek yra 5 + 7?", "atsakymas": "12"},
    ...
]
```

Kiekvienam klausimui:
- Užduok klausimą
- Patikrink vartotojo atsakymą
- Skaičiuok taškus

Pabaigoje parodyk rezultatą:
```plaintext
Teisingi atsakymai: 2 iš 3
```

---

###  **4 užduotis: Loterijos simuliatorius**  
**Temos**: random modulis, sąrašai, funkcijos

**Užduotis**:
- Vartotojas pasirenka 6 skaičius nuo 1 iki 30
- Naudojant `random.sample()`, sugeneruok 6 atsitiktinius „laimėjimo“ skaičius
- Palygink ir parodyk kiek skaičių sutapo

Pavyzdys:
```plaintext
Jūs pataikėte 3 iš 6 skaičių! Sėkmės kitą kartą!
```

### **5 užduotis: Klasė `Biblioteka`**

Sukurk klasę `Biblioteka`, kuri turi:
- atributą `knygos` – tai `Knyga` objektų sąrašas

Metodai:
- `prideti_knyga(knyga: Knyga)`
- `rodyti_knygas()`
- `paimti_knyga(pavadinimas: str)`
- `grazinti_knyga(pavadinimas: str)`
- `__str()__`
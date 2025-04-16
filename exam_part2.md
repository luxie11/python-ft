### 1. **Prisijunkite prie [GitHub](https://github.com)**

---

###  2. **Sukurkite naują repozitoriją**

1. Viršutiniame dešiniajame kampe spausk **"+" > "New repository"**
2. Užpildyk laukus:
   - **Repository name** – students-registry
   - **Description** (nebūtina)
3. Pasirinkite:
   -  **"Private"** 
4. Spauskite **"Create repository"**

---

### 3. **Privačios repositorijos klonavimas  **

Terminale:

```bash
git clone https://github.com/tavo-vartotojas/tavo-repozitorija.git
```

Kai paleisite šią komandą:

- Jei nenaudojate SSH ratko, GitHub paprašys tavo **prisijungimo duomenų** (vartotojo vardo ir asmeninio prieigos rakto – Personal Access Token).
- Arba galite naudoti SSH:

```bash
git clone git@github.com:tavo-vartotojas/tavo-repozitorija.git
```

> Reikia būti **sukūrus SSH raktą** ir įkėlus jį į GitHub paskyrą.
Rakto sukurimas pateikiamas žemiau:
```bash
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub
```
Gautas rezultatas yra pridedamas į Github. Nustatymuose spaudžiame SSH Keys ir jį pridedame.

---

Po klonavimo:

```bash
cd tavo-repozitorija
git checkout -b exam
```

Ir galite pradėti dirbti su failais, daryti commit'us ir push'inti.

Visiems rekomenduoju šiuos žingnsius pirmiausiai atlikti ir tik tada keliauti prie užduoties

---

### **Antroji Užduotis: Studentų Registracijos Sistema**

**Tikslas:**  
Sukurti paprastą sistemą, leidžiančią registruoti studentus, peržiūrėti jų informaciją, atnaujinti duomenis ir pašalinti studentus.

---

###  **Reikalavimai:**

#### ŽINGSNIS 1: Sukurkite klasę `Student`
- **Laukai:**
  - `name` (vardas)
  - `student_id` (studento ID)
  - `enrollment_year` (stojimo metai)
  - `active` (ar studentas aktyvus) – pagal nutylėjimą `True`

- **Metodai:**
  - `__str__()` – gražina informaciją apie studentą gražiu formatu.
  - `is_graduated()` – grąžina `True`, jei studentas mokosi ilgiau nei 4 metus (naudojant `datetime`).

---

#### ŽINGSNIS 2: Sukurkite klasę `StudentRegistry`
- **Laukai:**
  - `students` – sąrašas, kuriame saugomi visi studentai.

- **Metodai:**
  - `add_student(student)` – prideda naują `Student` objektą į registrą.
  - `display_students()` – atvaizduoja visus studentus.
  - `find_student(student_id)` – suranda studentą pagal ID.
  - `deactivate_student(student_id)` – pažymi studentą kaip neaktyvų.
  - `remove_student(student_id)` – pašalina studentą iš registro.

---

#### ŽINGSNIS 3: Naudokite `datetime` studijų metų valdymui
- Naudokite `datetime.datetime.now().year`, kad patikrintumėte, kiek metų studentas jau mokosi.

---

#### ŽINGSNIS 4: Sukurkite vartotojų sąsają terminale
- Naudokite `while` ciklą, kad vartotojas galėtų:
  - Pridėti naują studentą.
  - Peržiūrėti visus studentus.
  - Pažymėti studentą, kuris baigė studijas.
  - Pašalinti studentą.
  - Išeiti iš programos.

---

####  Papildomos sąlygos:
- Naudokite `try-except` klaidoms suvaldyti (pvz., jei įvedami blogi metai ar studento ID nerastas).
- Naudokite aiškius pranešimus vartotojui.

---
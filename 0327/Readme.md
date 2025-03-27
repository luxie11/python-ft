# Projekto užduočių valdymas

## 1. Jira nustatymai

### 1.1 Paskyros ir projekto sukūrimas
1. **Prisiregistruokite** prie [Jira](https://www.atlassian.com/software/jira) arba prisijunkite prie esamos paskyros.
2. **Sukurkite naują projektą**:
   - Pasirinkite projekto tipą (Scrum ar Kanban).
   - Nurodykite projekto pavadinimą.
3. **Pakvieskite komandos narius**:
   - Eikite į projekto nustatymus ir pridėkite komandos narius naudodami jų el. pašto adresus.

### 1.2 Sprinto ir užduočių sukūrimas
4. **Sukurkite naują "sprintą"**:
   - Sprinto trukmė: **2 savaitės**.
   - Sprinto lentoje paspauskite „Create Sprint“.
5. **Sukurkite užduotis**:
   - Remdamiesi funkciniais reikalavimais, sukurti užduotis "backlog" dalyje. Rekomenduojama daryti kuo smulkiai, kad matytusi progresas
   - Pasirinkite atsakingą asmenį.
6. **Perkelkite užduotis į "sprintą"**:
   - „Backlog“ lentoje vilkite užduotis į naujai sukurtą sprintą.

---

## 2. Git darbo eiga

### 2.1 Repozitorijos klonavimas
1. **Jei jau yra sukurta repozitorija, ją reikia atsisiųsti į savo kompiuterį**:
   ```sh
   git clone <repo-url>
   cd project-name
   ```

### 2.2 Branch kūrimas
2. **Pasirinkite užduotį iš Jira, kurią Jūs atliksite**:
   - Kiekviena užduotis turi unikalų numerį (pvz., `TASK-1`).
3. **Sukurkite naują „feature“ šaką**:
   ```sh
   git checkout -b feature/TASK-1
   ```

### 2.3 Kodavimo darbai
4. **Pradėkite programavimo darbus**
   - Užtikrinkite, kad visi pakeitimai atitinka gerąsias praktikas, kurias išmokote paskaitų metu
5. **Commit ir push į git repozitoriją**:
   ```sh
   git add .
   git commit -m "TASK-1: Trumpas commit'o aprašymas"
   git push origin feature/TASK-1
   ```

### 2.4 Pull Request kūrimas
6. **Atidarykite PR (Pull Request) (Github puslapyje)**:
   - PR nukreipkite į `master` arba `main` šaką.
   - Aprašykite pakeitimus ir pridėkite nuorodą į Jira užduotį.
7. **Code review ir merge**:
   - Komandos nariai peržiūri kodą (atsiunčiate dėstytojui).
   - Jei viskas gerai – PR sujungiamas su pagrindiniu branchu.

---

## 3. Front-End darbo pradžia

### 3.1 Projekto paruošimas
1. **Vienas žmogus turi sukurti Front-End projektą**. Galima rinktis iš dviejų variantų:
   - **React:**
     ```sh
     npx create-react-app project-name
     cd project-name
     ```
   - **HTML + CSS + JavaScript:**
     ```sh
     mkdir project-name
     cd project-name
     touch index.html styles.css script.js
     ```
2. **Išvalyti nereikalingus failus**:
   - Jei naudojate React, pašalinkite nereikalingus failus (`App.css`, `App.test.js`, `logo.svg` ir pan.).
   - Jei naudojate paprastą JS + HTML + CSS, užtikrinkite, kad `index.html` turi bazinę struktūrą.
3. **Sukurti bazinę struktūrą** pagal projekto poreikius.

### 3.2 Repozitorijos paruošimas
4. **Jei repozitorija jau sukurta, prisijunkite prie jos**:
   ```sh
   git remote add origin <repo-url>
   ```
5. **Push į nuotolinę repozitoriją**:
   ```sh
   git push -u origin main
   ```
6. **Pasidalinti repozitorijos nuoroda su komanda**.

---

## 4. Pastabos
- Laikykitės vieningo branch pavadinimo formato (`feature/TASK-XX`).
- Venkite didelių PR – geriau dažnesni ir mažesni pakeitimai.
- Užduotis stenkitės skaidyti kuo smulkesniais etapais, kad būtų galima stebėti Jūsų progresą.

# Sėkmės


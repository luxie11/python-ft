
### 1. **Prisijunk prie [GitHub](https://github.com)**

---

###  2. **Sukurk naują repozitoriją**

1. Viršutiniame dešiniajame kampe spausk **"+" > "New repository"**
2. Užpildyk laukus:
   - **Repository name** – python-exam-20250415
   - **Description** (nebūtina)
3. Pasirink:
   -  **"Private"** 
4. Spausk **"Create repository"**

---
Aha, jeigu nori **nusiklonuoti** _privatų_ repozitorijų į savo kompiuterį – vietoj 3 žingsnio naudok:

---

### 3. **Klonavimas privačios repositorijos**

Terminale:

```bash
git clone https://github.com/tavo-vartotojas/tavo-repozitorija.git
```

Kai paleisi šią komandą:

- Jei nenaudoji SSH, GitHub paprašys tavo **prisijungimo duomenų** (vartotojo vardo ir asmeninio prieigos rakto – Personal Access Token).
- Arba gali naudoti SSH, tada komandą rašyk taip:

```bash
git clone git@github.com:tavo-vartotojas/tavo-repozitorija.git
```

> Reikia būti **sukūrus SSH raktą** ir įkėlus jį į GitHub paskyrą. Jei reikia – galiu parodyti, kaip tai padaryti.

---

Po klonavimo:

```bash
cd tavo-repozitorija
```

Ir galite dirbti su failais, daryti commit'us ir push'inti.

---

### **1 užduotis: Pirkinių analizatorius**  
**Temos**: žodynai, `input`, `try-except`, ciklai  
**Užduotis**:  
Vartotojas įveda prekes formatu:  
```
obuolys:1.2, banana:0.99, pienas:2.3
```
Išvesk:
- Bendrą kainą
- Prekių, brangesnių nei 2€, skaičių
- Pigiausią prekę

---

### **2 užduotis: Skaičių analizė**  
**Temos**: sąrašai, `map`, `input`, funkcijos  
**Užduotis**:
- Vartotojas įveda skaičius: `10, 5, 3, 7, 12`
- Išvesk:
  - Skaičių kiekį
  - Skaičių vidurkį
  - Tik lyginius skaičius

---

### **3 užduotis: Mini bankomatas**  
**Temos**: funkcijos, sąlygos  
**Užduotis**:
- Sukurk meniu su pasirinkimais:
  - [1] Balansas
  - [2] Įnešti
  - [3] Išimti
- Tvarkyk balansą kintamajame
- Apsaugok nuo neigiamo balanso

---

### **4 užduotis: El. pašto tikrinimas**  
**Temos**: sąlygos, `in`, `string`  
**Užduotis**:
- Patikrink, ar vartotojo įvestas el. paštas:
  - Turi „@“
  - Baigiasi „.com“ arba „.lt“

---

### **5 užduotis: Lyginių skaičių suma**  
**Temos**: ciklai  
**Užduotis**:
- Suskaičiuok visų lyginių skaičių sumą nuo 1 iki 100

---

### **6 užduotis: Klasė `Automobilis` (patobulinta versija)**  
**Temos**: klasės, konstruktorius, metodai, validacija  

**Užduotis**:  
Sukurk klasę `Automobilis`, kuri turėtų šiuos duomenų laukus:  
- `marke` (tekstas) – automobilio markė,  
- `metai` (skaičius) – automobilio pagaminimo metai,  
- `rida` (skaičius) – automobilio rida kilometrais.  

**Reikalavimai**:  
1. Sukurk konstruktorių `__init__`, kuris priskirtų pradines reikšmes.  
2. Apsaugok, kad rida negalėtų būti neigiama – jeigu įvedama neigiama, laikyk ją lygią 0.  
3. Parašyk metodą `prideti_ridos(km: int)`, kuris padidina automobilio ridą. Jei perduodamas neigiamas skaičius – nieko nekeisk ir parodyk pranešimą.  
4. Parašyk metodą `gauti_info()`, kuris grąžina automobilio informaciją kaip teksto eilutę, pvz.:  
   `"Markė: Toyota, Metai: 2010, Rida: 200000 km"`  
5. (Papildoma) Parašyk metodą `ar_senas()`, kuris grąžina `True`, jei automobilis senesnis nei 15 metų, kitaip – `False`.

**Pavyzdinis naudojimas**:
```python
auto1 = Automobilis("Toyota", 2005, 250000)
print(auto1.gauti_info())       # Markė: Toyota, Metai: 2005, Rida: 250000 km
auto1.prideti_ridos(5000)
print(auto1.gauti_info())       # Markė: Toyota, Metai: 2005, Rida: 255000 km
auto1.prideti_ridos(-100)       # Negalima pridėti neigiamų kilometrų.
print(auto1.ar_senas())         # True
```

---

### **7 užduotis: Žodžių skaičiuotuvas**  
**Temos**: string, sąrašai  
**Užduotis**:
- Įvedus sakinį, grąžink:
  - Kiek žodžių
  - Kiek raidžių be tarpų

---

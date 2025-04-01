### **Paskaita: Funkcijos ir jų naudojimas**

#### **Įvadas į funkcijas**
Funkcijos yra specialiai apibrėžti kodo fragmentai, kurie gali būti iškviečiami pagal pavadinimą bet kurioje programos dalyje. Jos padeda organizuoti ir struktūrizuoti kodą, leidžia išvengti kodo kartojimo, nes funkcijas galima naudoti pakartotinai.

---

#### **Funkcijų paskirtis**
Funkcijos leidžia sugrupuoti logiką į atskirus blokus, kurie gali būti iškviečiami kelis kartus. Šis pavyzdys parodo, kaip aprašyti funkciją ir kaip ji gali būti naudojama programoje.

```python
# def <mūsų sugalvotas funkcijos pavadinimas> (): - skliausteliuose, funkcijos priimamasis
def say_hello():
    print("Hello world!!!")
    print("Funkcija atsisveikina")

# def aukščiau yra tik paruoštas vykdymui kodas,
# realiai jis įvykdomas, parašius funkcijos iškvietimą
say_hello()

# bandymas įsidėti funkcijos darbo rezultatą į kintamąjį
res = say_hello()  # į res įrašoma None, nes mūsų funkcijoje neaprašytas duomenų atidavimas iš funkcijos
print(res)  # None
```

**Apibendrinimas:**  
Funkcijos „print_hello“ pavyzdys demonstruoja, kaip galima išvengti kodo kartojimo, apibrėžiant atskiras funkcijas ir jas iškviečiant, kai reikia.

---

#### **Argumentai ir return reikšmės**
Funkcijos gali priimti argumentus (duomenis) ir grąžinti reikšmes naudojant `return`. Tai leidžia atlikti veiksmus su perduotais duomenimis ir gauti rezultatą.

```python
def give_hello_world():
    return "Hello world!"

res = give_hello_world()
print(res)  # Hello world!
```

**Apibendrinimas:**  
Funkcija `give_hello_world` parodo, kaip `return` naudojama grąžinti rezultatą. Tai padeda bendrauti funkcijoms ir pagrindinei programai.

---

#### **Funkcijos su keliais argumentais**
Funkcijos gali priimti kelis argumentus ir vykdyti veiksmus su kiekvienu iš jų. Tai suteikia galimybę apdoroti daugiau duomenų vienu metu.

```python
def say_hello_to2(name1, name2):
    hello_string = f"Hello to {name1} and hello to {name2}"
    return hello_string

res = say_hello_to2("Ramūnas", "Adomas")
print(res)
```

**Apibendrinimas:**  
Funkcija `say_hello_to2` priima du argumentus ir grąžina pasisveikinimą abiem žmonėms. Funkcijos gali apdoroti kelis duomenis vienu metu, atsižvelgiant į jų paskirtį.

---

#### **Numatytosios reikšmės ir keyword argumentai**
Šiame fragmente parodoma, kaip funkcijoms galima suteikti numatytąsias argumentų reikšmes ir kaip jas galima perduoti naudojant keyword argumentus.

```python
def greet(name="Drauge"):
    print(f"Hello, {name}!")

greet()  # Hello, Drauge!
greet("Ramūnas")  # Hello, Ramūnas!
```

Dalis argumentų gali būti poziciniai, jie rašomi pirmieji, po to rašomi keyword argumentai su numatytomis(default) reikšmėmis.

```python
# pacientas - paprastas argumentas
# gydytojas - default, keyword argumentas, jam priskiriama iškarto reikšmė,
# nes gydytojas gyd. Pagalnutylenis, yra pagrindinis ir dažniausiai priima
# pacientus
def priimk_pacienta(pacientas, gydytojas="gyd. Pagalnutylenis"):
    irasas_gyd_zurnale = f"Pacientas {pacientas}, priėmė {gydytojas}"
    return irasas_gyd_zurnale


res = priimk_pacienta("Adomas")
print(res)  # Pacientas Adomas, priėmė gyd. Pagalnutylenis

res = priimk_pacienta("Rolandas")
print(res)  # Pacientas Rolandas, priėmė gyd. Pagalnutylenis

res = priimk_pacienta("Adomas", gydytojas="gyd. Pakeitenis")
print(res)  # Pacientas Adomas, priėmė gyd. Pakeitenis
```

**Apibendrinimas:**  
Naudojant numatytąsias argumentų reikšmes, galima užtikrinti, kad funkcija veiks net ir be pateiktų argumentų. `Keyword` argumentai leidžia nurodyti reikšmes konkretiems parametrams pagal pavadinimą.

---

#### **Loginiai jungikliai funkcijose**
Funkcijos gali naudoti loginę struktūrą sprendimams priimti pagal argumentus. Loginiai jungikliai leidžia keisti funkcijos elgesį pagal perduotus duomenis. Loginiams jungikliams naudojami `keyword` argumentai su numatytomis reikšmėmis `True` arba `False`

```python
# speciali dalybos funkcija vykdanti
# paprastą dalybą ARBA (logika keičiasi)
# dalybą iki sveiko skaičiaus
def dalink_spec(sk1, sk2, iki_sveiko_sk=False):
    if not iki_sveiko_sk:
        return sk1 / sk2
    else:
        return sk1 // sk2
```

**Apibendrinimas:**  
Loginiai jungikliai leidžia funkcijai grąžinti rezultatą pagal tam tikrą sąlygą. Pavyzdžiui, funkcija `is_even` patikrina, ar skaičius lyginis.

---

#### **Docstringai funkcijose**
Docstringai naudojami funkcijos aprašymui, siekiant aiškiai nurodyti, ką ji daro, kokius argumentus priima ir ką grąžina. Doctringus galima matyti Pycharm užvedos pelės žymeklį ant funkcijos iškvietimo, tas suteikia patogumą išsiaiškinti ką daro viena ar kita funkcija.

```python
def say_hello(name):
    """
    Priima vardą ir atspausdina pasisveikinimą.
    :param name: str - vardas žmogaus
    :return: None
    """
    print(f"Hello, {name}")
```

**Apibendrinimas:**  
Docstringai pateikia funkcijos dokumentaciją, kuri leidžia programuotojams greitai suprasti funkcijos paskirtį ir kaip ji naudojama.

---

#### **Type hints ir anotacijos**
Type hints leidžia nurodyti duomenų tipus, kuriuos funkcijos priima arba grąžina. Tai padidina kodo aiškumą ir gali padėti išvengti klaidų, nes anotacijas naudoja automatiniai parašyto kodo tikrintojai.

```python
def add(x: int, y: int) -> int:
    return x + y

res = add("10", 10)  # bus rodomas įspėjimas
```

**Apibendrinimas:**  
Type hints naudojimas nurodo funkcijos argumentų ir grąžinamų duomenų tipus, padedant programuotojams aiškiau suprasti, kokie duomenys turėtų būti perduodami funkcijoms ir kokio tipo rezultatai bus grąžinami.
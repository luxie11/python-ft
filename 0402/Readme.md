Supratau! Štai atnaujintas konspektas, su apibendrinimais po kiekvieno kodo pavyzdžio, bet be teksto, kuris prasideda „Šis konspektas“:

---

### **Paskaita: `try-except` – Exceptionų (klaidų) suvaldymas**

---

#### **1. Įvadas į `try-except`**
`try-except` yra Python sakinys, skirtas suvaldyti klaidoms (exceptions) programoje. Naudojant šį mechanizmą, galima pagauti klaidas ir su jomis susitvarkyti, užtikrinant, kad programa nesugrius ir galės tęsti darbą po klaidos.

---

#### **Pagrindinis `try-except` pavyzdys**
Šiame pavyzdyje demonstruojama, kaip veikia `try-except` blokas. Mėginant atlikti operaciją su neteisingais duomenimis (pvz., dalyba iš nulio), programa sugeneruoja klaidą. `except` blokas pagaus klaidą ir leis programai ją suvaldyti.

```python
ivestis = '4'
try:
    skaicius = int(ivestis)
    res = skaicius / 0  # šis veiksmas sukels klaidą
except Exception as e:
    print("Mes crashinom, tačiau suvaldėm crashą")
    print(e.__class__)  # išspausdina klaidos klasę
    print(e)  # išspausdina klaidos pranešimą

print("Programa tęsia darbą")
```

**Apibendrinimas:**  
`try-except` blokas leidžia pagauti klaidą ir ją apdoroti, užtikrinant, kad programa nesugrius, o tęsis toliau. Tai ypač naudinga kritinėse situacijose, kai norima kontroliuoti klaidų valdymą ir išlaikyti programos stabilumą.

---

#### **2. Konkrečių klaidų (Exceptionų) gaudymas**
Konkretizuotas `try-except` naudojimas leidžia sugauti specifines klaidas, atsižvelgiant į jų tipą. Vietoje bendro `Exception`, galima nurodyti konkrečias klaidų klases, tokias kaip `ValueError` ar `ZeroDivisionError`, kad geriau valdyti programos elgesį esant tam tikroms klaidoms.

---

#### **Pavyzdys: Specifinių klaidų suvaldymas**
Šiame pavyzdyje programa prašo vartotojo įvesti du sveikus skaičius ir dalinti juos. `try-except` bloku gaudomi du specifiniai exceptionai: `ValueError`, jei vartotojas įveda neteisingą skaičių, ir `ZeroDivisionError`, jei dalijama iš nulio.

```python
ivestis1 = input("Įveskite sveiką skaičių")
ivestis2 = input("Įveskite daliklį")

try:
    skaicius = int(ivestis1)
    daliklis = int(ivestis2)
    res = skaicius / daliklis
except ValueError:
    print("Mes crashinom su ValueError")
    print("Paleiskite programą išnaujo ir ivestis padarykit kad tai būtų sveikas skaičius")
except ZeroDivisionError:
    print("Mes crashinom su ZeroDivisionError")
    print("Pakeiskite daliklį iš 0 į kitą")

print("Programa tęsia darbą")
```

**Apibendrinimas:**  
Specifinių klaidų gaudymas leidžia tiksliau apibrėžti, kokios klaidos bus apdorotos ir kokie veiksmai bus atlikti. Šiame pavyzdyje sugauti `ValueError` ir `ZeroDivisionError` klaidas leidžia tiksliai nurodyti, ką vartotojas turėtų pataisyti.

---

#### **3. `try-except-else-finally` struktūra**
Pilnas `try-except` blokas gali turėti papildomus elementus, tokius kaip `else` ir `finally`. Šie blokai leidžia dar labiau praplėsti klaidų valdymą:
- `else`: įvykdomas, kai `try` blokas nesugeneruoja klaidos.
- `finally`: visada įvykdomas, nesvarbu, ar klaida buvo sugeneruota, ar ne. Tai naudinga išvalymui ar užbaigimo veiksmams.

---

#### **Pavyzdys: `else` ir `finally` naudojimas**
Šiame pavyzdyje naudojamas pilnas `try-except` blokas. Jei klaida nesugeneruojama, įvykdomas `else` blokas, o nepriklausomai nuo rezultato, visada vykdomas `finally` blokas.

```python
try:
    res = 100 / 0
except ZeroDivisionError:
    print("Dalyba iš 0 negalima")
else:
    print(res)
```

**Apibendrinimas:**  
`else` blokas įvykdomas tik tada, kai klaidos nėra, o `except` sugauna tik tam tikrą klaidą (`ZeroDivisionError`). Šis pavyzdys rodo, kaip elgtis su papildomomis logikos dalimis, jei klaida neįvyksta.

---

#### **Pavyzdys: Naudojant `finally`**
`finally` blokas naudojamas nepriklausomai nuo to, ar klaida įvyksta, ar ne. Šiame pavyzdyje vartotojas turi įvesti teisingą skaičių, o `finally` blokas vykdomas kiekvieną kartą.

```python
while True:
    ivestis = input("Įveskite float skaičių")
    try:
        float_skaicius = float(ivestis)
        print("Įvestis tinkama", float_skaicius)
        break
    except ValueError:
        print("Įvestis NETINKAMA, pakartokite!!!")
    finally:
        print("Manęs niekaip neatsikratysit - FINALLY komanda")

print("Programa tęsia darbą")
```

**Apibendrinimas:**  
`finally` blokas garantuoja, kad tam tikras veiksmas bus atliekamas nepriklausomai nuo to, ar buvo klaida. Tai naudinga išvalymui ar veiksmams, kuriuos norime visada vykdyti.

---

#### **4. `raise` – Klaidos sukūrimas**
`raise` naudojamas, kai norime patys sąmoningai iššaukti klaidą (exception) tam tikromis sąlygomis. Tai naudinga, kai reikia nurodyti, kad funkcijos argumentai ar duomenys neatitinka numatytų reikalavimų. `raise` sukelia konkrečią klaidą, kurią galima pagauti ir suvaldyti naudojant `try-except`.

---

#### **Pavyzdys: `raise` naudojimas patikrinant argumentų tipą**
Ši funkcija `sumuok_int_skaicius` priima du argumentus, tikrina, ar jie yra sveiki skaičiai (`int`). Jei nors vienas argumentas nėra `int`, funkcija iššaukia `ValueError` klaidą naudodama `raise`.

```python
def sumuok_int_skaicius(sk1: int, sk2: int) -> int:
    if not (type(sk1) is int and type(sk2) is int):
        raise ValueError  # iššaukiame klaidą, jei argumentai nėra sveiki skaičiai
    return sk1 + sk2

res = sumuok_int_skaicius(4, 5)
print(res)
```

**Apibendrinimas:**  
`raise` leidžia rankiniu būdu sukelti klaidą, kai yra netinkami duomenys. Šiuo atveju funkcija neleidžia vykdyti tolimesnių veiksmų, jei argumentai nėra sveiki skaičiai, ir iššaukia `ValueError`.
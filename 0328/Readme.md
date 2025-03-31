### **Kartojimo sakiniai: `while` ir `for`**

#### **`while` ciklas:**
`while` ciklas naudojamas, kai reikia vykdyti tam tikrą kodą tol, kol tenkinama nurodyta sąlyga. Pavyzdžiui:

```python
while <sąlyga>:
    <kodo blokas, kuris bus kartojamas tol, kol sąlyga yra teisinga>
```

- Ciklas pasikartoja, kol sąlyga išlieka `True`. 
- Galima naudoti kartu su komandomis `break` ir `continue`, norint nutraukti ciklą arba praleisti tam tikrą iteraciją.

#### **`for` ciklas:**
`for` ciklas naudojamas perrinkti per elementus, esančius tam tikrame objekte, pvz., sąraše, žodyne ar intervale (range). Struktūra:

```python
for <elementas> in <objektas>:
    <kodo blokas, kuris bus vykdomas kiekvienam elementui>
```

- `for` ciklas iteruoja per kiekvieną elementą objekto viduje, kol elementų nebelieka.
- Galima naudoti kartu su komandomis `break` ir `continue`, norint praleisti iteraciją arba nutraukti ciklą.

---

#### **Paprastas `while` ciklas**
Šis fragmentas parodo, kaip veikia paprastas `while` ciklas, kuris kartoja kodą tol, kol tenkinama nurodyta sąlyga.

```python
skaitiklis = 0
while skaitiklis < 5:
    print("skaitiklis yra:", skaitiklis)
    print("---------------")
    skaitiklis += 1  # skaitiklis = skaitiklis + 1
```

**Apibendrinimas:**  
Šis fragmentas moko, kaip naudojamas paprastas `while` ciklas, kuris kartoja veiksmus tol, kol skaitiklis tampa mažesnis nei 5. Po kiekvieno ciklo skaitiklis padidinamas vienetu.

---

#### **`while True` su `break` komanda**
Šis pavyzdys parodo, kaip sukurti begalinį ciklą naudojant `while True` ir kaip jį nutraukti naudojant `break` komandą.

```python
while True:
    ivestis = input("Įveskite žodį (q - išeiti)")
    if ivestis == 'q':
        break
    print("Jūs įvedėte:", ivestis)
```

**Apibendrinimas:**  
Šiame cikle naudojama komanda `break`, kad būtų galima nutraukti ciklą, kai įvedamas žodis "q". Ciklas tęsiasi tol, kol įvedama kita reikšmė nei "q". Tai pavyzdys, kaip valdyti vartotojo įvestis cikle.

---

#### **`break` ir `continue` naudojimas `while` cikle**
Šis fragmentas moko, kaip naudoti komandas `break` ir `continue` norint valdyti ciklo eigą.

```python
while True:
    print("kartojimo pradžia")
    print("1. šis meniu punktas nedaro nieko\n"
          "2. išeiti iš kartojimo bloko\n"
          "3. vėl parodyti meniu")

    pasirinkimas = input()
    if pasirinkimas == "2":
        break
    elif pasirinkimas == "3":
        continue
    else:
        print("nieko nebuvo pasirinkta")
    print("kartojimo pabaiga")
```

**Apibendrinimas:**  
Čia naudojama `break`, norint nutraukti ciklą, kai pasirinkta opcija "2", ir `continue`, norint praleisti ciklo dalį, kai pasirenkama "3". Šis kodas moko valdyti ciklą dinamiškai pagal vartotojo įvestis.

---

#### **Vidinis `while` ciklas**
Šis kodas moko, kaip įdėti vieną `while` ciklą į kitą (`nested while loop`) ir naudoti `continue` bei `break` komandas vidiniuose cikluose.

```python
while True:
    print("1. atlikti skaičiaus daugybą\n"
          "2. išeiti")

    pasirinkimas = input()
    if pasirinkimas == "2":
        break

    if pasirinkimas == "1":
        # daugyba tęsis, kol nebus paspausta q
        while True:
            print("Įvesti skaičių daugybai iš 100 arba q - grįžti")
            ivestis = input()
            if ivestis == "q":
                break
            elif not ivestis.isdigit():
                print("Įvestas ne skaičius!!!")
                continue
            skaicius = int(ivestis) * 100
            print("Daugybos iš 100 rezultatas -", skaicius)
```

**Apibendrinimas:**  
Vidinis `while` ciklas tęsiamas tol, kol įvedamas teisingas skaičius, arba vartotojas pasirenka grįžti paspaudęs "q". Šis fragmentas moko kurti vidinius ciklus ir naudoti skirtingas sąlygas kiekviename lygmenyje.

---

#### **`for` ciklo pagrindai**
Šis fragmentas moko, kaip naudoti `for` ciklą iteruojant per skaičių intervalą.

```python
for skaicius in range(5):
    print("Dabartinis skaicius yra:", skaicius)
```

**Apibendrinimas:**  
Čia `for` ciklas iteruoja per intervalą nuo 0 iki 4 ir atspausdina kiekvieną skaičių. Tai moko, kaip naudoti `for` ciklą perinant per intervalus.

---

#### **Operacijos `for` cikle**
Šis pavyzdys moko, kaip naudoti sąlygas ir flagus ciklo viduje.

```python
listas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
flag5 = False
flag3 = False

for elem in listas:
    print(elem)
    if elem % 5 == 0:
        flag5 = True
    if elem % 3 == 0:
        flag3 = True

    if flag5 and flag3:
        break

if flag5:
    print("Liste yra elementas kuris dalinasi iš 5")
if flag3:
    print("Liste yra elementas kuris dalinasi iš 3")
```

**Apibendrinimas:**  
Šiame kode naudojami flagai ir sąlyginiai sakiniai `for` ciklo viduje, kad būtų patikrinta, ar elementai dalijasi iš 5 ir 3. Tai moko, kaip valdyti ciklą naudojant sudėtingesnes logines sąlygas.

---

#### **Kaupikliai cikluose**
Šis pavyzdys moko, kaip naudoti kaupiklius (`sum`, `max`, `min` ir kt.) ciklų viduje, kad būtų kaupiami tam tikri duomenys.

```python
listas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# suma
suma = 0
for elem in listas:
    suma += elem  # kaupiame sumą
print("Suma yra:", suma)

# maksimalus skaičius
maksimalus = listas[0]
for elem in listas:
    if elem > maksimalus:
        maksimalus = elem  # randame maksimalų elementą
print("Maksimalus yra:", maksimalus)
```

**Apibendrinimas:**  
Šiame kode naudojami ciklai kartu su kintamaisiais, kurie kaupia sumą ir maksimalų elementą iš sąrašo. Tai moko, kaip rinkti ir apdoroti informaciją ciklo metu, pvz., skaičiuoti sumą arba rasti didžiausią vertę sąraše.

---

#### **`break` ir `continue` komandos `for` cikle**
Šis fragmentas moko, kaip naudoti `break` ir `continue` komandas `for` cikle norint valdyti iteraciją.

```python
listas = ['sausis', 'vasaris', 'kovas', 'balandis', 'gegužė', 'birželis']

# break pavyzdys, spausdinam visus mėnesius, tačiau pasiekę balandį nutraukiam perrinkimą
for elem in listas:
    if elem == 'balandis':
        break
    print(elem)

# continue panaudosim praleisti sausį
for elem in listas:
    if elem == 'sausis':
        continue
    print(elem)
```

**Apibendrinimas:**  
Šis kodas parodo, kaip `break` komanda nutraukia `for` ciklą, kai pasiekiamas konkretus elementas, o `continue` komanda praleidžia tam tikras iteracijas (šiuo atveju – "sausį"). Tai leidžia valdyti, kuriuos elementus apdoroti ciklo metu.

---

#### **`else` blokas cikluose**
Šis pavyzdys moko, kaip naudoti `else` kartu su `for` ciklu ir kokios klaidos gali pasitaikyti netinkamai jį pritaikius.

```python
for skaicius in range(1, 5):
    if skaicius % 2 == 0:
        print("Skaičius", skaicius, "yra lyginis")
    else:
        print("Skaičius", skaicius, "yra nelyginis")

print("-----")

for skaicius in range(1, 5):
    if skaicius % 2 == 0:
        print("Skaičius", skaicius, "yra lyginis")
else:
    print("Ciklas baigtas")
```

**Apibendrinimas:**  
Šiame kode matome, kaip `else` blokas gali būti naudojamas po `for` ciklo. Kai ciklas baigiasi be pertraukų (pvz., be `break` komandos), `else` blokas vykdomas automatiškai. Tai naudinga norint atlikti papildomus veiksmus, kai ciklas pilnai baigtas.


### Sąlygos programoje, jų naudojimas su if

#### Sąlygos programoje

Sąlygos Python programavimo kalboje naudojamos tam, kad būtų galima palyginti reikšmes ir nustatyti, ar kodo fragmentas turėtų būti vykdomas. 

Dažniausiai naudojami palyginimo operatoriai yra:

- `>`: daugiau
- `>=`: daugiau arba lygu
- `<`: mažiau
- `<=`: mažiau arba lygu
- `==`: lygu
- `!=`: nelygu
- `is`: naudojamas tikrinant tapatumą
- `in`: naudojamas tikrinant, ar elementas yra kolekcijoje

Pvz.:
```python
numb1 = 100
numb2 = 500
numb3 = 100

print(numb1 < numb2)  # True
print(numb1 > numb2)  # False
print(numb1 == numb3)  # True
print(numb1 != numb3)  # False
```

Operatoriai `is` ir `in` taip pat naudojami sąlygose:
```python
print(type(numb1) is int)  # True
print("A" in "ABCD")  # True
```

Operatorius `in` gali būti naudojamas tikrinant, ar objektas yra kolekcijos dalis:
```python
char = "A"
text = "ABCD"
chars_numbers = ["ABCD", 100, "sausis", "vasaris"]

print(char in text)  # True
print(char in chars_numbers)  # False
print(text in chars_numbers)  # True
print(numb1 in chars_numbers)  # True
```

---

#### If sakinys

„If“ sakiniai naudojami norint keisti programos eigą – tam tikros kodo eilutės bus vykdomos tik tada, kai sąlyga yra teisinga (`True`).

Pavyzdys:
```python
numb1 = 100
numb2 = 500

if numb1 < numb2:
    print("numb1 yra mažesnis už numb2")
    print(f"numb1 yra {numb1}, numb2 yra {numb2}")
```

Jeigu sąlyga yra klaidinga, t.y., kai reikšmės neatitinka, kodas if bloke nėra vykdomas:
```python
if numb1 == numb2:  # False
    print("numb1 yra lygus numb2")
```

Taip pat galima naudoti „else“, kai reikia nurodyti, kas vykdytina, jei sąlyga nėra tenkinama:
```python
if numb1 > numb2:
    print("numb1 yra didesnis už numb2")
else:
    print("numb1 nėra didesnis už numb2")
```

---

#### „elif“ ir kelių sąlygų tikrinimas

Kai reikia patikrinti keletą sąlygų, galime naudoti „elif“, kuris suteikia galimybę patikrinti kitą sąlygą, jei pirmoji neteisinga:

Pavyzdys:
```python
if numb1 > numb2:
    print("numb1 yra didesnis už numb2")
elif numb1 == numb2:
    print("numb1 yra lygus numb2")
else:
    print("numb1 yra mažesnis už numb2")
```

Jeigu reikia tikrinti daugiau nei vieną sąlygą kartu, galima naudoti loginį operatorių `and`:
```python
if numb1 < numb2 and numb1 == 100:
    print("Abi sąlygos teisingos")
```

---

#### Loginiai operatoriai

Loginiai operatoriai leidžia derinti kelias sąlygas viename „if“ sakinyje:

- `and`: abi sąlygos turi būti teisingos
- `or`: bent viena sąlyga turi būti teisinga
- `not`: apverčia sąlygos reikšmę

Pvz.:
```python
if numb1 < numb2 and numb1 == 100:
    print("Abi sąlygos teisingos")
    
if numb1 < numb2 or numb1 == 500:
    print("Bent viena sąlyga teisinga")
    
if not numb1 > numb2:
    print("numb1 nėra didesnis už numb2")
```

Sujungiant daugiau sąlygų su „and“ ir „or“ reikia atkreipti dėmesį į operatorių prioretitą ir kontroliuoti vykdymo eiliškumą skliaustais, kitaip gali būti gaunami netikslūs rezultatai, nes pvz `and` suvykdomas pirmas ir tik po to `or'. Pateikiamam pavyzdyje nesuskkliaudus šios dalies `((auto in autos_ger) or (auto in autos_it))` programa veiks klaidingai. Pvz.:
```python
auto = "Audi"
autos_ger = ["BMW", "Audi", "Mercedes"]
autos_it = ["Ferrari", "Lamborghini"]
autos_sport = ["BMW", "Ferrari"]

if ((auto in autos_ger) or (auto in autos_it)) and (auto in autos_sport):
    print(auto, "yra vokiškas-sportinis arba itališkas-sportinis")
else:
    print(auto, "nėra tarp sportinių itališkų arba vokiškų")
```

---

#### Sutrumpintas if sakinys

Sutrumpintas if sakinys (ternary operatorius) leidžia rašyti sąlygas vienoje eilutėje, kai yra tik dvi galimos išvestys.

Pavyzdys:
```python
numb4 = 9
result = "lygus" if numb4 % 2 == 0 else "nelygus"
print(result)
```

---

#### Metodai, grąžinantys True arba False

Daugelyje situacijų Python metodai grąžina logines reikšmes (`True` arba `False`). Jie gali būti naudojami „if“ sakiniuose kaip sąlygos. Pavyzdžiai naudos `str` metodus, dirbančius su simbolių eilutėmis - `startswith()`, `istitle()`, `isupper()` ir kt.

Pvz.:
```python
miestas1 = "Vilnius"
miestas2 = "Kaunas"

# Ar prasideda didžiąja raide
print(miestas1.istitle())  # True

# Ar visi simboliai didžiosios
print(miestas1.isupper())  # False

# Ar prasideda tam tikru simboliu
print(miestas1.startswith("V"))  # True
print(miestas2.startswith("V"))  # False
```

---

### Pratimai

#### 1 pratimas

Sukurkite sąrašą miestų ir mėnesių, atskirdami juos remiantis didžiųjų raidžių buvimu pavadinime:
```python
listas = ['vasaris', 'sausis', 'Vilnius', 'Kaunas', 'balandis', 'Panevėžys', '45']
menesiai = []
miestai = []

for elem in listas:
    if elem.istitle():
        miestai.append(elem)
    elif elem.isalpha():
        menesiai.append(elem)

print(miestai)  # ['Vilnius', 'Kaunas', 'Panevėžys']
print(menesiai)  # ['vasaris', 'sausis', 'balandis']
```

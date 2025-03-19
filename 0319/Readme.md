
# Python sąrašai ir jų panaudojimas

## Kas yra sąrašas (list)?
Sąrašas (`list`) Python kalboje yra kintama duomenų struktūra, kuri gali talpinti daug elementų. Sąrašo elementai gali būti skirtingų tipų, pavyzdžiui, skaičiai, eilutės, **kiti sąrašai** ar net funkcijos. Sąrašai yra **indeksuojami** (t.y., kiekvienas elementas turi savo vietą sąraše), **kintami** (elementai gali būti keičiami), ir **heterogeniški** (elementai gali būti skirtingų tipų).

Naudojant sąrašus galima atlikti daugybę veiksmų: pridėti naujus elementus, pašalinti esamus, keisti elementus, iteruoti per sąrašą, skaičiuoti elementų skaičių, rikiuoti ir t.t.

#### Sąrašų metodai
Išmoksime dirbti su sąrašais ir jų metodais. Bus apžvelgti šie veiksmai:
- **Tuščio sąrašo sukūrimas**: Norint pradėti dirbti su sąrašu, pirmiausia reikia jį sukurti. Tuščias sąrašas sukuriamas tiesiog parašius `[]`.
- **Elementų pridėjimas**: `append()` metodas leidžia pridėti naujus elementus į sąrašo pabaigą. `insert()` leidžia pridėti elementą į nurodytą poziciją pagal indeksą.
- **Elementų šalinimas**: Galite naudoti `remove()` norint pašalinti pirmą pasitaikiusį elementą pagal reikšmę arba `pop()` norint pašalinti elementą pagal indeksą (jei indeksas nenurodomas, šalinamas paskutinis elementas).
- **Indeksavimas**: Sąrašo elementai gali būti pasiekti pagal jų indeksus, pradedant nuo `0`. Galite taip pat naudoti neigiamus indeksus norint pasiekti elementus nuo sąrašo galo.

```python
# sukuriam tuščią sąrašą
sarasas = []
print(type(sarasas))  # <class 'list'>
print(sarasas)  # []

# duomenys kuriais pildysim tuščią sąrašą
men1 = "sausis"
men2 = "vasaris"

# .append() prijungia naują elementą į sąrašo pabaigą
sarasas.append(men1)
print(sarasas)  # ['sausis']

sarasas.append(men2)
print(sarasas)  # ['sausis', 'vasaris']

sarasas.append("kovas")
sarasas.append(2024)
print(sarasas)  # ['sausis', 'vasaris', 'kovas', 2024]

# .insert() prijungia naują elementą, indeksu nurodytoj pozicijoj
sarasas.insert(0, "balandis")
sarasas.insert(-1, "balandis")
print(sarasas)  # ['balandis', 'sausis', 'vasaris', 'kovas', 'balandis', 2024]

sarasas.insert(2, "birželis")
print(sarasas)  # ['balandis', 'sausis', 'birželis', 'vasaris', 'kovas', 'balandis', 2024]

# .remove() - pašalinti elementą, pagal reikšmę(šalinamas pirmas pasitaikęs)
sarasas.remove("balandis")
print(sarasas)  # ['sausis', 'birželis', 'vasaris', 'kovas', 'balandis', 2024]

# .pop() - išmesti paskutinį(nenurodžius indekso) arba nurodytą elementą
# šalinamas elementas grąžinamas
sarasas.pop()
print(sarasas)  # ['sausis', 'birželis', 'vasaris', 'kovas', 'balandis']

# gaudom šalinamą elementą, taip pat nurodom jo indeksą
ismestas = sarasas.pop(1)
print(ismestas)  # birželis
print(sarasas)  # ['sausis', 'vasaris', 'kovas', 'balandis']

# del - python komanda trinti
del sarasas[-1]
print(sarasas)  # ['sausis', 'vasaris', 'kovas']

# indeksai listuose
print(sarasas[1])  # vasaris
print(sarasas[1:])  # ['vasaris', 'kovas']

print(sarasas)  # ['sausis', 'vasaris', 'kovas']
sarasas[0] = "lapkritis"
print(sarasas)  # ['lapkritis', 'vasaris', 'kovas']

```

#### Sąrašų iteravimas
Bus apžvelgti šie veiksmai:
- **`for` ciklo naudojimas**: Sąrašo elementai gali būti peržiūrimi naudojant `for` ciklą. Kiekvienas sąrašo elementas automatiškai perduodamas į ciklo kintamąjį.
- **Skaičiavimai su sąrašais**: Iteruojant per sąrašą, galima atlikti įvairius veiksmus su elementais, pavyzdžiui, suskaičiuoti sumą, atlikti daugybą, filtruoti elementus.
- **Kaupimas cikluose**: Naudojant iteraciją, galima sukaupti reikšmes, pavyzdžiui, suskaičiuoti visų sąrašo skaičių sumą.

Pavyzdys kaip sąrašo iteravimas atrodo javascript kalboje:

```javascript
# for (let i = 0; i < array.length; i++) {
#   console.log(array[i]);

# }
```

Python kalbos pavyzdžiai:
```python
menesiai = ['sausis', 'vasaris', 'kovas', 'balandis']

# for sakinyje po for komandos privalom įrašyti
# kintamojo pavadinimą, kuris bus automatiškai
# sukurtas saugoti iteruojamiems elementams
for elem in menesiai:
    print(elem, "mėn.")  # sausis mėn., ..
    print(elem.upper())  # SAUSIS, ..
    print("*****")  # *****, ..

print("---------------")

skaiciai = [10, 7, 50, 111]

for elem in skaiciai:
    print(elem * 100)  # 1000, .., 11100

print("---------------")

# sumavimas, kaupimas iteruojant
suma = 0
for elem in skaiciai:
    suma += elem  # suma = suma + elem

print(suma)  # 178

# susumuojam elementus, kiekvieną padaugintą iš 100
suma = 0
for elem in skaiciai:
    # suma = suma + elem * 100
    suma += elem * 100

print(suma)  # 17800

# sumavimas, kaupimas iteruojant, kas antrą skaičių
suma = 0
for elem in skaiciai[::2]:
    # suma = suma + elem
    suma += elem

print(suma)  # 60

```

#### Python integruotos funkcijos galinčios dirbti su sąrašais
Kai kurios integruotos, bendros paskirties Python funkcijos, taip pat dirba su sąrašais.

```python
skaiciai = [10, 7, 50, 111]
tuscias = []

# len - listo ilgis, elementų skaičius
print(len(skaiciai))  # 4
print(len(tuscias))  # 0

# veikia ir su str tipu  
print(len("ABC"))  # 3

# sum - elementų suma
print(sum(skaiciai))  # 178

# max - didžiausias skaičius
print(max(skaiciai))  # 111

# min - mažiausias skaičius
print(min(skaiciai))  # 7

```

#### Sąrašų indeksavimas
Sąrašai indeksuojami analogiškai kaip `str` tipas ir yra galimi tie patys veiksmai:
- **Indeksų naudojimas**: Kiekvienas sąrašo elementas turi savo indeksą, pradedant nuo `0`. Indeksavimas leidžia pasiekti bet kurį elementą sąraše. Naudojant neigiamus indeksus, galite pasiekti sąrašo elementus nuo galo (pvz., `-1` reikšmė atitinka paskutinį sąrašo elementą).
- **Sąrašo pjaustymas**: Python leidžia gauti tam tikras sąrašo dalis naudojant pjaustymo (angl. slicing) sintaksę. Pvz., `list[start:stop:step]` leidžia gauti elementus nuo `start` iki `stop` su tam tikru žingsniu `step`.

```python
months = ['sausis', 'vasaris', 'kovas', 'balandis', 'gegužė', 'birželis']

# indeksavimas
print(months[0])  # sausis
print(months[-1])  # birželis

# sliceinimas
print(months[1:4])  # ['vasaris', 'kovas', 'balandis']
print(months[1:3 + 1])  # ['vasaris', 'kovas', 'balandis']
print(months[1:])  # ['vasaris', 'kovas', 'balandis', 'gegužė', 'birželis']
print(months[:5])  # ['sausis', 'vasaris', 'kovas', 'balandis', 'gegužė']

# žingsniai
print(months[::3])  # kas trečias - ['sausis', 'balandis']
print(months[::-1])  # atvirkščiai - ['birželis', 'gegužė', 'balandis', 'kovas', 'vasaris', 'sausis']
print(months[::-2])  # atvirkščiai kas antrą - ['birželis', 'balandis', 'vasaris']

# papildomos operacijos po 1 elemento ištraukimo
# gavę stringą pagal indeksą liste, papildomai indeksuojam stringą,
# ištraukiam iš stringo 1 indeksu esantį simbolį
print(
    months[0][1]  # a
)

# suvykdom stringui vieną iš stringų metodų
print(
    months[1].upper()  # VASARIS
)

```

#### Tuple – nekintami sąrašai
Tuple savybės:
- **Tuple sukūrimas**: `tuple` yra panašus į sąrašą, tačiau esminis skirtumas yra tas, kad `tuple` negali būti keičiama po sukūrimo. Tai reiškia, kad negalite pridėti ar pašalinti elementų po to, kai tuple yra sukurta.
- **Tuple indeksavimas**: Kaip ir sąrašuose, tuple elementai gali būti pasiekiami pagal jų indeksus.

```python
# duomenų tipas - tuple, listas kuriame negalimi pakeitimai

months = ('sausis', 'vasaris', 'kovas', 'balandis', 'gegužė', 'birželis', 'sausis')

print(type(months))  # <class 'tuple'>

for elem in months:
    print(elem)  # sausis, ..

# galim indeksuoti
print(months[0])  # sausis

# slice
print(months[1:])  # ('vasaris', 'kovas', 'balandis', 'gegužė', 'birželis', 'sausis')

# keitimo operacijos neįmanomos (CRASH)
# del months[0]
# months[0] = "gruodis"

# galimi tik 2 metodai, šie metodai taip pačiai veikia ir su listais
# .index() - grąžina elemento indeksą
print(months.index("gegužė"))  # 4

# .count() - suskaičiuoja pasikartojimus elementų pagal reikšmę
print(months.count("sausis"))  # 2

# papildom tuplą perrašydami orginalą
months = months + ("lapkritis", "gruodis")
print(months)  # ('sausis', 'vasaris', 'kovas', 'balandis', 'gegužė', 'birželis', 'sausis', 'lapkritis', 'gruodis')
```

#### Sąrašai sąrašuose
Sudėtinių sąrašų panaudojimas:
- **Sąrašai sąrašuose**: Python leidžia kurti sąrašus, kuriuose gali būti kiti sąrašai kaip elementai. Tai naudinga, kai norite saugoti sudėtinius duomenis, pavyzdžiui, darbuotojų duomenis (vardas, pareigos, atlyginimas).
- **Vidinių sąrašų iteracija**: Naudodami `for` ciklą galite iteruoti per išorinius sąrašus, o tada – per vidinius sąrašus. 
- **Sudėtingų duomenų apdorojimas**: Demonstracija, kaip suskaičiuoti vidinių sąrašų duomenis (pvz., bendrą atlyginimų sumą arba kiek yra tam tikrų pareigų darbuotojų).

```python
darbuotojai = [
    ['Valdas', 'programuotojas', 2000],
    ['Adomas', 'direktorius', 3000],
    ['Aldona', 'vadybininkas', 1800],
    ['Jogaila', 'programuotojas', 2500]
]

print(darbuotojai[0])  # ['Valdas', 'programuotojas', 2000]
print(darbuotojai[0][1])  # programuotojas
print(darbuotojai[0][1].upper())  # PROGRAMUOTOJAS

# printinam po 1 vidinį pilną listą
for listas in darbuotojai:
    print(listas)  # ['Valdas', 'programuotojas', 2000], ..

# printinam atskirus elementus iš kiekvieno vidinio listo
# imdami per indeksą
for listas in darbuotojai:
    print(listas[0], listas[2])  # Valdas programuotojas, ..

# python priimta yra išardyti listus for eilutėje
for vardas, pareigos, atlyginimas in darbuotojai:
    print(atlyginimas, vardas, pareigos)  # Valdas 2000 programuotojas, ..

# susumuojam atlyginimus
# variantas 1
suma = 0
for vardas, pareigos, atlyginimas in darbuotojai:
    suma += atlyginimas

print(suma)  # 9300

# variantas 2
atlyginimai = []  # tuščias listas, sukaupti visiems atlyginimams
for vardas, pareigos, atlyginimas in darbuotojai:
    atlyginimai.append(atlyginimas)

print(atlyginimai)  # [2000, 3000, 1800, 2500]
print(sum(atlyginimai))  # 9300

# suskaičiuojam programuotojus
pozicijos = []
for vardas, pareigos, atlyginimas in darbuotojai:
    pozicijos.append(pareigos)

print(pozicijos)  # ['programuotojas', 'direktorius', 'vadybininkas', 'programuotojas']
print("Programuotojų skaičius yra", pozicijos.count("programuotojas"))  # Programuotojų skaičius yra 2

# TODO perdaryti, kad atlyginimų fondas ir programuotojai būtų suskaičiuoti naudojant 1 for ciklą
```

#### String metodai sąrašams
Kai kurie `str` metodai sąveikauja su sąrašais:
- **`split()` metodas**: Padalina eilutę (`str`) į sąrašą pagal tam tikrą simbolį. Pavyzdžiui, eilutę galima padalinti į sąrašą naudojant tarpą kaip skiriamąjį simbolį.
- **`join()` metodas**: Sujungia sąrašo elementus į vieną eilutę, naudojant nurodytą jungiklį (pvz., tarpą arba kitą simbolį tarp elementų).

```python
months_str = "sausis vasaris kovas"  # str
print(months_str)  # sausis vasaris kovas  # sausis vasaris kovas

# str metodas .split() - padalina str į listą
# per nurodytą simbolį
months_list = months_str.split(" ")
print(months_list)  # ['sausis', 'vasaris', 'kovas']

# months_list = months_str.split("a")
# print(months_list)  # ['s', 'usis v', 's', 'ris kov', 's']

# str metodas .join() - sujungia stringų dalis į vieną stringą
# naudodamas skirtuką
joined_str = " ".join(months_list)
print(joined_str)  # sausis vasaris kovas

joined_str = "---".join(months_list)
print(joined_str)  # sausis---vasaris---kovas
```

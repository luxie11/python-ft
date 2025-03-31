# Comprehensions sudarymas ir filtravimo operacijos

Comprehensions (sutrumpintos sąrašų, žodynų, aibių ir kitų struktūrų sudarymo konstrukcijos) leidžia lengvai kurti naujus sąrašus ar kitas struktūras iš esamų duomenų, naudojant ciklus, sąlyginius sakinius ir įvairias operacijas. Pagrindiniai veiksmai gali būti apimantys tiek duomenų transformacijas, tiek filtravimą.

## List Comprehensions naudojimas
Šis fragmentas moko, kaip sukurti naują sąrašą naudojant list comprehension, kuris leidžia sudaryti sąrašus efektyviau ir trumpiau nei naudojant paprastą for ciklą.

```python
kaupiklis = []
duomenu_listas = [1, 10, 2, 20, 3, 30, 4, 40]

for elem in duomenu_listas:
    kaupiklis.append(elem)

print(kaupiklis)  # [1, 10, 2, 20, 3, 30, 4, 40]

# tas pats rezultatas, naudojant list comprehension
kaupiklis2 = [elem for elem in duomenu_listas]
print(kaupiklis2)  # [1, 10, 2, 20, 3, 30, 4, 40]
```

## Operacijų atlikimas naudojant list comprehension
Šis fragmentas moko, kaip naudoti list comprehension, kad būtų atliekamos įvairios operacijos su sąrašo elementais, pvz., skaičių dauginimas arba kvadratų skaičiavimas.

```python
# visi seno listo skaičiai sudauginami iš 9
kaupiklis3 = [elem * 9 for elem in duomenu_listas]
print(kaupiklis3)  # [9, 90, 18, 180, 27, 270, 36, 360]

# visi seno listo skaičiai pakelti kvadratu
kaupiklis4 = [elem ** 2 for elem in duomenu_listas]
print(kaupiklis4)  # [1, 100, 4, 400, 9, 900, 16, 1600]
```

## Vidinės struktūros sudarymas naudojant list comprehension
Šis pavyzdys parodo, kaip sukurti sudėtingesnes struktūras, tokias kaip sąrašai, kurių elementai patys yra sąrašai su skaičių kvadratais ir kubais.

```python
# struktūra [skaicius, skaicius kvadratu]
kaupiklis5 = [[elem, elem ** 2] for elem in duomenu_listas]
print(kaupiklis5)  # [[1, 1], [10, 100], [2, 4],.. , [4, 16], [40, 1600]]

# struktūra [skaicius, skaicius kvadratu, skaicius kubu]
kaupiklis6 = [[elem, elem ** 2, elem ** 3] for elem in duomenu_listas]
print(kaupiklis6)   # [[1, 1, 1], [10, 100, 1000], [2, 4, 8],.. , [4, 16, 64], [40, 1600, 64000]]
```

## Duomenų filtravimas naudojant list comprehension
Šis fragmentas moko, kaip filtruoti sąrašus pagal tam tikras sąlygas naudojant list comprehension.

```python
listas = [1, 10, 2, 20, 3, 30, 4, 40, 99]

# išfiltruojam, kad gautume elementus tik mažesnius už 10
res = [elem for elem in listas if elem < 10]
print(res)  # [1, 2, 3, 4]
```

## Sudėtingas list comprehension su keliais for ir sąlyginiais sakiniais
Šis fragmentas moko, kaip galima naudoti kelis for ciklus ir sąlyginius sakinius viename list comprehension.

```python
raides = ['A', 'B', 'C']
skaiciai = ['1', '2', '3', '4']

res = [raid + sk for raid in raides for sk in skaiciai]
print(res)  # ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4']
```

## Comprehension naudojimas su kitomis duomenų struktūromis
Šis fragmentas moko, kaip naudoti comprehension su kitomis struktūromis, tokiomis kaip tuplės, žodynai ir aibės.

```python
listas = [0, 0, 5, 2, 3, 3, 3]

# tuple comprehension
tuple_res = tuple(elem for elem in listas)
print(tuple_res)  # (0, 0, 5, 2, 3, 3, 3)

# dict comprehension
dict_res = {elem: elem ** 2 for elem in listas}
print(dict_res)  # {0: 0, 5: 25, 2: 4, 3: 9}

# set comprehension
set_res = {elem for elem in listas}
print(set_res)  # {0, 2, 3, 5}
```

---
Šis dokumentas padeda suprasti comprehension naudojimą skirtingoms duomenų struktūroms ir kaip jis gali palengvinti kodavimą.
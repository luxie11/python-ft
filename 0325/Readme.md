# Python Integruotos Funkcijos: Pagrindai

Python siūlo daug integruotų funkcijų, kurios palengvina įvairias operacijas su duomenimis, jų apdorojimą, spausdinimą, įvedimą ir kt. Šios funkcijos leidžia atlikti dažniausiai naudojamas užduotis be papildomų bibliotekų.

## Dažnai naudojamos funkcijos

### `print` – naudojama informacijai išvesti į terminalą.
```python
print("Hello, world!")
```
Spausdina tekstą ar kintamąjį į konsolę.

### `input` – priima vartotojo įvestį iš terminalo.
```python
vardas = input("Įveskite savo vardą: ")
print(vardas)
```

### `len` – grąžina rinkinio (pvz., sąrašo ar eilutės) ilgį.
```python
text = "ABC"
res = len(text)  # Grąžins 3
```

### `sum` – apskaičiuoja sekos elementų sumą.
```python
skaiciu_listas = [10, 122, 8, 7]
res = sum(skaiciu_listas)  # Grąžins 147
```

### `max` ir `min` – grąžina didžiausią ir mažiausią reikšmę sekoje.
```python
res = max(skaiciu_listas)  # Grąžins 122
res = min(skaiciu_listas)  # Grąžins 7
```

### `type` – nustato kintamojo tipą.
```python
text = "ABC"
res = type(text)  # Grąžins <class 'str'>
```

### Duomenų konvertavimo funkcijos
`int`, `float`, `str`, `tuple`, `list`, `bool` – leidžia pakeisti vieną tipą į kitą.

> **Svarbu:** Nepavadinkite kintamųjų taip pat kaip šios funkcijos, nes tai gali sukelti klaidų.

---
## `range` funkcija

Funkcija `range` grąžina nurodytą skaičių diapazoną, dažniausiai naudojamą kartu su `for` ciklu.

### Naudojimas su ciklu:
```python
for skaicius in range(5):
    print(skaicius)  # 0, 1, 2, 3, 4
```

### Praktinis panaudojimas:
```python
for skaicius in range(5):
    print(skaicius ** 2)  # 0, 1, 4, 9, 16
```

---
## `print` funkcija su parametrais

### Separatorius (`sep`)
```python
print("A", "B", "C", sep="|")  # A|B|C
```

### Baigiamoji reikšmė (`end`)
```python
print("Hello", end=" ")
print("World!")  # Hello World!
```

---
## `type` funkcija ir tipų patikra

Tipų tikrinimas gali būti atliekamas naudojant `type` funkciją:
```python
listas = ['abc', 123, True]
for elem in listas:
    if type(elem) is str:
        print(elem.upper())  # ABC
    elif type(elem) is int:
        print(elem * 10)  # 1230
```

---
## `round` ir `sorted` funkcijos

### `round` – naudojama skaičių apvalinimui.
```python
x = 1.123456789
res = round(x, 5)  # Grąžins 1.12346
```

### `sorted` – rikiuoja duomenis didėjimo arba mažėjimo tvarka.
```python
skaiciai = [5, 1, 0, 100, 20]
res = sorted(skaiciai)  # Grąžins [0, 1, 5, 20, 100]
```

### Lietuviškų raidžių rikiavimas
Naudojant `locale`, galima tinkamai rikiuoti tekstą su lietuviškomis raidėmis:
```python
import locale
locale.setlocale(locale.LC_ALL, 'lt_LT')
list_lt = ["Žemė", "Ąžuolas", "Vilnius"]
res = sorted(list_lt, key=locale.strxfrm)
print(res)  # ['Ąžuolas', 'Vilnius', 'Žemė']
```

---
## Apibendrinimas
Šios funkcijos yra labai naudingos kasdieniame programavime, leidžia efektyviai dirbti su duomenimis ir jų apdorojimu. Atkreipkite dėmesį į kintamųjų pavadinimus, kad jie nesutaptų su integruotomis funkcijomis, ir išnaudokite `print`, `range`, `type`, `round`, `sorted` bei kitas funkcijas, siekdami rašyti švarų ir aiškų kodą.
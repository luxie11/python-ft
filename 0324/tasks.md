# Python Sąlyginiai sakiniai (if) - Užduotys

## 1 užduotis: Temperatūros klasifikacija
Parašykite programą, kuri prašo vartotojo įvesti temperatūrą laipsniais Celsijaus ir pagal šią temperatūrą išveda pranešimą:
- Jei temperatūra mažesnė nei 0, spausdinti: "Šalta"
- Jei tarp 0 ir 20 (imtinai), spausdinti: "Vėsu"
- Jei daugiau nei 20, spausdinti: "Šilta"

## 2 užduotis: Slaptažodžio tikrinimas
Parašykite programą, kuri tikrina vartotojo įvestą slaptažodį.
- Jei slaptažodis yra "Python123", išveda: "Slaptažodis teisingas"
- Jei ne, išveda: "Neteisingas slaptažodis"

## 3 užduotis: Lyginiai ir nelyginiai skaičiai
Sukurkite programą, kuri paprašo vartotojo įvesti skaičių ir patikrina:
- Jei skaičius yra lyginis, išveda: "Skaičius yra lyginis"
- Jei skaičius yra nelyginis, išveda: "Skaičius yra nelyginis"

## 4 užduotis: Amžiaus kategorijos
Paprašykite vartotojo įvesti savo amžių ir klasifikuokite jį pagal šiuos kriterijus:
- Jei mažiau nei 7 metai: "Jūs esate darželinukas"
- Jei tarp 7 ir 18: "Jūs esate moksleivis"
- Jei tarp 19 ir 25: "Jūs esate studentas"
- Jei daugiau nei 25: "Jūs esate suaugęs"

## 5 užduotis: Skaičių rėžiai
Paprašykite vartotojo įvesti skaičių ir patikrinkite:
- Jei skaičius tarp 1 ir 10: "Skaičius mažas"
- Jei tarp 11 ir 100: "Skaičius vidutinis"
- Jei daugiau nei 100: "Skaičius didelis"

## 6 užduotis: Sąrašo filtravimas su ciklu
Turite sąrašą skaičių. Naudodami `for` ciklą ir `if` sąlygą, atskirkite lyginius ir nelyginius skaičius į atskirus sąrašus.

```python
skaiciai = [3, 7, 2, 8, 10, 15, 21, 30, 42, 55]
lyginiai = []
nelyginiai = []

```

Rezultatas:
```
Lyginiai skaičiai: [2, 8, 10, 30, 42]
Nelyginiai skaičiai: [3, 7, 15, 21, 55]
```

## 7 užduotis: Studentų pažymių analizė
Sukurkite programą, kuri analizuoja studentų pažymius iš sąrašo ir klasifikuoja juos į skirtingas kategorijas:
- Pažymiai 9-10: "Puikiai"
- Pažymiai 7-8: "Gerai"
- Pažymiai 5-6: "Patenkinamai"
- Pažymiai mažesni nei 5: "Nepatenkinamai"

```python
pazymiai = [10, 8, 7, 5, 9, 4, 6, 10, 3, 7, 8]
puikiai = []
gerai = []
patenkinamai = []
nepatenkinamai = []

```

Rezultatas:
```
Puikiai: [10, 9, 10]
Gerai: [8, 7, 7, 8]
Patenkinamai: [5, 6]
Nepatenkinamai: [4, 3]
```


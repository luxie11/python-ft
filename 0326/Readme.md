# Python Žodynai

## Įvadas
Python žodynai (`dict`) yra duomenų struktūros, kuriose duomenys saugomi poromis **raktas: reikšmė**. Kiekvieno elemento reikšmė pasiekiama per unikalų raktą. 

Raktai dažniausiai būna **string** tipo, tačiau reikšmės gali būti bet kokio tipo. Python žodynai gali būti suderinami su JSON formatu, bet tai nėra tas pats kaip JSON (tačiau galima konvertuoti).

---

## Žodyno sukūrimas ir reikšmių pasiekimas

Pavyzdys, kaip sukurti žodyną `person_info`, kuris saugo informaciją apie asmenį:

```python
# žodyno su duomenimis sukūrimas
person_info = {
    "name": "Albert",
    "surname": "Einstein",
    "languages": ["German", "Latin", "Italian", "English"],
    "occupation": {"role": "Professor",
                   "workplace": "Uni of Berlin"}
}

print(person_info)
print(type(person_info))
```

### Reikšmių pasiekimas pagal raktus

```python
res = person_info["name"]
print(res)   # Albert

print(person_info["surname"])  # Einstein
print(person_info["languages"])  # ['German', 'Latin', 'Italian', 'English']
print(person_info["languages"][1])  # Latin
print(person_info["languages"][2])  # Italian

print(person_info["occupation"])   # {'role': 'Professor', 'workplace': 'Uni of Berlin'}
print(person_info["occupation"]["role"])   # Professor
print(person_info["occupation"]["workplace"])   # Uni of Berlin
```

---

## Iteracija per žodyną

Naudojamas `for` ciklas iteruoti per žodyną `person_info`, kad būtų atspausdinti visi raktai ir jų reikšmės.

```python
# Iteracija per žodyną
for key, value in person_info.items():
    print(key, value)
```

---

## Klaidos

Jei bandome pasiekti neegzistuojantį raktą, Python gražins klaidą:

```python
# CRASH, kai raktas neegzistuoja
print(person_info["spouse"])  # KeyError
```

Norint išvengti klaidų, galima naudoti `get()` metodą:

```python
print(person_info.get("spouse", "Neegzistuoja"))  # Neegzistuoja
```

---

## Žodyno pildymas ir reikšmių keitimas

```python
# Sukuriame tuščią žodyną
auto = {}
print(auto)

# Pridedame duomenis
auto["make"] = "Audi"
print(auto)  # {'make': 'Audi'}

auto["make"] = "BMW"
print(auto)  # {'make': 'BMW'}

auto["model"] = "x5"
print(auto)  # {'make': 'BMW', 'model': 'x5'}

auto["colors"] = ["red", "white", "black"]
print(auto)  # {'make': 'BMW', 'model': 'x5', 'colors': ['red', 'white', 'black']}
```

---

## Žodynų sujungimas naudojant `.update()`

```python
# Sukuriame papildomą žodyną
bonus_info = {"engine": 2, "interior": "leather"}
auto.update(bonus_info)
print(auto)  # {'make': 'BMW', 'model': 'x5', 'colors': [...], 'engine': 2, 'interior': 'leather'}

# Pridedame dar kelis laukus
auto.update({"year": 2000, "eco2000": True})
print(auto)
```

---

## Duomenų pašalinimas ir reikšmių keitimas

```python
# Pašaliname elementą
del auto["eco2000"]
print(auto)

auto.pop("interior")
print(auto)

# Pervadiname raktą
auto["gas_engine"] = auto.pop("engine")
print(auto)

# Keičiame metus
auto["year"] = 2001
print(auto)

auto["year"] += 10
print(auto)

# Pridedame spalvą
auto["colors"].append("yellow")
print(auto)
```



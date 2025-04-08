#  Funkcijos: `*args`, `**kwargs`, `lambda` – Praktinės Užduotys

Šis rinkinys skirtas praktiniam `*args`, `**kwargs` ir `lambda` funkcijų naudojimui. Užduotys padės pagilinti supratimą apie lankstesnį funkcijų naudojimą.



##  1. Suskaičiuok sumą naudodamas `*args`

**Užduotis:**  
Sukurk funkciją `suma(*args)`, kuri grąžintų visų pateiktų skaičių sumą.

### Testai:
```python
print(suma(1, 2, 3))         # 6
print(suma(10, 20))          # 30
print(suma())                # 0
```

### Atsakymai:
```
6
30
0
```

---

##  2. Sugeneruok pasisveikinimus su `*args`

**Užduotis:**  
Sukurk funkciją `sveikinkis(*vardai)`, kuri kiekvienam vardui grąžintų eilutę `Sveikas, {vardas}!`.

### Testai:
```python
print(sveikinkis("Jonas", "Aistė"))
print(sveikinkis("Tomas"))
```

### Atsakymai:
```
Sveikas, Jonas!
Sveikas, Aistė!

Sveikas, Tomas!
```

---

##  3. Pakelk skaičius kvadratu su `*args`

**Užduotis:**  
Sukurk funkciją `pakelk_kvadratu(*args)`, kuri grąžintų sąrašą su kiekvieno skaičiaus kvadratu.

### Testai:
```python
print(pakelk_kvadratu(2, 3, 4))  # [4, 9, 16]
print(pakelk_kvadratu())         # []
```

### Atsakymai:
```
[4, 9, 16]
[]
```

---

##  4. Parodyk perduotus `**kwargs`

**Užduotis:**  
Sukurk funkciją `rodyk_argumentus(**kwargs)`, kuri kiekvieną raktą ir reikšmę išspausdintų naujoje eilutėje formatu `raktas: reikšmė`.

### Testai:
```python
rodyk_argumentus(vardas="Jonas", amzius=30)
```

### Atsakymas:
```
vardas: Jonas
amzius: 30
```

---

##  5. Padaugink su `*args` ir pridėk žinutę su `**kwargs`

**Užduotis:**  
Sukurk funkciją `padaugink_ir_rasyk(sk, *args, **kwargs)`, kuri:
- Padaugina kiekvieną `*args` skaičių iš `sk`
- Išspausdina rezultatą kartu su žinute `text` iš `**kwargs`
- Jei `text` nėra pateikta – naudok "Rezultatas:"

### Testai:
```python
padaugink_ir_rasyk(2, 3, 4, 5)
padaugink_ir_rasyk(3, 1, 2, text="Dauginta:")
```

### Atsakymai:
```
Rezultatas: 6
Rezultatas: 8
Rezultatas: 10

Dauginta: 3
Dauginta: 6
```

---

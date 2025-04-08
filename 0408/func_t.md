### **Paskaita: Funkcijos – pažangi dalis**

#### **Įvadas į `*args` ir `**kwargs`**
Pažengusios funkcijų naudojimo galimybės apima galimybę priimti kintamą kiekį argumentų, naudojant `*args` ir `**kwargs`. Tai suteikia didelį lankstumą kuriant funkcijas, kurios gali priimti įvairų skaičių argumentų be iš anksto nustatyto kiekio.

---

#### **1. `*args` naudojimas funkcijose**
`*args` leidžia funkcijai priimti nežinomą skaičių pozicinių argumentų, kurie yra supakuojami į tuple. Tai leidžia naudoti funkciją su bet kokiu argumentų kiekiu.

```python
def print_args(*args):
    print(args)
    print(type(args))

print_args("Adomas", "sausis", 1000)
```

**Apibendrinimas:**  
Naudodami `*args`, galime perduoti nežinomą kiekį argumentų funkcijai, kuri juos priims ir apdoros kaip tuple.

---

#### **2. Funkcija su daugybe vardų**
Galima naudoti `*args`, kad funkcija dirbtų su įvairiais vardais, formuodama rezultatus iš daugelio argumentų.

```python
def give_hello_to_names(*args):
    res = ""
    for name in args:
        res += f"Hello {name}\n"
    return res

print(give_hello_to_names("Ram", "Adomas", "Valdas"))
```

**Apibendrinimas:**  
Ši funkcija suformuoja pasisveikinimus su kiekvienu vardu, kuris buvo perduotas per `*args`, parodant, kaip galima dirbti su kintamu argumentų kiekiu.

---

#### **3. Argumentų derinimas su `*args`**
`*args` gali būti derinamas su kitais argumentų tipais. Tai leidžia naudoti ir pozicinius argumentus, kartu su kintamu kiekiu papildomų argumentų.

```python
def multiply_all_by_numb(numb, *args):
    for elem in args:
        print(elem * numb)

multiply_all_by_numb(7, 10, 11, 50)
```

**Apibendrinimas:**  
Čia matome, kaip `*args` galima derinti su poziciniais argumentais, kad būtų galima valdyti tiek fiksuotus, tiek kintamus duomenis vienoje funkcijoje.

---

#### **4. Kelių argumentų tipų derinimas**
Kombinuojant paprastus argumentus, `*args`, ir vardinius argumentus (keyword arguments), galima sukurti labai lankstų funkcijų dizainą.

```python
def multiply_all_by_numb(numb, *args, text="* DAUGYBA"):
    for elem in args:
        print(f"{elem * numb} {text}")

multiply_all_by_numb(7, 10, 11, 50)
multiply_all_by_numb(7, 10, 11, 50, text="***")
```

**Apibendrinimas:**  
Vardinių argumentų (`keyword arguments`) ir `*args` derinimas leidžia funkcijai priimti įvairius argumentus ir juos tvarkyti efektyviai.

---

#### **5. Rezultatų grąžinimas naudojant `*args`**
Funkcija gali apdoroti `*args` argumentus ir grąžinti suformuotą rezultatą, pavyzdžiui, sąrašą daugybos rezultatų.

```python
def return_list_of_multiplied_numbs(numb, *args, info=False):
    multiplied_numbs = [elem * numb for elem in args]
    if info:
        print(f"daugiklis: {numb}, args: {args}, rezultatas: {multiplied_numbs}")
    return multiplied_numbs

res = return_list_of_multiplied_numbs(7, 10, 11, 50)
print(res)  # [70, 77, 350]

res = return_list_of_multiplied_numbs(3, 10, 11, 50, info=True)  # daugiklis yra: 3 *args yra: (10, 11, 50) rezultatas yra: [30, 33, 150]
print(res)  # [30, 33, 150]
```

**Apibendrinimas:**  
Ši funkcija ne tik priima kintamą kiekį argumentų, bet ir grąžina rezultatą kaip sąrašą, parodydama, kaip galima manipuliuoti perduotais argumentais ir grąžinti apdorotus duomenis.

---

Šioje paskaitos dalyje nagrinėjome `*args` naudojimo galimybes, įskaitant jo kombinavimą su kitais argumentų tipais ir jų lankstumą perduodant įvairų argumentų kiekį į funkcijas.

---
#### **1. Įvadas į `**kwargs`**
`**kwargs` naudojamas funkcijose, kai norima priimti iš anksto nežinomą kiekį vardinių argumentų (keyword arguments). Vardiniai argumentai paverčiami į žodyną (dict), kur raktai yra argumentų pavadinimai, o reikšmės – perduotos reikšmės. Tai suteikia didelį lankstumą priimant ir apdorojant funkcijas su įvairiais keyword argumentais.

---

#### **2.  `**kwargs` mechanizmas**
Kai funkcija priima kintamą kiekį vardinių argumentų ir jų reikšmių per `**kwargs`, jie yra supakuojami į žodyną.

```python
def print_kwargs(**kwargs):  # ** - pakavimas į žodyną, kintamajame kwargs
    print(kwargs)
    print(type(kwargs))


print_kwargs(pirmas=1, antras=2)  # {'pirmas': 1, 'antras': 2} <class 'dict'>
```

**Apibendrinimas:**  
Funkcija `print_kwargs` priima nežinomą kiekį vardinių argumentų ir juos supakuoja į žodyną. Naudojant `**kwargs`, galima perduoti įvairius parametrus į funkciją ir juos apdoroti dinamiškai.

---

#### **3. `**kwargs` su numatytaisiais argumentais**
Naudojant `**kwargs` vietoje atskirų keyword argumentų, galima patogiau perduoti keyword argumentus svetimai funkcijai, kurią mes kviečiame savojoje funkcijoje.
Pirma funkcija nesinaudoja `**kwargs` ir kuria savo keyword argumentus, kad juos po to perduotų print(svetimai) funkcijai jos keyword argumentus `sep` ir `end`. Matome kaip tai nepatogu.

```python
def print_list(listas, skirtukas=" ", eilutes_pabaiga="\n"):
    for elem in listas:
        print(elem, "mėn.", sep=skirtukas, end=eilutes_pabaiga)

listas_duom = ['sausis', 'vasaris', 'kovas']
print_list(listas_duom)
print_list(listas_duom, skirtukas="|||", eilutes_pabaiga="***\n")
```
Vienas iš pagrindinių `**kwargs` naudojimo būdų yra perduoti iš funkcijos į kitą funkciją tam tikrus keyword argumentus. Šiame pavyzdyje perdarom ankstesnę funkciją ir `**kwargs` yra naudojamas kaip būdas perduoti parametrus į `print` funkciją.

```python
def print_list(listas, **kwargs):   # kwargs panaudosim print funkcijos keyword argumentams
    for elem in listas:
        print(elem, "mėn.", **kwargs)  # kwargs žodynas išpakuojamas į keyword argumentus

print_list(listas_duom)
print_list(listas_duom, sep=">>>")
print_list(listas_duom, sep=">>>", end="---")
```

**Apibendrinimas:**  
Naudodami `**kwargs`, galime lengvai perduoti keyword argumentus į kitą funkciją, tokią kaip `print`. Tai labai naudinga, kai norime perduoti daug argumentų arba kai nežinome visų argumentų iš anksto.

---

#### **5. Nereikalingų argumentų sugėrimas naudojant `**kwargs`**
Kartais naudojamas `**kwargs`, kai norime, kad funkcija priimtų ir ignoruotų nereikalingus argumentus. Tai yra patogus būdas neleisti funkcijai sugriūti dėl nenumatytų argumentų.

```python
def kelk_laipsniu(sk, laipsnis=2, **kwargs):
    res = sk ** laipsnis
    return res

kelk_laipsniu(2, laipsnis=3, radianas=2)  # radianas yra nenumatytas parametras, jį sugeria kwargs
```

**Apibendrinimas:**  
Naudojant `**kwargs`, galima "sugerti" ir ignoruoti nenumatytus argumentus, kurie kitaip gali crashinti funkciją. Tai suteikia galimybę funkcijoms priimti papildomus argumentus, kurių jos nebūtinai naudos.

---
#### **Įvadas į lambda funkcijas**
Lambda funkcijos, dar vadinamos anoniminėmis funkcijomis, yra paprastos vienos eilutės funkcijos be pavadinimo. Jų pagrindinė paskirtis – naudoti kartu su kitomis funkcijomis, kurios jas priima kaip argumentą, tokiose situacijose kaip rūšiavimas, filtravimas ar map'inimas.

---

#### **1. Lambda funkcijos ir rūšiavimas**
Šiame pavyzdyje pateikiami darbuotojų duomenys, kuriuos galima rūšiuoti naudojant įprastą funkciją arba lambda funkciją. Pirmiausia parodytas rūšiavimas pagal numatytąją tvarką, o tada – rūšiavimas pagal funkciją ir lambda.

```python
darbuotojai = [
    ['Valdas', 'programuotojas', 2000],
    ['Adomas', 'direktorius', 3000],
    ['Aldona', 'vadybininkas', 1800],
    ['Jogaila', 'programuotojas', 2500]
]

# Rūšiavimas pagal pirmąjį elementą (vardą) – numatytoji rūšiavimo tvarka
res = sorted(darbuotojai)
print(res)
```

**Apibendrinimas:**  
Pagal numatytąją rūšiavimo tvarką, sąrašas yra rikiuojamas pagal pirmąjį elementą kiekvienoje vidinėje struktūroje (vardą). Tai yra natūralus būdas rikiuoti string'ų sąrašus.

---

#### **2. Rūšiavimas naudojant paprastą funkciją**
Galime kurti funkcijas, kurios leidžia atlikti rūšiavimą pagal specifinius sąrašo elementus, pavyzdžiui, pagal profesiją ar atlyginimą.

```python
def grazink_index_1(listas):
    return listas[1]  # grąžina profesiją

res = sorted(darbuotojai, key=grazink_index_1)
print(res)
```

**Apibendrinimas:**  
Funkcija `grazink_index_1` leidžia rūšiuoti sąrašą pagal antrąjį elementą (profesiją). Tai rodo, kaip sukurti paprastas funkcijas, kurios naudojamos kaip rūšiavimo `key` argumentai.

---

#### **3. Rūšiavimas naudojant lambda funkciją**
Tas pats rūšiavimas gali būti atliktas daug greičiau naudojant lambda funkciją, kuri veikia kaip anoniminė vienos eilutės funkcija.

```python
res = sorted(darbuotojai, key=lambda listas: listas[-1])  # rūšiavimas pagal atlyginimą
print(res)
```

**Apibendrinimas:**  
Naudodami lambda funkciją, galime greitai apibrėžti rūšiavimo kriterijų be atskiros funkcijos kūrimo. Šiuo atveju rūšiuojama pagal paskutinį elementą (atlyginimą), ir lambda funkcija leidžia tai padaryti greitai bei efektyviai.
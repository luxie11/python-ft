## **Paskaita: Objektinis programavimas – Klasės, Instancijos, Metodai, ir Objektų Valdymas**

---

### **Įvadas:**  
Objektinis programavimas (OOP) yra programavimo paradigma, kuri remiasi objektais ir jų sąveika. Pagrindiniai OOP principai apima inkapsuliaciją, paveldimumą ir polimorfizmą. Objektais laikomos klasės instancijos, kurios turi savybes (laukus) ir metodus (funkcijas). Šioje paskaitoje apžvelgsime klasių kūrimą, jų instancijų kūrimą, laukų ir metodų naudojimą bei kaip valdyti objektų grupes naudojant sąrašus.

---

### **1. Klasės kūrimas ir statiniai laukai**

Objektiniame programavime klasė yra šablonas, pagal kurį kuriami objektai (instancijos). Klasėje apibrėžiami atributai (laukeliai) ir metodai, kurie bus bendri visiems tos klasės objektams. Šiame pavyzdyje sukuriama `House` klasė su statiniu atributu `country`, kuris bus bendras visoms klasės instancijoms.

```python
class House:
    country = "LT"

print(House.country)  # LT
```

**Apibendrinimas:**  
Čia sukuriame `House` klasę ir apibrėžiame statinį lauką `country`, kuris turi reikšmę "LT". Statiniai laukai yra bendri visoms klasės instancijoms – tai reiškia, kad visi `House` objektai turės tą pačią `country` reikšmę.

---

### **2. Konstruktorius `__init__` ir instancijos laukų inicializavimas**

Konstruktorius `__init__` yra specialus metodas, kuris automatiškai iškviečiamas, kai kuriama nauja klasės instancija. Šiame konstruktoriuje apibrėžiami specifiniai laukeliai, kurie bus priskiriami kiekvienai klasei atskirai.

```python
class House:
    country = "LT"

    def __init__(self, price, year):
        self.price = price
        self.year = year
```

**Apibendrinimas:**  
Konstruktorius leidžia inicializuoti instancijos laukus, tokius kaip `price` ir `year`. Kiekvienai instancijai šie laukai gali turėti skirtingas reikšmes, o konstruktoriaus pagalba tie laukai yra priskiriami instancijai jos sukūrimo metu.

---

### **3. Statinio lauko ir instancijų naudojimas**

Kai klasė yra sukurta, mes galime naudoti statinius ir instancijų laukus. Pavyzdžiui, galima prieiti prie statinio lauko tiesiai per klasės pavadinimą, o prie instancijų laukų – per konkrečią instanciją.

```python
print(House.country)  # LT

house_instance_1 = House(10_000, 1990)
print(house_instance_1.price)  # 10000
print(house_instance_1.year)  # 1990

house_instance_2 = House(12_000, 1920)
print(house_instance_2.price)  # 12000
print(house_instance_2.year)  # 1920
```

**Apibendrinimas:**  
Naudojant `House.country`, mes prieiname prie statinio lauko `country`, kuris yra bendra visoms klasės instancijoms. Kuriant naujas klasės instancijas, mes inicializuojame jų laukus `price` ir `year`, kurie gali skirtis tarp skirtingų objektų.

---

### **4. Klasės instancijų atvaizdavimas**

Kiekviena sukurta klasės instancija gali būti atvaizduojama kaip unikalus objektas su savo vieta atmintyje. Tačiau be papildomo metodo, klasės instancijos išvedamos kaip atminties adresas.

```python
print(house_instance_1)  # <__main__.House object at 0x000001FDB47DB850>
print(house_instance_2)  # <__main__.House object at 0x000001FDB47DB790>
```

**Apibendrinimas:**  
Kai klasės instancija spausdinama, ji pagal nutylėjimą pateikia informaciją apie savo atminties vietą, kuri yra unikali kiekvienam objektui. Norint gauti prasmingesnį rezultatą, reikėtų aprašyti specialų metodą, pvz., `__str__` arba `__repr__`, kuris grąžintų aiškų objekto atvaizdavimą.

---

### **5. Savų metodų kūrimas klasėje**

Objektuose esančiuose metoduose galima atlikti tam tikrus veiksmus su objekto laukais. Šiame pavyzdyje sukuriame metodą `get_age`, kuris apskaičiuoja namo amžių pagal dabartinius metus ir `year` lauką.

```python
import datetime

class House:
    country = "LT"

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        now = datetime.datetime.today()
        current_year = now.year
        return current_year - self.year
```

**Apibendrinimas:**  
Šio metodo dėka, kiekvienas `House` objektas gali apskaičiuoti savo amžių, naudodamas dabartinę datą ir `year` lauką. Metodas `get_age` yra priskirtas kiekvienai `House` klasei ir gali būti iškviestas kiekvienai instancijai atskirai.

---

### **6. Metodų iškvietimas ir rezultatų naudojimas**

Kai metodas yra sukurtas klasėje, jį galima iškviesti per bet kurią klasės instanciją. Tai leidžia atlikti veiksmus su konkretaus objekto duomenimis.

```python
house_instance_1 = House(10_000, 1990)
age = house_instance_1.get_age()
print(age)  # 34

house_instance_2 = House(12_000, 1920)
print(house_instance_2.get_age())  # 104
```

**Apibendrinimas:**  
Naudodami `get_age` metodą, galime apskaičiuoti ir atspausdinti namo amžių pagal instancijos duomenis. Kiekviena instancija gali turėti skirtingus `year` laukus, todėl metodo rezultatai bus unikalūs kiekvienam objektui.

---

### **7. `__str__` metodas – Objektų atvaizdavimo valdymas**

Kai metodas `__str__` yra apibrėžtas, jis automatiškai naudojamas, kai bandome išvesti objektą su `print()` funkcija. Šiame pavyzdyje vietoje objekto atminties adreso išvedamas aiškus objekto aprašymas.

```python
class House:
    country = "LT"

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        now = datetime.datetime.today()
        current_year = now.year
        return current_year - self.year

    def __str__(self):
        return f"Namas {self.year} pastatymo, kaina - {self.price}, amžius - {self.get_age()}"
```

**Apibendrinimas:**  
`__str__` metodas suteikia galimybę nurodyti, kaip objektas turėtų būti pateikiamas tekstiniu formatu. Jis grąžina aiškų ir suprantamą tekstą, kuriame pateikiami reikalingi laukai bei metodų rezultatai.

---

### **8. Objektų grupių valdymas naudojant sąrašus**

Objektinio programavimo metu dažnai reikia dirbti ne tik su pavieniais objektais, bet ir su jų grupėmis. Vienas iš būdų tai padaryti – naudoti Python sąrašus (list). Šiame pavyzdyje talpiname kelias `House` klases į sąrašą ir atliekame veiksmus su jų duomenimis.

```python
house1 = House(22_000, 1980)
house2 = House(12_000, 1970)
house3 = House(33_000, 2000)

houses = [house1, house2, house3]
print(houses)

for house in houses:
    print(house)
```

**Apibendrinimas:**  
Objektus galima sutalpinti į sąrašą ir vėliau atlikti iteracijas per jį. Tai suteikia galimybę apdoroti daugelį objektų vienu metu. Kai naudojamas `print(house)`, iškviečiamas `__str__` metodas, todėl kiekvienas objektas bus išvedamas aiškiai.

---

### **9. Objektų laukų keitimas iteruojant per sąrašą

**

Šiame pavyzdyje iteruojame per objektų sąrašą ir keičiame kiekvieno objekto lauką – kainą, padidindami ją 21%.

```python
for house in houses:
    print(f"sena kaina: {house.price}")
    house.price = round(house.price * 1.21)
    print(f"nauja kaina: {house.price}")

print(house1)
```

**Apibendrinimas:**  
Iteruojant per sąrašą, galime keisti kiekvieno objekto laukus. Šiuo atveju keičiame `price` lauką, padidindami jį 21%. Pokyčiai taikomi visiems objektams sąraše, todėl po kiekvieno keitimo turime atnaujintus duomenis.

---

### **10. Objektų pridėjimas į sąrašą naudojant vartotojo įvestį**

Šiame pavyzdyje sukuriame tuščią sąrašą ir leidžiame vartotojui įvesti duomenis apie naujus namus. Kiekvienas įvestas namas pridedamas į sąrašą, kuris vėliau išvedamas.

```python
houses_kaupiklis = []
while True:
    quit_choice = input("įveskite bet kokį simbolį kad išeiti Enter, tęsti įvedimą")
    if quit_choice:
        break

    year = int(input("Įveskite metus "))
    price = int(input("Įveskite kainą "))

    house_instance = House(price, year)
    houses_kaupiklis.append(house_instance)

    print("Spausdinam ką sukaupėm")
    for house in houses_kaupiklis:
        print(house)
```

**Apibendrinimas:**  
Naudojant `while` ciklą ir sąrašą, galima kaupti vartotojo įvestus duomenis ir kiekvieną kartą sukurti naują `House` instanciją. Šis metodas leidžia dinamiškai pridėti naujus objektus į sąrašą ir vėliau juos peržiūrėti.

---

### **Išvados:**  
Šiame konspekte sužinojome, kaip naudoti objektinį programavimą Python kalboje, sukuriant klases, inicializuojant instancijas ir naudojant metodus. Be to, aptarėme, kaip efektyviai valdyti objektų grupes naudojant sąrašus, juos modifikuoti ir pridėti naujus objektus.
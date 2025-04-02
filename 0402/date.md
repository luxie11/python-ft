### **Paskaita: `datetime` modulis ir laiko valdymas**

---

### **1. `datetime` klasė ir datos-laiko skaičiavimai**

**Įžanga:**  
Šioje dalyje apžvelgsime `datetime` modulį ir jo naudojimą su datomis ir laiku. Naudosime `datetime` klasę, esančią `datetime` modulyje, norint manipuliuoti datos ir laiko objektais, juos išskaidyti į sudedamąsias dalis bei atlikti skaičiavimus, pavyzdžiui, nustatyti laiko skirtumus tarp dviejų datų.

---

#### **Dabartinės datos-laiko gavimas**

```python
import datetime

print(type(datetime))  # <class 'module'>

# kreipiamės į funkcionalumą aprašytą datetime faile
# todėl kode 2 kartus kartojam datetime
# antrasis datetime yra kreipimasis į klasę
# .today() metodas sukuria šio laiko momento datos-laiko objektą
# rezultatas yra datetime.datetime objektas
dt_res = datetime.datetime.today()
print(dt_res)  # 2024-10-10 10:33:24.596796
print(type(dt_res))  # <class 'datetime.datetime'>
```

**Apibendrinimas:**  
Naudodami `datetime.datetime.today()`, gauname dabartinę datą ir laiką kaip `datetime` objektą. Šis objektas saugo tiek datą, tiek laiką ir gali būti naudojamas vėlesniems skaičiavimams ar operacijoms.

---

#### **Atskiri datos-laiko laukai iš `datetime` objekto**

```python
# datetime.datetime objektas turi savybes(laukus)
# į kuriuos galima kreiptis, jie saugo atskiras datos-laiko
# sudedamąsias dalis(keisis vis išnaujo paleidus, nes ėmėm šio momento datą laiką)
res_year = dt_res.year
print(res_year)  # 2024
print(type(res_year))  # <class 'int'>

print(dt_res.month)
print(dt_res.day)
print(dt_res.hour)
print(dt_res.minute)
print(dt_res.second)
print(dt_res.microsecond)
```

**Apibendrinimas:**  
`datetime` objektai turi įvairias savybes, kurios leidžia pasiekti atskiras datos ir laiko dalis, tokias kaip metai, mėnuo, diena ir kt. Šios savybės grąžina sveikus skaičius, kurie atitinka tam tikrą datos arba laiko elementą.

---

#### **Norimos datos ir laiko objekto sukūrimas**

```python
# patys sukuriam norimos datos ir laiko objektą
# pilnai užpildome datos ir laiko laukus
my_datetime = datetime.datetime(2011, 12, 31, 23, 59, 59)
print(my_datetime)  # 2011-12-31 23:59:59

# laiką paduoti nebūtina, užtenka datos
my_datetime = datetime.datetime(2000, 1, 1)
print(my_datetime)  # 2000-01-01 00:00:00
```

**Apibendrinimas:**  
Kuriant `datetime` objektą, galima nurodyti tik datą arba kartu ir laiką. Jei laiko dalis nepateikiama, ji automatiškai nustatoma kaip 00:00:00. Tai leidžia lanksčiai dirbti su norima data ir laiku.

---

#### **Laiko skirtumo tarp datų skaičiavimas**

```python
# mes galim daryti paskaičiavimus su datos-laiko objektais
# pvz gauti laiko skirtumą tarp datų
time_from_2000 = datetime.datetime.today() - my_datetime
print(time_from_2000)  # 9049 days, 13:43:49.111984
```

**Apibendrinimas:**  
`datetime` objektai leidžia atlikti skaičiavimus tarp datų. Pavyzdžiui, galima apskaičiuoti skirtumą tarp dviejų datų, o rezultatas rodomas kaip dienų, valandų, minučių ir sekundžių intervalas.

---

### **2. Datos ir laiko formatavimas – įvestis ir išvestis**

**Įžanga:**  
Šioje dalyje apžvelgsime, kaip galime patys nustatyti specialius datos ir laiko formatus, kai duomenys yra įvedami į arba išvedami iš `datetime` objekto. Nors dažniausiai su datomis dirbama naudojant skaičius (`int`), šiame pavyzdyje sužinosime, kaip formuoti duomenis naudojant `str` formatą ir specialias kaukes.

---

#### **Datos ir laiko įvedimas naudojant `str` formatą**

```python
# ĮVESTIS
# sukursime savo ivesties formatą, naudojant kaukes - formato apibrėžimui
# ir str - įvesčiai
# .strptime - metodas naudoja kaukes, duomenų atpažinimui - https://strftime.org/
ivestis = "2020-02-11"
my_datetime = datetime.datetime.strptime(ivestis, "%Y-%m-%d")
print(my_datetime)

ivestis = "2020.02.15, 10:11:59"
my_datetime = datetime.datetime.strptime(ivestis, "%Y.%m.%d, %H:%M:%S")
print(my_datetime)
```

**Apibendrinimas:**  
Naudojant `strptime` metodą ir specialias kaukes, galime sukurti `datetime` objektą iš formato tekstinio įvesties (`str`). Kaukės leidžia atpažinti skirtingas datos ir laiko dalis, tokias kaip metai, mėnuo, diena, valanda ir pan.

---

#### **Datos ir laiko išvedimas naudojant `strftime` formatą**

```python
# IŠVESTIS,
# taip pačiai sudaroma kaukė, tačiau naudojamas kitas metodas,
# įvesties nepateikiama, naudojamas jau sukurtas datetime objektas
# strftime metodas
print(my_datetime)  # 2020-02-15 10:11:59
print(my_datetime.strftime("%d %m %Y"))  # 15 02 2020
print(my_datetime.strftime("%d %B %Y"))  # 15 February 2020
```

**Apibendrinimas:**  
Naudodami `strftime` metodą ir kaukes, galime suformuoti ir išvesti datas ar laiką formatuotu būdu, pavyzdžiui, nurodydami mėnesį pavadinimo formatu arba išvedant tam tikra tvarka dieną, mėnesį ir metus.

---

### **3. Laiko skirtumo (`timedelta`) objektai**

**Įžanga:**  
Šioje dalyje apžvelgsime, kaip dirbti su laiko skirtumo objektais – `timedelta`. Tai specialus `datetime` modulyje esantis objektas, kuris leidžia atlikti skaičiavimus su laiko intervalais. Mes galime apskaičiuoti skirtumus tarp dviejų datų ar laiko momentų ir atlikti įvairius laiko intervalų skaičiavimus.

---

#### **Laiko skirtumo (`timedelta`) objekto gavimas atliekant datų atimtį**

```python
dabar = datetime.datetime.today()
mileniumas = datetime.datetime(2000, 1, 1)

# padarius atimtį datos-laiko iš datos-laiko, gaunamas kitas objektas
# laiko skirtumo(laiko tarpo) objektas datetime.timedelta
skirtumas = dabar - mileniumas
print(skirtumas)
print(type(skirtumas))  # <class 'datetime.timedelta'>
```

**Apibendrinimas:**  
Atimant vieną `datetime` objektą iš kito, gauname `timedelta` objektą, kuris rodo skirtumą tarp šių dviejų datų ar laikų. Šis skirtumas gali būti pateikiamas dienomis, valandomis, minutėmis ir sekundėmis.

---

#### **Skaičiavimai su `timedelta` objektais**

```python
# laiko skirtumo objektą mes galim pridėti arba atimti iš datos laiko,
# gaudami kitą datetime objektą
# skaičiavimams dažniausiai patogiau sudaryti naują timedelta objektą,
# iškvietus jo klasę
skirtumas = datetime.timedelta(hours=1000)
print(skirtumas)
res = dabar + skirtumas
print(res)

skirtumas = datetime.timedelta(days=1000, hours=100, minutes=100)
print(skirtumas)
res = dabar - skirtumas
print(res)
```

**Apibendrinimas:**  
Galima pridėti arba atimti `timedelta` objektus prie arba

 iš `datetime` objektų, taip apskaičiuojant naujas datas ar laikus. Tai leidžia atlikti įvairius laiko intervalų skaičiavimus, pavyzdžiui, pridėti ar atimti dienas, valandas ar minutes nuo esamos datos.

---

#### **`timedelta` objekto laukų prieiga**

```python
# SVARBU! timedelta objekto laukai
print(skirtumas.days)  # dienomis
print(skirtumas.seconds)  # valandinė dalis atlikusi nuo dienų
print(skirtumas.seconds / 60 / 60)  # seconds valandomis

# VISOS laiko tarpo sekundės
sekundes = skirtumas.total_seconds()
print(sekundes)
```

**Apibendrinimas:**  
`timedelta` objektai turi specifinius laukus, tokius kaip `.days` ir `.seconds`, kurie leidžia gauti laikotarpius tam tikrais vienetais. Metodas `total_seconds()` grąžina viso intervalo sekundes, įskaitant visas dienas ir valandas.
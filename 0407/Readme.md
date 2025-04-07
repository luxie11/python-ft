### **Paskaita: Importai ir moduliai**

#### **Įvadas į importus ir modulius**
Modulių importavimas leidžia pridėti išorinį kodą į savo programą, nesikartojant ir neperrašant jau esamų funkcijų ar kodo fragmentų. Tai gali būti tiek Python bibliotekos, tiek jūsų pačių sukurti moduliai, kurie yra pasiekiami per importavimo mechanizmą.

---

#### **1. Paprastas importavimas**
Importuojant modulį, galime naudoti modulio pavadinimą ir pasiekti jo funkcijas ar klases per taško operatorių.

```python
import random

atsitiktinis_skaicius = random.randint(1, 10)
print(f"Atsitiktinis int skaičius nuo 1 iki 10: {atsitiktinis_skaicius}")
```

**Apibendrinimas:**  
Naudojant paprastą importą, pasiekiame visą modulį ir naudojame taško operatorių, kad iškviečiame reikalingas funkcijas ar duomenis.

---

#### **2. Specifinių funkcijų importavimas**
Galime importuoti tik tas funkcijas ar klases, kurios yra reikalingos, taip sumažindami kodą ir nereikalaudami naudoti taško operatoriaus.

```python
from random import randint, choice

atsitiktinis_skaicius = randint(1, 10)
atsitiktinis_elementas = choice(["sausis", "vasaris", "kovas"])
```

**Apibendrinimas:**  
Specifinių funkcijų importavimas leidžia tiesiogiai naudoti funkcijas be modulio pavadinimo, taip supaprastinant kodą.

---

#### **3. Modulio trumpinimas naudojant alias**
Galime suteikti modulio pavadinimui sutrumpinimą, kad išvengtume ilgesnių pavadinimų.

```python
import random as rn

atsitiktinis_skaicius = rn.randint(20, 25)
atsitiktinis_elementas = rn.choice(["sausis", "vasaris", "kovas"])
```

**Apibendrinimas:**  
Naudojant alias, moduliui suteikiame sutrumpintą vardą, kurį vėliau naudojame visoje programoje.

---

#### **4. Specifinių funkcijų importavimas su alias**
Galime ne tik importuoti specifines funkcijas, bet ir suteikti joms trumpesnius pavadinimus.

```python
from random import randint as rnt

atsitiktinis_skaicius = rnt(1, 10)
```

**Apibendrinimas:**  
Alias naudojimas suteikia galimybę dar labiau optimizuoti kodą ir naudoti trumpus, aiškius pavadinimus dažnai naudojamoms funkcijoms.

---

#### **5. Visko importavimas iš modulio (nerekomenduojamas būdas)**
Importuojant viską iš modulio, gauname prieigą prie visų jo funkcijų be pavadinimų, tačiau tai gali sukelti neaiškumų ir konfliktų.

```python
from random import *

parinktis = sample(["sausis", "vasaris", "kovas"], k=3)
print(parinktis)
```

**Apibendrinimas:**  
Šis būdas nėra rekomenduojamas, nes sunku kontroliuoti, kurios funkcijos ar kintamieji buvo importuoti, ir tai gali sukelti nenumatytų problemų.

---

Ši konspekto dalis pateikia pagrindinius importavimo būdus ir jų naudojimo privalumus bei trūkumus.

### **Importai iš mūsų sukurto modulio**

Modulių kūrimas leidžia kurti atskirus failus su funkcijomis ir logika, kuriuos galima importuoti į kitus projektus ar failus. Tai suteikia didesnį kodo modularumą ir leidžia organizuoti programą efektyviau.

---

#### **1. Visas modulio importavimas**
Importuodami visą modulį, naudojame taško operatorių, kad pasiektume jo funkcijas ar kitas struktūras.

```python
import aritmetikosmodulis

res = aritmetikosmodulis.dalink(10, 7)
print(res)

res = aritmetikosmodulis.daugink(10, 7)
print(res)

res = aritmetikosmodulis.atimk(10, 7)
print(res)

res = aritmetikosmodulis.sumuok(10, 7)
print(res)
```

**Apibendrinimas:**  
Visas modulio importavimas leidžia pasiekti visas jo funkcijas, bet kiekvieną kartą reikia naudoti modulio pavadinimą prieš funkciją.

---

#### **2. Specifinių funkcijų importavimas**
Galime importuoti tik reikiamas funkcijas iš modulio, taip sumažinant kodą.

```python
from aritmetikosmodulis import dalink, daugink

res = dalink(10, 7)
print(res)

res = daugink(10, 7)
print(res)
```

**Apibendrinimas:**  
Specifinių funkcijų importavimas leidžia tiesiogiai naudoti funkcijas be modulio pavadinimo, kas supaprastina kodą.

---

#### **3. Modulio trumpinimas naudojant alias**
Modulio vardą galime sutrumpinti, naudojant alias, kad nereikėtų rašyti ilgo pavadinimo.

```python
import aritmetikosmodulis as ar

res = ar.dalink(10, 7)
print(res)

res = ar.daugink(10, 7)
print(res)
```

**Apibendrinimas:**  
Alias naudojimas padeda efektyviai naudoti modulio funkcijas su trumpesniu pavadinimu, ypač kai modulis turi ilgesnį vardą arba dažnai naudojamas projekte.

---

Šis konspektas paaiškina, kaip importuoti ir naudoti mūsų pačių sukurtą modulį, pateikiant skirtingus importavimo variantus ir jų privalumus.

### **Importai iš folderio**

Kai modulis yra organizuotas kaip dalis projekto struktūros ir saugomas kataloge (folderyje), mes galime importuoti jį nurodydami modulio vietą. Tai leidžia efektyviai struktūrizuoti projektą, padalijant jį į modulius ir submodulius.

---

#### **1. Visas modulio importavimas iš folderio**
Importuodami modulį iš folderio, nurodome jo kelią per taško operatorių, kad pasiektume funkcijas.

```python
import mylib.aritmetika

res = mylib.aritmetika.sumuok(10, 7)
print(res)

res = mylib.aritmetika.atimk(10, 7)
print(res)
```

**Apibendrinimas:**  
Modulis, saugomas projekto folderyje, gali būti importuojamas nurodant jo kelią su taško operatoriumi. Tai suteikia prieigą prie visų funkcijų naudojant pilną modulio vardą.

---

#### **2. Specifinių funkcijų importavimas iš folderio**
Galime importuoti tik tam tikras funkcijas iš submodulio, kad sumažintume kodo sudėtingumą ir nereikėtų naudoti pilno pavadinimo.

```python
from mylib.aritmetika import dalink, daugink

res = dalink(10, 7)
print(res)

res = daugink(10, 7)
print(res)
```

**Apibendrinimas:**  
Specifinių funkcijų importavimas iš folderyje esančio modulio leidžia tiesiogiai naudoti reikalingas funkcijas be modulio kelio, supaprastinant kodą.

---

#### **3. Modulio trumpinimas naudojant alias**
Kaip ir su kitais moduliais, galime sutrumpinti modulio pavadinimą naudojant alias, kad būtų lengviau rašyti kodą.

```python
import mylib.aritmetika as ar

res = ar.sumuok(10, 7)
print(res)

res = ar.atimk(10, 7)
print(res)
```

**Apibendrinimas:**  
Naudodami alias, galime sutrumpinti modulio pavadinimą ir greičiau pasiekti funkcijas. Tai naudinga, kai modulis ar submodulis turi ilgą pavadinimą.

---

#### **4. Importavimas viso folderio**
Galime importuoti visą folderį kaip modulį ir pasiekti jo vidinius modulius su pilnu keliu.

```python
import mylib

res = mylib.aritmetika.sumuok(1, 5)
print(res)
```

**Apibendrinimas:**  
Importuojant visą folderį, mes pasiekiame jo viduje esančius modulius per pilną modulio kelią. Tai suteikia lankstumo, kai reikia valdyti didesnį projekto struktūros kiekį.

---

Šis konspektas apima importų iš folderių pagrindus, paaiškindamas, kaip naudoti modulius, esančius projekto struktūroje, ir įvairius importavimo būdus bei jų privalumus.
# Užduotys: Importai ir moduliai

Šiame skyriuje pateikiamos užduotys, padėsiančios įtvirtinti supratimą apie Python modulių importavimą, alias naudojimą, specifinių funkcijų importavimą ir darbo su savo moduliais praktiką.

---

##  1. Paprastas importavimas

**Užduotis:**  
Importuok `math` modulį ir išvesk apskaičiuotą kvadratinę šaknį iš skaičiaus 144, naudodamas `sqrt` funkciją.

 *Tikslas:* suprasti, kaip veikia bazinis importas.

---

##  2. Specifinių funkcijų importavimas

**Užduotis:**  
Iš `math` modulio importuok funkciją `pow` ir pakelk skaičių 5 trečiuoju laipsniu.

*Tikslas:* naudotis tik tomis funkcijomis, kurių reikia.

---

##  3. Importas su alias

**Užduotis:**  
Importuok `random` modulį su alias `rnd` ir naudok `rnd.randint(50, 100)` funkciją, kad sugeneruotum atsitiktinį skaičių.

*Tikslas:* išmokti naudoti sutrumpintus vardus ilgų pavadinimų moduliams.

---

## 4. Funkcijų importavimas su alias

**Užduotis:**  
Iš `random` modulio importuok `choice` funkciją su alias `ch` ir atsitiktinai pasirink vieną elementą iš sąrašo `["obuolys", "bananas", "kriaušė"]`.
 
*Tikslas:* naudoti aliastus funkcijoms dažnam naudojimui.

---

##  5. Sukurk ir importuok savo modulį

**Užduotis:**  
1. Sukurk naują failą `skaiciuotuvas.py`.
2. Jame aprašyk 4 funkcijas: `sudetis(a, b)`, `atimtis(a, b)`, `daugyba(a, b)`, `dalyba(a, b)`.
3. Kitoje programoje importuok visą modulį ir naudok funkcijas su taško operatoriumi.

 *Tikslas:* išmokti kurti ir naudoti nuosavus modulius.

---

##  6. Importuok tik reikiamas funkcijas iš savo modulio

**Užduotis:**  
Naudodamas ankstesnį `skaiciuotuvas.py` modulį, importuok tik `daugyba` ir `dalyba` funkcijas ir jas panaudok be modulio pavadinimo.

 *Tikslas:* efektyviai naudoti funkcijų importavimą iš savo modulio.

---

##  7. Importas iš folderio struktūros

**Užduotis:**  
1. Sukurk folderį `mylib`, o jame – failą `geometrija.py`.
2. `geometrija.py` faile sukurk funkcijas `apskritimo_plotas(r)` ir `trikampio_plotas(a, h)`.
3. Kitame faile importuok šias funkcijas ir išbandyk jas.

 *Tikslas:* įvaldyti modulių organizavimą projekto kataloge.

---

##  8. Blogos praktikos atpažinimas

**Užduotis:**  
1. Parašyk pavyzdinį kodą, kuriame naudojamas `from math import *`.
2. Paaiškink, kodėl toks importavimas gali būti pavojingas dideliuose projektuose.

 *Tikslas:* suprasti gerąsias praktikas ir išvengti klaidų.

---

 **Papildoma užduotis (iššūkis):**
Sukurk katalogą `tools`, jame laikyk 2 modulius: `tekstas.py` (su funkcija `skaiciuok_zodzius(tekstas)`) ir `failai.py` (su funkcija `nuskaito_faila(kelias)`). Sukurk programą, kuri nuskaitys `.txt` failą, apskaičiuos žodžių kiekį ir išves rezultatą.


#### Matematiniai Operatoriai

Python palaiko įvairias matematines operacijas, kurios leidžia atlikti skaičiavimus su skaičiais. Štai keletas pagrindinių matematinių operatorių ir kaip jie veikia:

1. **Sudėtis ir Atimtis**:

    ```python
    numb1 = 11
    numb2 = 2
    numb3 = 1.5

    # Sudėtis
    res = numb1 + numb2
    print(res)  # 13

    # Atimtis
    res = numb1 - numb2
    print(res)  # 9
    ```

    Sudėtis (`+`) ir atimtis (`-`) naudojamos skaičių sumavimui ir atimčiai. Šiuo atveju `11 + 2` duoda `13`, o `11 - 2` duoda `9`.

2. **Daugyba ir Dalyba**:

    ```python
    # Daugyba
    print(numb1 * numb2)  # 22

    # Dalyba
    print(numb1 / numb2)  # 5.5
    ```

    Daugyba (`*`) ir dalyba (`/`) leidžia padauginti ir padalinti skaičius. Pvz., `11 * 2` yra `22`, o `11 / 2` yra `5.5`.

3. **Dalyba iki sveiko skaičiaus ir Modulus**:

    ```python
    # Dalyba iki sveiko skaičiaus
    print(numb1 // numb2)  # 5
    print(numb1 // 7)  # 1
    print(numb1 // 99)  # 0

    # Modulus - dalybos liekana
    print(numb1 % 7)  # 4
    print(13 % 5)  # 3
    ```

    Dalyba iki sveiko skaičiaus (`//`) grąžina tik sveiką dalybos rezultatą, pvz., `11 // 2` yra `5`. Modulus (`%`) grąžina dalybos liekaną, pvz., `11 % 7` yra `4`.

#### Duomenų Tipai

Python turi keletą duomenų tipų, kurie yra svarbūs norint suprasti, kaip Python veikia su skirtingais duomenimis. Duomenų tipus Python nustato ir priskiria automatiškai.

1. **Pagrindiniai Duomenų Tipai**:

    ```python
    numb1 = 10
    numb2 = 1.5
    text = "Hello, world"

    # Skaičių tipai
    print(type(numb1))  # <class 'int'>
    print(type(numb2))  # <class 'float'>

    # Teksto tipas
    print(type(text))  # <class 'str'>
    ```

    Python turi kelis pagrindinius duomenų tipus: `int` (sveikieji skaičiai), `float` (skaičiai su kableliu) ir `str` (tekstai).

2. **Matematinės Operacijos su Skirtingais Tipais**:

    ```python
    # Matematinės operacijos tarp skirtingų tipų
    res = "100" + 1  # Tai sukels klaidą
    ```

    Skirtingų tipų (pvz., `str` ir `int`) negalima tiesiogiai naudoti matematinėse operacijose, nes tai sukels klaidą.

#### Tekstinė įvestis, duomenų tipo keitimas

1. **Input funkcija**:
    - Funkcija `input()` naudojama norint gauti duomenis iš vartotojo. Tačiau šie duomenys visuomet yra grąžinami kaip `str` (teksto) tipo duomenys, nepriklausomai nuo to, ar vartotojas įveda tekstą, ar skaičių.

   ```python
   user_input = input("Įveskite tekstą: ")
   print("Jūs įvedėte", user_input)
   ```

   Pirmoji kodo dalis prašo vartotojo įvesti tekstą, o įvestą informaciją išspausdina. Kadangi `input()` grąžina tekstinę eilutę, bet kokia vartotojo įvestis, įskaitant skaičius, bus laikoma eilutės formatu.

2. **Duomenų tipo keitimas**:
    - Jei norime atlikti matematines operacijas su vartotojo įvestimi, reikia šiuos tekstinius duomenis paversti į skaičius. Tam naudojamos `float()` arba `int()` funkcijos, priklausomai nuo to, kokio tipo skaičių reikia (slankiojo kablelio skaičius ar sveikasis).

    ```python
    user_input = input("Įveskite skaičių: ")
    input_to_int = float(user_input)
    res = input_to_int * 100
    print("Daugyba iš 100 yra:", res)
    ```

   Šiame kode vartotojo prašoma įvesti skaičių, tada naudojama `float()` funkcija, kuri konvertuoja tekstinę eilutę į `float`. Po to atliekama daugybos operacija, kurios rezultatas yra išspausdinamas.
   - Funkcija `float()` konvertuoja eilutę į skaičių su kableliu.
   - Funkcija `int()` konvertuoja eilutę į sveikąjį skaičių, tačiau veiks tik jei eilutė turi sveikąjį skaičių.


3. **Dažnos klaidos**:
   - Jei vartotojas įveda ne skaičių, o tekstą, naudojant `int()` arba `float()` funkcijas bus išmesta klaida. Todėl prieš atliekant konvertavimą būtina užtikrinti, kad įvestas teisingas formatas arba naudoti klaidų tvarkymo mechanizmus (pvz., `try-except`).

#### Stringų Indeksavimas

Stringų indeksavimas leidžia pasiekti atskirus simbolius ar jų sekas tekstuose.

1. **Indeksavimas**:

    Indeksavimas leidžia pasiekti specifinius simbolius stringe pagal jų poziciją. Teigiami indeksai skaičiuojami nuo stringo pradžios, o neigiami - nuo pabaigos.

    Štai kaip atrodo stringas "ABCDE" su teigiamais ir neigiamais indeksais:

    |   | A | B | C | D | E |
    |---|---|---|---|---|---|
    | Neigiamas indeksas | -5 | -4 | -3 | -2 | -1 |
    | Teigiamas indeksas | 0 | 1 | 2 | 3 | 4 |

    ```python
    text1 = "ABCDE"
    text2 = "Hello World"

    # Simbolių indeksavimas
    print(text1[0])  # A
    print(text1[2])  # C
    print(text1[4])  # E
    print(text1[-1])  # E
    print(text1[-2])  # D
    ```

    Stringas text2 = "Hello World" su teigiamais ir neigiamais indeksais:

    |   | H | e | l | l | o |   | W | o | r | l | d |
    |---|---|---|---|---|---|---|---|---|---|---|---|
    | Neigiamas indeksas | -11 | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |
    | Teigiamas indeksas | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |

2. **Slicing - iškarpos**:

    Slicing leidžia iškirpti stringo dalis naudojant pradžios ir pabaigos indeksus. Pvz., `text1[1:4]` grąžins `BCD`.

    ```python
    # Slicing
    print(text1[1:4])  # BCD
    print(text1[1:-1])  # BCD

    # Hello World pavyzdžiai
    print(text2[0:5])  # Hello
    print(text2[:5])  # Hello
    print(text2[6:])  # World
    print(text2[6:11])  # World
    print(text2[:7])  # Hello W
    print(text2[1:7])  # ello W
    ```

3. **Slicing su žingsniu**:

    Slicing taip pat galima naudoti su žingsniu (step), leidžiančiu praleisti tam tikrus simbolius. Pvz., `text2[1:10:2]` grąžins `el ol`, o `text2[::-1]` apverčia stringą.

    ```python
    # Slicing su žingsniu
    print(text2[1:10:1])  # ello Worl
    print(text2[1:10:2])  # el ol
    print(text2[::2])  # HloWrd
    print(text2[::-1])  # dlroW olleH
    ```

#### Stringų Metodai

Metodai tai yra funkcijos priklausančios tik tam tikriems duomenų tipams. Stringų metodai leidžia atlikti įvairias operacijas su tekstais. Kviečiant `str` metodus naudojamas `.` - taško operatorius.

1. **Didžiųjų Raidžių Konvertavimas**:

    `upper()` metodas konvertuoja visas stringo raides į didžiąsias raides.

    ```python
    text = "hello world"
    print(text)  # hello world

    # Konvertavimas į didžiąsias raides
    print(text.upper())  # HELLO WORLD

    # Originalus text išliks nepakitęs
    print(text)  # hello world

    # Išsaugom teksto pakeitimo rezultatą į kitą kintamąjį
    text_u = text.upper()
    print(text_u)  # HELLO WORLD
    ```

2. **Simbolių Pasikartojimų Skaičiavimas**:

    `count()` metodas suskaičiuoja, kiek kartų tam tikras simbolis ar simbolių seka pasikartoja stringe.

    ```python
    # Simbolių pasikartojimų skaičiavimas
    print(text.count("l"))  # 3
    print(text.count("ll"))  # 1
    ```

3. **Indekso Paieška**:

    `index()` metodas grąžina pirmojo nurodyto simbolio ar simbolių sekos atsiradimo indeksą stringe.

    ```python
    # Indekso paieška
    print(text.index("l"))  # 2
    print(text.index("world"))  # 6
    ```

4. **Indekso Paieška su `.find()`**:

    `find()` metodas panašus į `index()`, tačiau, jei simbolis ar simbolių seka nerandama, grąžina `-1` vietoj klaidos.

    ```python
    # Indekso paieška naudojant .find()
    print(text.find("l"))  # 2
    print(text.find("L"))  # -1 (nerasta)
    ```

5. **Simbolių Keitimas**:

    `replace()` metodas leidžia pakeisti nurodytus simbolius ar simbolių sekas kitais.

    ```python
    # Pakeitimas kitais simboliais
    text_w = text.replace("l", "w")
    print(text_w)  # hewwo worwd
    text_w = text_w.replace("w", "")
    print(text_w)  # heo ord
    ```

6. **Tarpų Pašalinimas**:

    `strip()` metodas pašalina tarpus ar kitus nurodytus simbolius iš stringo pradžios ir pabaigos, neliečiant vidurio.

    ```python
    # Tarpų pašalinimas
    text2 = "   Welcome class!!!    "
    text2 = text2.strip()
    print(text2)  # Welcome class!!!
    ```

#### f-string
1. **F-stringai**:
F-stringai Pythone yra specialia sintakse sudaromi `str` tipo tekstiniai duomenys, ši priemonė leidžia formatuoti tekstą lengvai ir patogiai. Duomenys prijungiami naudojant `{}` kaip žymę kintamiesiems.
    ```python
    # f-stringai formatuoti stringai, galintys priimti į
    # stringą bet kokius duomenis
    month = "sausis"
    day = 31
    ftext = f"Mėnesis yra {month}, diena {day}d."
    print(ftext)  # Mėnesis yra sausis, diena 31d.
    ftext = f"Mėnesis yra {month}, diena {day - 1}d."
    print(ftext)  # Mėnesis yra sausis, diena 30d.
    ```
Šis konspektas padės suprasti pagrindines Python operacijas su skaičiais ir tekstu bei jų naudojimo būdus.
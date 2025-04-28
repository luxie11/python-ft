```markdown
# SQL naudojimas Jupyter Notebook ir Db Browser SQLite

## Įvadas

Norint naudoti SQL Jupyter Notebook aplinkoje, reikia įdiegti papildomą modulį `ipython-sql`. Tai galima padaryti naudojant komandą:

```bash
pip install ipython-sql
```

Alternatyviai, SQL užklausas galima vykdyti naudojant Db Browser for SQLite arba bet kurią kitą SQL duomenų bazės valdymo sistemą.

## SQL plėtinio įkėlimas ir duomenų bazės prijungimas

Prieš pradedant darbą, reikia užkrauti SQL plėtinį ir prijungti duomenų bazę:

```python
%load_ext sql
%sql sqlite:///cars.db
```

Kiekvienai SQL užklausai reikia pridėti `%%sql` direktyvą, o Python komentarai šiame kontekste nėra leidžiami.

## Duomenų atrinkimas naudojant `SELECT`

### Filtravimas su `BETWEEN ... AND`

Šis filtras leidžia atrinkti reikšmes tam tikrame intervale, pvz., automobilius pagamintus tarp 1991 ir 1993 metų, kurių kaina viršija 20 000:

```sql
%%sql
SELECT * FROM cars WHERE year BETWEEN 1991 AND 1993 AND price > 20000;
```

### Filtravimas su `IN`

Galima filtruoti įrašus pagal konkretų reikšmių sąrašą, pvz., atrinkti automobilius, pagamintus konkrečiais metais:

```sql
%%sql
SELECT * FROM cars WHERE year IN (1995, 2000, 2001);
```

Arba atrinkti automobilius pagal gamintoją:

```sql
%%sql
SELECT * FROM cars WHERE make IN ("Audi", "Ford");
```

### Filtravimas su `LIKE`

Naudojamas, kai reikia ieškoti pagal dalinį atitikimą.

- `A%` – ieškos gamintojų, kurių pavadinimas prasideda A raide.
- `_e%` – ieškos gamintojų, kurių antra raidė yra `e`.

```sql
%%sql
SELECT * FROM cars WHERE make LIKE "A%";
```

```sql
%%sql
SELECT * FROM cars WHERE make LIKE "_e%";
```

### `NULL` reikšmės paieška

Jei norime atrinkti tik tas eilutes, kuriose spalvos stulpelis neturi reikšmės (`NULL`):

```sql
%%sql
SELECT * FROM cars WHERE color IS NULL;
```

### Kombinuotos sąlygos su `AND`, `OR`, `NOT`

- `AND` reikalauja, kad abi sąlygos būtų tenkinamos.
- `OR` reikalauja, kad bent viena sąlyga būtų tenkinama.
- `NOT` paneigia sąlygą.

```sql
%%sql
SELECT * FROM cars WHERE make = "Ford" AND price > 40000;
```

```sql
%%sql
SELECT * FROM cars WHERE make = "Ford" OR year > 2012;
```

```sql
%%sql
SELECT * FROM cars WHERE color NOT IN ("Violet", "Turquoise", "Crimson");
```

## Duomenų rikiavimas

### `ORDER BY`

Rikiuoti pagal kainą didėjančia tvarka:

```sql
%%sql
SELECT * FROM cars ORDER BY price;
```

Rikiuoti mažėjančia tvarka:

```sql
%%sql
SELECT * FROM cars ORDER BY price DESC;
```

### `COLLATE NOCASE` – neatsižvelgia į didžiąsias ir mažąsias raides

```sql
%%sql
SELECT * FROM cars WHERE make = "toyota" COLLATE NOCASE;
```

## Teksto operacijos

### Teksto sujungimas (`||` operatorius)

```sql
%%sql
SELECT "Gamintojas: " || make, model FROM cars;
```

Pervadinti sujungtą stulpelį naudojant `AS`:

```sql
%%sql
SELECT "Gamintojas: " || make AS "Gamintojas", model FROM cars;
```

## Skaičiavimai SQL užklausose

### Amžiaus apskaičiavimas

```sql
%%sql
SELECT make, model, 2022 - year AS "age" FROM cars;
```

### Kainos be PVM apskaičiavimas

```sql
%%sql
SELECT make, model, price, round(price / 1.21, 2) AS "be PVM" FROM cars;
```

## Grupavimas ir agregavimo funkcijos

Dažniausiai naudojamos grupavimo funkcijos:

- `AVG()` – vidurkis
- `COUNT()` – eilučių skaičius
- `MAX()` – didžiausia reikšmė
- `MIN()` – mažiausia reikšmė
- `SUM()` – suma

```sql
%%sql
SELECT MIN(price), MAX(price), AVG(price) FROM cars;
```

### Automobilių kiekis pagal gamintoją:

```sql
%%sql
SELECT make, count(*) FROM cars GROUP BY make;
```

### Brangiausios spalvos pagal didžiausią kainą:

```sql
%%sql
SELECT color, max(price), make, model FROM cars GROUP BY color ORDER BY price DESC;
```

## Sudėtingesnės užklausos su filtravimu ir grupavimu

Atrenkami brangiausi kiekvieno gamintojo automobiliai, išskyrus tam tikrus gamintojus:

```sql
%%sql
SELECT make, model, year, MAX(price) AS "maxas" FROM cars WHERE make NOT IN ("Toyota", "Mercury", "Volvo") GROUP BY make ORDER BY year;
```

Pridedame papildomą filtrą `HAVING`, kuris atrenka tik automobilius pigesnius nei 80 000:

```sql
%%sql
SELECT make, model, year, MAX(price) AS "maxas" FROM cars WHERE make NOT IN ("Toyota", "Mercury", "Volvo") GROUP BY make HAVING maxas < 80000 ORDER BY year;
```

## Išvados

- SQL leidžia efektyviai manipuliuoti duomenimis naudojant įvairius filtrus (`WHERE`, `IN`, `LIKE`, `BETWEEN` ir kt.).
- `ORDER BY` leidžia rikiuoti duomenis, o `GROUP BY` – atlikti grupavimo operacijas.
- Agregavimo funkcijos (`SUM`, `AVG`, `MAX`, `MIN`) padeda atlikti statistinius skaičiavimus.
- Kombinuotos sąlygos su `AND`, `OR`, `NOT` leidžia vykdyti sudėtingesnes užklausas.
- SQL sintaksė yra intuityvi, tačiau reikia atidžiai pasirinkti užklausų vykdymo eiliškumą.
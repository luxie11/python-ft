# Darbas su keliomis SQL lentelėmis

## Įvadas

Šiame projekte nagrinėjame, kaip dirbti su keliomis tarpusavyje susijusiomis SQL lentelėmis. Norint gauti reikalingus duomenis iš kelių lentelių, naudojame įvairius metodus, tokius kaip `JOIN` ir `WHERE` sąlygos. Tai leidžia efektyviai gauti ir analizuoti duomenis, naudojant įvairius filtrus ir grupavimus.

## Lentelių peržiūra

Norint peržiūrėti, kokios lentelės yra duomenų bazėje, galima naudoti šią SQL komandą:

```sql
SELECT name, sql FROM sqlite_master WHERE name NOT LIKE "sqlite%";
```

### Pvz., radome tris lenteles:
- `car`
- `company`
- `person`

## Duomenų peržiūra iš atskirų lentelių

Norint peržiūrėti duomenis iš atskirų lentelių, naudojame šias komandas:

```sql
SELECT * FROM person LIMIT 8;
```

```sql
SELECT * FROM car LIMIT 8;
```

```sql
SELECT * FROM company;
```

## Lentelių jungimas naudojant WHERE

Senesnis būdas sujungti lenteles yra naudojant `WHERE`. Pvz., sujungiame `person` ir `car` lenteles pagal `car_id` ir `id`:

```sql
SELECT * FROM person, car WHERE person.car_id=car.id;
```

Norėdami patikrinti, kurie žmonės neturi priskirtų automobilių:

```sql
SELECT * FROM person WHERE car_id IS NULL;
```

Sujungiame visas tris lenteles:

```sql
SELECT * FROM person, car, company
WHERE person.car_id=car.id AND person.company_id=company.id;
```

Norint gauti tik reikalingus stulpelius, naudojame šią sintaksę:

```sql
SELECT person.first_name, person.last_name, person.email, car.make, car.model, car.plate, company.name
FROM person, car, company
WHERE person.car_id=car.id AND person.company_id=company.id;
```

## Lentelių jungimas naudojant JOIN

Naudojant `JOIN`, galima aiškiau ir efektyviau jungti lenteles.

Pirmiausia sujungiame `person` ir `car` lenteles:

```sql
SELECT first_name, last_name, email, make, model, plate
FROM person
JOIN car ON person.car_id=car.id;
```

Galime rikiuoti pagal gamintoją:

```sql
SELECT first_name, last_name, email, make, model, plate
FROM person
JOIN car ON person.car_id=car.id
ORDER BY make;
```

Sujungiame visas tris lenteles ir rikiuojame pagal kompanijos pavadinimą:

```sql
SELECT first_name, last_name, email, make, model, plate, name
FROM person
JOIN car ON person.car_id=car.id
JOIN company ON person.company_id=company.id
ORDER BY name;
```

Filtruojame tik „Ford“ automobilius:

```sql
SELECT first_name, last_name, email, make, model, plate, name
FROM person
JOIN car ON person.car_id=car.id
JOIN company ON person.company_id=company.id
WHERE make="Ford"
ORDER BY name;
```

## Grupavimas ir skaičiavimai

Suskaičiuojame, kiek žmonių dirba kiekvienoje kompanijoje:

```sql
SELECT name, COUNT() AS "people"
FROM person
JOIN company ON person.company_id=company.id
GROUP BY name
ORDER BY people DESC;
```

Filtruojame kompanijas, kuriose dirba daugiau nei 3 žmonės:

```sql
SELECT name, COUNT() AS "people"
FROM person
JOIN company ON person.company_id=company.id
GROUP BY name
HAVING people > 3;
```

Suskaičiuojame, kiek automobilių priklauso kiekvienai kompanijai:

```sql
SELECT name, COUNT(person.car_id)
FROM person
JOIN company ON person.company_id=company.id
GROUP BY name;
```

Filtruojame tik tas kompanijas, kurios turi daugiau nei 2 automobilius:

```sql
SELECT name, COUNT() AS "autos"
FROM person
JOIN company ON person.company_id=company.id
JOIN car ON person.car_id=car.id
GROUP BY name
HAVING autos > 2
ORDER BY COUNT() DESC;
```

## JOIN variantai

### INNER JOIN

Standartinis jungimas, kai jungiamos tik atitinkančios eilutės iš abiejų lentelių:

```sql
SELECT * FROM person JOIN car ON person.car_id=car.id;
```

### LEFT JOIN

Iš kairės (`person`) lentelės pateikiamos visos eilutės, o iš dešinės (`car`) – tik tos, kurios turi atitikmenį:

```sql
SELECT first_name, last_name, email, make, model, plate
FROM person
LEFT JOIN car ON person.car_id=car.id
ORDER BY make;
```

Sujungiame `LEFT JOIN` su `INNER JOIN`:

```sql
SELECT first_name, last_name, email, make, model, plate, name
FROM person
LEFT JOIN car ON person.car_id=car.id
INNER JOIN company ON person.company_id=company.id
ORDER BY last_name;
```

## Išvados

- `JOIN` leidžia jungti kelias lenteles ir lengviau analizuoti duomenis nei naudojant `WHERE`.
- `INNER JOIN` jungia tik tas eilutes, kurios turi atitinkamas reikšmes abiejose lentelėse.
- `LEFT JOIN` išlaiko visas eilutes iš pirmosios (kairės) lentelės, net jei antrojoje (dešinėje) lentelėje nėra atitikmenų.
- `JOIN` ir agregavimo funkcijos (`COUNT()`, `SUM()`, `AVG()`) leidžia analizuoti duomenų pasiskirstymą.
- Norint išgauti daugiau informacijos, galima naudoti papildomus filtrus, `GROUP BY`, `HAVING` ir `ORDER BY`.




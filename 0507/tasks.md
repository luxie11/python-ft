# Užduotis: Knygų valdymo aplikacija su Flask ir React

## Tikslas

Sukurti web aplikaciją, leidžiančią vartotojams valdyti knygų sąrašą. Aplikacija turės galimybę pridėti, peržiūrėti, redaguoti ir ištrinti knygas, naudojant Flask kaip backend ir React kaip frontend.

## Užduoties aprašymas

Jūsų užduotis - sukurti dvi aplikacijos dalis:

### 1. Backend (Flask + SQLite)

- Sukurti Flask serverį.
- Naudoti SQLite duomenų bazę.
- Sukurti "Book" modelį su laukais:
  - `id` (unikalus identifikatorius)
  - `title` (knygos pavadinimas)
  - `author` (autorius)
  - `year` (išleidimo metai)
- Įdiegti šiuos API maršrutus:
  - Gauti visas knygas (`GET /api/books`)
  - Pridėti knygą (`POST /api/books`)
  - Redaguoti knygą (`PUT /api/books/<id>`)
  - Ištrinti knygą (`DELETE /api/books/<id>`)
- API grąžins duomenis JSON formatu.
- Naudoti CORS, kad frontend galėtų pasiekti backend.

### 2. Frontend (React + Fetch API)

- Sukurti React aplikaciją su pagrindiniu komponentu `App.js`.
- Naudoti fetch API jungimui su backend.
- Implementuoti šias funkcijas:
  - Atvaizduoti knygų sąrašą.
  - Pridėti knygą.
  - Redaguoti knygą.
  - Ištrinti knygą.
- Sukurti UI su laukais knygos pavadinimui, autoriui ir metams.
- Pridėti mygtukus pridėti, redaguoti ir ištrinti knygas.

## Papildomos užduotys

- Pridėti klaidų pranešimus (pvz., jei neįvesti visi reikalingi duomenys).
- Patobulinti UI naudojant CSS.
- Sukurti paieškos funkciją knygų sąraše.

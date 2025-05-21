# Django užduotis: Viešas užrašų bloknotas („Public Notes“)

##  Užduoties tikslas

Sukurti Django aplikaciją, kurioje vartotojai gali **kurti, redaguoti ir trinti tik savo užrašus**, bet **visi vartotojai gali matyti visų užrašus**. Taip pat turi būti papildomas puslapis, kuriame matomi **tik prisijungusio vartotojo užrašai**.

---
## Github

- Sukurti privačią repozitoriją pavadinimu ``public-notes``
- Sukurti naują branch ```git checkout -b feature/project```
- Atlikus šią užduotį sukurti Pull Request Github puslapyje ir atsiųsti nuorodą dėstytojui

---

## Modeliai (tekstinis aprašymas)

### Note (Užrašas)
- `title` – trumpas pavadinimas (CharField)
- `content` – turinys (TextField)
- `created_by` – nuoroda į Django `User` modelį (ForeignKey)
- `created_at` – sukūrimo data (DateTimeField)

> Vienas vartotojas gali turėti daug užrašų, bet vienas užrašas priklauso tik vienam vartotojui (**One-to-Many** ryšys).

---

## Formos

Naudojama `ModelForm` forma:

### `NoteForm`
- Laukai:
  - `title`
  - `content`
- `created_by` ir `created_at` užpildomi automatiškai programiškai.

---

##  URL maršrutai

| Maršrutas               | Aprašymas                                  |
|------------------------|--------------------------------------------|
| `/notes/`              | Visų vartotojų užrašų sąrašas              |
| `/notes/<id>/`         | Konkretaus užrašo peržiūra                 |
| `/notes/create/`       | Naujo užrašo kūrimas                       |
| `/notes/<id>/edit/`    | Užrašo redagavimas (tik autoriui)         |
| `/notes/<id>/delete/`  | Užrašo trynimas (tik autoriui)            |
| `/notes/mine/`         | Tik prisijungusio vartotojo užrašai       |

---

## Vartotojų teisės

- Tik **prisijungęs vartotojas** gali kurti, redaguoti ir trinti.
- Redaguoti ar trinti leidžiama **tik savo užrašus**.
- Visi vartotojai gali **peržiūrėti visų vartotojų užrašus**.
- Puslapis `/notes/mine/` rodo tik prisijungusio vartotojo įrašus.

---

## Šablonų idėjos

- **header.html**
- **footer.html**
- **notes_list.html** – rodomi visi užrašai
- **notes_mine.html** – rodomi tik savo užrašai
- **note_detail.html** – peržiūra
- **note_form.html** – kūrimas/redagavimas
- **note_confirm_delete.html** – trynimo patvirtinimas ***Jeigu reikia! (NEPRIVALOMA)***

> Redaguoti/trinti mygtukai rodomi tik autoriui.
> 
> Galima sukurti ir daugiau reikalingų šablonų.

---

## Django admin
- Registruoti `Note` modelį su `list_display = ['title', 'created_by', 'created_at']`
- Galima naudoti admin'ą testavimui, bet pagrindinis funkcionalumas – naudotojų puslapiuose.

---
## Dizainas

- Reikia panaudoti CSS arba kažkokį Framework (Bootstrap, Chakra UI, Tailwind CSS)
---

##  Papildomos idėjos (pasirinktinai studentams)

1. **Paieška pagal pavadinimą** visų užrašų sąraše
2. **Filtras** pagal vartotoją (pvz. „rodyti tik naudotojo Tomas užrašus“)
3. **Markdown palaikymas** turinio lauke (naudojant `markdown` biblioteką)
4. **Komentarų sistema** prie kiekvieno užrašo (One-to-Many: Note → Comments)
5. **Žvaigždučių sistema / įvertinimai** (pvz., 1–5 žvaigždutės)
6. **Žymės (tags)** – Many-to-Many ryšys tarp Notes ir Tag modelių


---

##  Minimalus funkcionalumas

- [ ] Visi gali peržiūrėti visus užrašus
- [ ] Tik prisijungęs vartotojas gali kurti naujus įrašus
- [ ] Tik autorius gali redaguoti ir trinti savo įrašus
- [ ] `/notes/mine/` rodo tik prisijungusio vartotojo įrašus
- [ ] CRUD veikia korektiškai
- [ ] Puslapiai tvarkingi, informatyvūs ir intuityvūs

---

## Testavimas

Rekomenduojama sukurti bent 2 vartotojus:
- Sukurti po kelis užrašus
- Patikrinti, kad vienas negali redaguoti kito įrašų
- Patikrinti, kad mato visų užrašus

---

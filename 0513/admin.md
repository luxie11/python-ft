
---

# Django administracinė sąsaja (Admin)

## Tikslai

* Suprasti, kokią reikšmę turi Django administracinė sąsaja.
* Išmokti aktyvuoti ir konfigūruoti admin sistemą.
* Suprasti, kaip modeliai pateikiami administracinėje aplinkoje.
* Pradėti personalizuoti, kaip duomenys rodomi ir tvarkomi admin sąsajoje.

---

## Teorija

### Kas yra Django administracinė sąsaja?

Django turi įmontuotą administravimo sistemą – tai pilnai veikiantis grafinis valdymo įrankis duomenų bazei:

✅ Duomenų įrašų kūrimas, redagavimas, šalinimas

✅ Paieškos, filtravimo ir rūšiavimo galimybės

✅ Vartotojų teisės ir valdymas

✅ Patogus grafinis sąsajos interfeisas, be SQL

> Visi veiksmai atliekami su tais pačiais modeliais, kurie aprašomi `models.py` faile.

---

### Kaip įjungti administracinę sistemą

1. **Registruok modelį `admin.py` faile:**

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

2. **Sukurk administratorių (supernaudotoją):**

```bash
python manage.py createsuperuser
```

Įvesk vartotojo vardą, el. paštą ir slaptažodį.

3. **Prisijunk prie administracinės aplinkos:**
 
4. [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

### Modelių vaizdavimo konfigūravimas

Galima personalizuoti, kaip modeliai rodomi admin lange, naudojant `ModelAdmin` klases.

#### Pavyzdys:

```python
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

admin.site.register(Post, PostAdmin)
```

**`list_display`** – rodomi stulpeliai sąrašo vaizde
 
**`search_fields`** – leidžia ieškoti pagal laukus
 
**`list_filter`** – šoninis filtravimo langas
 
**`ordering`** – numatytoji įrašų rikiavimo tvarka

---

## 🛠️ Praktika

1. Patikrink, ar `Post` modelis yra užregistruotas `admin.py`. Jei ne – pridėk jį.

2. Sukurk supernaudotoją:

```bash
python manage.py createsuperuser
```

3. Prisijunk prie administracinės sąsajos:
   📍 [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

4. Sukurk naują įrašą per `Post` modelį.

5. Sukurk `PostAdmin` klasę su `list_display`:

```python
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
```

6. Pridėk paieškos funkcionalumą:

```python
search_fields = ('title',)
```

7. Išbandyk filtravimą, rūšiavimą, redagavimą.

---

## Klausimai savikontrolei

1. **Kuo naudinga naudoti Django administracinę sistemą vietoje darbo tiesiogiai su DB?**
   Leidžia greitai ir saugiai atlikti CRUD veiksmus be SQL ar papildomų įrankių.

2. **Kokios informacijos reikia supernaudotojui sukurti?**
   Naudotojo vardas, el. paštas, slaptažodis.

3. **Kaip keisti, kokie stulpeliai rodomi sąrašo lange?**
   Naudoti `list_display` `ModelAdmin` klasėje.

4. **Kaip greitai rasti konkretų įrašą admin sąsajoje?**
   Naudojant `search_fields` konfigūraciją arba filtrus.

5. **Kaip apriboti naudotoją, kad jis matytų tik dalį duomenų?**

   * Sukurti jam atskirą vartotoją.
   * Pritaikyti teises (`permissions`).
   * Naudoti `ModelAdmin` su `get_queryset()` ir `has_change_permission()` metodais.

---

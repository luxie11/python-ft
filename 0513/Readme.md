# Modeliai ir duomenų bazės valdymas su Django

## Tikslai

* Suprasti, kaip Django modeliai leidžia kurti duomenų struktūrą panaudojant Python kalbą.
* Išmokti sukurti modelius ir juos registruoti aplikacijoje.
* Suprasti, kaip Django generuoja ir naudoja migracijas.
* Naudotis `manage.py shell` testuojant modelių funkcionalumą.

---

## Teorija

### Django modelių sistema

Django modeliai aprašo, kaip duomenys saugomi. Modelis – tai `Python` klasė, paveldinti iš `django.db.models.Model`. Django automatiškai konvertuoja modelį į SQL lentelę.

**Modelio pavyzdys:**

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

* `CharField` – trumpam tekstui (reikalingas `max_length`)
* `TextField` – ilgam tekstui
* `DateTimeField(auto_now_add=True)` – reikšmė nustatoma objekto sukūrimo metu

> Django automatiškai prideda `id` lauką kaip pirminį raktą.

---

### Modelio registravimas admin panelėje

Kad modelis būtų matomas administravimo sąsajoje, jį reikia registruoti `admin.py` faile:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Prisijunk prie [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin), jei sukūrei supervartotoją:

```bash
python manage.py createsuperuser
```

---

### Migracijos

Kai sukuri ar pakeiti modelį, naudok migracijas, kad atnaujintum duomenų bazę:

```bash
python manage.py makemigrations
python manage.py migrate
```

* `makemigrations` – sukuria migracijų failus
* `migrate` – įvykdo pakeitimus duomenų bazėje

---

### Django ir SQLite

Pagal nutylėjimą Django naudoja SQLite:

* Duomenys saugomi faile: `db.sqlite3`
* Tinka mokymuisi ir prototipų kūrimui

Pavyzdys, kaip naudoti PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mano_duombaze',
        'USER': 'vartotojas',
        'PASSWORD': 'slaptazodis',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

---

## Praktika

1. **Sukurk modelį** `Post` su šiais laukais:

```python
title: CharField (iki 200 simbolių)
body: TextField
created_at: DateTimeField(auto_now_add=True)
```

2. Įrašyk modelį į `models.py`.

3. Paleisk migracijas:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Užregistruok modelį `admin.py` faile.

5. Sukurk supervartotoją:

```bash
python manage.py createsuperuser
```

6. Prisijunk prie admin sąsajos: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

7. **Naudok `shell`** testavimui:

```bash
python manage.py shell
```

```python
from blogas.models import Post
Post.objects.create(title="Pirmas įrašas", body="Tai yra turinys")
Post.objects.all()
```

---

## Klausimai savikontrolei

1. **Kodėl migracijos yra būtinos kuriant ar keičiant modelius?**
   Kad pakeitimai modeliuose būtų pritaikyti realiai duomenų bazei.

2. **Kada naudojamas `auto_now_add=True` ir kuo jis skiriasi nuo `auto_now=True`?**

   * `auto_now_add=True` – nustato reikšmę tik sukūrus objektą.
   * `auto_now=True` – atnaujina datą kaskart išsaugojus objektą.

3. **Kur laikomi migracijų failai ir kokį vaidmenį jie atlieka?**

   * `migrations/` kataloge.
   * Aprašo modelių struktūros pokyčius ir leidžia valdyti DB versijas.

4. **Kodėl verta naudoti admin sąsają testuojant modelių veikimą?**
   Tai leidžia greitai peržiūrėti ir redaguoti duomenis be papildomo kodo.

5. **Ar galima pakeisti modelio pavadinimą nekeičiant duomenų bazės struktūros? Kodėl taip arba ne?**
   Ne visada. Django tai laikys struktūros pakeitimu – reikės migracijos, nes keičiasi lentelės pavadinimas.


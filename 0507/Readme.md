# Įvadas į Django

Šis projektas yra skirtas susipažinti su Django – vienu populiariausių Python karkasų žiniatinklio aplikacijoms kurti.

## Tikslai

- Suprasti, kas yra Django ir kam jis naudojamas

---

## Kas yra Django?

**Django** – tai „framework’as“ (programų karkasas), skirtas kurti žiniatinklio aplikacijas naudojant Python.

### Pagrindiniai privalumai:

| Privalumas         | Paaiškinimas                                          |
|--------------------|--------------------------------------------------------|
| Batteries included | Daug funkcijų iš karto prieinama                      |
| Saugumas           | Apsauga nuo SQL injekcijų, CSRF ir pan.              |
| Admin panelė       | Patogi administravimo sąsaja                          |
| Didelė bendruomenė | Daug pamokų, dokumentacijos, bibliotekų               |
| Greita plėtra      | Aiški struktūra, leidžianti greitai augti projektui   |

---

## Django struktūra: MTV

- **Model (M)** – duomenų bazės lentelių atvaizdavimas
- **Template (T)** – HTML šablonai su Django žymomis
- **View (V)** – Python funkcijos ar klasės, kurios apdoroja užklausas

---

##  Django diegimas

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
pip install django
python -m django --version
````

---

## Naujo projekto kūrimas

```bash
django-admin startproject mano_projektas
cd mano_projektas
```

**Struktūra:**

```
mano_projektas/
├── manage.py
└── mano_projektas/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## Aplikacijos (app) kūrimas

```bash
python manage.py startapp blogas
```

**Struktūra:**

```
blogas/
├── admin.py
├── apps.py
├── models.py
├── views.py
├── tests.py
└── migrations/
```

Nepamiršk pridėti aplikacijos į `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'blogas',
]
```

---

##  Serverio paleidimas

```bash
python manage.py runserver
```

Atsidaryk naršyklę ir eik į:

```
http://127.0.0.1:8000
```

Jei viskas veikia – matysi Django pasveikinimo puslapį 🎉

---



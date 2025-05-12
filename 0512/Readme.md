# Django URL maršrutai, vaizdai (views) ir šablonai (templates)

## Tikslai

* Suprasti, kaip Django projektas apdoroja vartotojo užklausas per URL maršrutų sistemą.
* Išmokti kurti ir susieti vaizdus (views) su URL.
* Suprasti šablonų (templates) paskirtį ir struktūrą.
* Gebėti perduoti duomenis iš Python funkcijų į HTML šabloną.

## Teorija

### Django URL sistema (maršrutai)

Kai vartotojas atidaro tam tikrą adresą naršyklėje, Django sistema tikrina, ar tas adresas yra aprašytas projekto `urls.py` faile. Jei randa atitinkamą maršrutą, iškviečia nurodytą Python funkciją (vadinamą *view*), kuri sugeneruoja atsakymą.

**Maršruto aprašymas:**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagrindinis, name='pagrindinis'),
    path('apie/', views.apie, name='apie'),
]
```

Kiekvienas `path()` kvietimas susieja konkretų adresą su `views.py` faile aprašyta funkcija.

* Pirmas parametras yra URL kelias,
* Antras – funkcija, kuri bus vykdoma,
* Trečias (nebūtinas) – simbolinis vardas.

### Pagrindinis projekto `urls.py`

Projekto `urls.py` faile dažniausiai yra pagrindinis maršrutų žemėlapis, kuris įtraukia visų aplikacijų `urls.py` failus per `include()`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogas.urls')),
]
```

Tokiu būdu visas aplikacijos `urls.py` turinys yra prijungiamas prie pagrindinio puslapio.

### View funkcijos (`views.py`)

View funkcijos apdoroja naršyklės užklausas ir grąžina atsakymą. Paprasčiausiu atveju jos gali grąžinti tekstą:

```python
from django.http import HttpResponse

def pagrindinis(request):
    return HttpResponse("Sveiki atvykę į pagrindinį puslapį!")
```

Tačiau dažniausiai naudojama `render()` funkcija, kuri leidžia atvaizduoti HTML šabloną:

```python
from django.shortcuts import render

def pagrindinis(request):
    return render(request, 'pagrindinis.html')
```

### Šablonai (`templates/`)

Django šablonai – tai HTML failai, kuriuose galima naudoti specialią Django sintaksę – šablonų žymėjimus. Jie leidžia dinamiškai keisti turinį priklausomai nuo duomenų, gautų iš view funkcijos.

**Pavyzdys: `templates/pagrindinis.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ pavadinimas }}</title>
</head>
<body>
    <h1>{{ antraste }}</h1>
    <p>Šis puslapis sukurtas naudojant Django šabloną.</p>
</body>
</html>
```

Šablonų failai turi būti laikomi kataloge `templates`, kurį reikia sukurti aplikacijos viduje. Django automatiškai ieško HTML failų šioje vietoje, jei ji nurodyta `settings.py` faile.

### `render()` funkcija ir context

Funkcija `render()` leidžia ne tik įkelti HTML failą, bet ir perduoti kintamuosius (*kontekstą*), kuriuos galima naudoti šablone:

```python
def pagrindinis(request):
    kontekstas = {
        'pavadinimas': 'Mano Puslapis',
        'antraste': 'Sveiki atvykę!'
    }
    return render(request, 'pagrindinis.html', kontekstas)
```

HTML šablone galima naudoti šiuos kintamuosius su `{{ }}`:

```html
<h1>{{ antraste }}</h1>
```

## Klausimai savikontrolei

* Kam naudojamas `include()` funkcionalumas pagrindiniame `urls.py`?
* Kaip Django žino, kokią funkciją vykdyti konkrečiam URL?
* Ką daro `render()` ir kuo jis naudingas?
* Kaip perduoti kintamuosius iš Python į HTML šabloną?
* Kuo skiriasi `HttpResponse("tekstas")` nuo `render()`?

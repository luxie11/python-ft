# Testavimas Django aplinkoje

## Tikslai

* Išmokti rašyti vienetinius testus (unit tests) Django projekte.
* Suprasti, kaip testuoti modelius, vaizdus ir formas.
* Gebėti naudoti Django testavimo įrankius (TestCase, Client).
* Paleisti testus naudojant komandą `python manage.py test`.

## Teorija

### Kam reikalingas testavimas?

Testavimas padeda užtikrinti, kad programos komponentai veikia taip, kaip tikimasi. Vienetinis testas – tai mažas testas, kuris patikrina atskirą funkciją, metodą ar logiką.

Django turi integruotą testavimo sistemą, pagrįstą `unittest` biblioteka, todėl testavimą galima pradėti be papildomų bibliotekų.

Testai rašomi faile `tests.py` (aplikacijos šaknyje), arba struktūruotai – kataloge `tests/`.

### TestCase

`TestCase` yra pagrindinė klasė, iš kurios paveldimi visi testų rinkiniai. Ji leidžia naudoti bandomąją (testinę) duomenų bazę, kuri automatiškai sukuriama ir išvaloma prieš ir po kiekvieno testo.

```python
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_teksto_generavimas(self):
        post = Post.objects.create(title="Testas", body="Turinys")
        self.assertEqual(str(post), "Testas")
```

### Client

`Client` leidžia simuliuoti vartotojo naršymą ir siųsti GET/POST užklausas į bet kurį URL. Tai leidžia testuoti vaizdus (views):

```python
from django.test import TestCase, Client
from django.urls import reverse

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_puslapis(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_forma(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'Testo įrašas',
            'body': 'Testinis turinys'
        })
        self.assertEqual(response.status_code, 302)  # peradresavimas po sėkmės
```

### Ką testuoti?

* **Modeliai** – ar veikia `__str__` metodas, ar suveikia metodai, ar išsaugomi duomenys.
* **Vaizdai (views)** – ar puslapiai pasiekiami, ar grąžina tinkamą kodą, ar vyksta peradresavimas, ar įrašai sukuriami.
* **Formos** – ar forma suveikia su teisingais duomenimis, ar rodo klaidas su neteisingais.

Papildomai galima testuoti:

* Šablonų atvaizdavimą
* Leidimų (permissions) sistemą
* Autentifikaciją

## Praktika

Sukurk `tests.py` faile testą, kuris:

* Sukuria modelio `Post` įrašą
* Patikrina, ar jo pavadinimas išsaugotas teisingai
* Patikrina, ar `__str__()` metodas grąžina pavadinimą

Sukurk testą vaizdui:

* Ištestuok, ar GET į `/` grąžina 200 statusą
* Ištestuok, ar POST sukuria naują įrašą ir peradresuoja

Paleisk testus:

```bash
python manage.py test
```

Papildomai – testuok klaidingą formos pateikimą, patikrink ar rodomos klaidos, jei laukai tušti.

## Klausimai savikontrolei

* Kam reikalingas `TestCase` ir kaip jis veikia?
* Kaip `Client` padeda testuoti vaizdus?
* Kodėl naudinga testuoti `__str__()` metodą?
* Kodėl naudinga turėti testus kiekvienai svarbiai funkcijai?
* Kaip Django užtikrina, kad testai neturės įtakos realiai duomenų bazei?
* Ką reiškia `status_code = 302` ir kada tai vyksta?

---
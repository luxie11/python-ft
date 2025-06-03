# Failų įkėlimas ir signalai

## Tikslai

* Išmokti įkelti ir rodyti paveikslėlius ar kitus failus naudojant Django modelius ir formas.
* Suprasti, kaip naudoti signalus tam tikrų veiksmų automatizavimui.
* Suprasti, kada naudoti signalus, o kada logiką rašyti tiesiogiai vaizduose arba modeliuose.

---

## Teorija

### MEDIA\_URL ir MEDIA\_ROOT

Django projekte failų įkėlimui būtina aiškiai nurodyti, kur bus saugomi įkelti failai (serveryje) ir kokiu adresu jie bus pasiekiami naršyklėje.

* **MEDIA\_ROOT** – serverio kelias į katalogą, kuriame laikomi įkelti failai.
* **MEDIA\_URL** – URL prefiksas, per kurį šie failai bus pasiekiami naršyklėje.

Šie nustatymai rašomi `settings.py` faile:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Kad failai būtų prieinami vystymo metu, `urls.py` faile turi būti įtraukti šie nustatymai:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # kiti maršrutai
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

⚠️ Tai veikia tik vystymo aplinkoje. Produkcijoje statiniais failais turėtų rūpintis specialus serveris (pvz. NGINX).

---

### ImageField ir FileField

Django modeliuose naudojami šie laukai failų įkėlimui:

* **FileField** – leidžia įkelti bet kokį failą (PDF, DOCX, ZIP ir kt.).
* **ImageField** – leidžia įkelti tik paveikslėlius. Reikalinga biblioteka **Pillow**, leidžianti apdoroti vaizdus Python'e.

Diegimas:

```bash
pip install pillow
```

**Pavyzdys – modelis su profilio nuotrauka:**

```python
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiliai/', blank=True, null=True)
```

Argumentas `upload_to='profiliai/'` nurodo, kad failai bus saugomi kataloge `media/profiliai/`.

---

### Failų atvaizdavimas šablone

Norint parodyti įkeltą paveikslėlį šablone, naudojamas `.url`:

```django
<img src="{{ user.profile.profile_picture.url }}" alt="Profilio nuotrauka">
```

Nepamiršk įkelti statinių failų sistemos:

```django
{% load static %}
```

Failai bus pasiekiami tik tuo atveju, jei naršyklė galės juos pasiekti per MEDIA\_URL.

---

### Signalai

Signalai yra Django mechanizmas, leidžiantis reaguoti į įvykius duomenų bazėje, pvz., objekto sukūrimą, atnaujinimą ar ištrynimą.

**Pagrindiniai signalų tipai:**

* `pre_save` – prieš įrašant duomenis į DB.
* `post_save` – po objekto sukūrimo arba atnaujinimo.
* `pre_delete` – prieš objektą ištrinant.
* `post_delete` – po objekto ištrynimo.

Signalai leidžia išskaidyti logiką ir užtikrinti, kad tam tikri veiksmai įvyktų visada, nepriklausomai nuo to, kaip objektas buvo sukurtas (admin, view, shell ar API).

**Pavyzdys – automatinis Profile sukūrimas:**

```python
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def sukurti_profili(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

Tai reiškia: kai sukuriamas naujas User objektas, automatiškai sukuriamas ir jam priskiriamas Profile objektas.

---

### Signalų aktyvavimas

Kad signalai veiktų, juos reikia importuoti. Įprasta praktika:

1. Sukurti failą `signals.py` aplikacijoje.
2. Importuoti jį `apps.py` faile perrašius `ready()` metodą:

```python
class BlogasConfig(AppConfig):
    name = 'blogas'

    def ready(self):
        import blogas.signals
```

Be šio importo signalai neveiks.

---

### Kada naudoti signalus, o kada ne?

✅ Naudoti signalus verta, kai:

* Reikia užtikrinti, kad kažkas visada įvyktų sukūrus/atnaujinus/ištrynus objektą.
* Veiksmas turi būti automatinis (nepriklausomas nuo objekto sukūrimo būdo).

❌ Geriau nenaudoti signalų, kai:

* Logika yra specifinė konkrečiam view arba formos pateikimui.
* Reikia grįžtamojo ryšio vartotojui (pvz. pranešimo apie rezultatą).

---

## Praktika

✅ Pridėk `ImageField` prie modelio `Profile` su `upload_to='profiliai/'`.

✅ Sukurk `ModelForm`, kuris leidžia redaguoti `profile_picture` lauką.

✅ `views.py` faile:

```python
if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    if form.is_valid():
        form.save()
```

✅ Šablone parodyk įkeltą paveikslėlį su `{{ user.profile.profile_picture.url }}`.

✅ Įsitikink, kad veikia failų rodymas per `MEDIA_URL`.

✅ Sukurk `signals.py` ir `post_save` signalą, kuris automatiškai sukuria `Profile` objektą naujam `User`.

✅ Sukurk kitą signalą, kuris:

* ištrina paveikslėlį, jei ištrinamas profilis (naudok `post_delete`), arba
* išsiunčia el. laišką įvykus veiksmui.

---

## Klausimai savikontrolei

1. Kam naudojamas `MEDIA_ROOT` ir `MEDIA_URL`? Ką jie daro?
2. Kodėl būtina naudoti `request.FILES`, kai forma turi failą?
3. Kuo skiriasi `FileField` ir `ImageField`? Kada naudoti kurį?
4. Kodėl signalai naudingi didesniuose projektuose?
5. Kaip importuoti `signals.py`, kad jis veiktų tinkamai?
6. Kaip veikia `post_save` signalas ir kaip patikrinti, ar objektas naujas (`created=True`)?


# Autentifikacija ir vartotojų sistema

## Tikslai

- Suprasti, kaip Django valdo naudotojų autentifikaciją.  
- Išmokti sukurti registracijos, prisijungimo ir atsijungimo funkcionalumą.  
- Suprasti, kaip apriboti prieigą prie puslapių tik prisijungusiems naudotojams.  
- Gebėti išnaudoti `request.user` objektą informacijos personalizavimui ir tikrinimui.

---

## Teorija

### Django naudotojų sistema

Django turi integruotą autentifikacijos sistemą, kuri leidžia kurti, valdyti ir autentifikuoti naudotojus be papildomų bibliotekų. Ji automatiškai įtraukta į projektą, jei naudojamas `django.contrib.auth` modulis (tai daroma pagal nutylėjimą).

Sistema apima:

- Prisijungimo ir atsijungimo funkcionalumą  
- Naudotojų registravimą  
- Sesijų valdymą (naudotojų būsena išlieka tarp puslapio perėjimų)  
- Teisių (permissions) ir grupių (groups) palaikymą  
- Lengvą integraciją su formomis ir `request.user` naudojimą šablonuose  

Numatytasis naudotojo modelis – `User` – turi pagrindinius laukus: `username`, `email`, `password`, `first_name`, `last_name`, taip pat papildomus atributus kaip `is_active`, `is_staff`, `is_superuser`, kurie naudingi skirstant vartotojus pagal prieigos teises.

---

### Registracija

Registracijai galima naudoti `UserCreationForm` – tai jau paruošta forma, kuri apima vartotojo vardo ir slaptažodžio įvedimą, dvigubą slaptažodžio patvirtinimą, validacijas ir klaidų pateikimą.

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistracijosForma(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
````

Šią formą galima pateikti per `views.py`, o duomenis išsaugoti su `form.save()`.

Registracijos procesas turi būti apsaugotas nuo netinkamų įrašų, todėl naudinga naudoti `form.is_valid()` – jis patikrins, ar visi laukai užpildyti, ar slaptažodžiai sutampa, ar vartotojo vardas nėra užimtas.

---

### Prisijungimas ir atsijungimas

Django siūlo `LoginView` ir `LogoutView`, kurie valdo prisijungimą ir atsijungimą pagal sesijų principą. Jie gali būti iškart naudojami su savo HTML šablonais.

```python
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [
    path('prisijungti/', LoginView.as_view(template_name='prisijungti.html'), name='prisijungti'),
    path('atsijungti/', LogoutView.as_view(next_page='prisijungti'), name='atsijungti'),
]
```

Prisijungus naudotojui, `request.user` taps prisijungusio vartotojo objektu. Jei ne, jis bus `AnonymousUser`. Šį objektą galima naudoti tiek `views.py`, tiek šablonuose, pavyzdžiui:

```django
{% if user.is_authenticated %}
  Sveiki, {{ user.username }}!
{% else %}
  Sveiki, svečias!
{% endif %}
```

---

### Naudotojo identifikavimas

`request.user` – tai visada prieinamas objektas bet kuriame Django vaizde (view) ir šablone. Jo metodas `is_authenticated` grąžina `True`, jei vartotojas prisijungęs, arba `False`, jei ne.

Galima naudoti sąlygas:

```python
if request.user.is_authenticated:
    # daryti kažką prisijungusiam naudotojui
else:
    # rodyti klaidą arba peradresuoti
```

---

### Prieigos ribojimas

Django leidžia lengvai apsaugoti tam tikrus puslapius:

#### Funkcijų vaizduose su dekoratoriumi `@login_required`:

```python
from django.contrib.auth.decorators import login_required

@login_required
def tik_prisijungusiems(request):
    return render(request, 'slaptas.html')
```

#### Klasiniuose vaizduose su `LoginRequiredMixin`:

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class SlaptasPuslapis(LoginRequiredMixin, TemplateView):
    template_name = 'slaptas.html'
```

Be autentifikacijos, šie metodai automatiškai peradresuoja neprisijungusį vartotoją į prisijungimo puslapį.

---

## Praktika

* Sukurk registracijos formą naudodamas `UserCreationForm` klasę ir parodyk ją `registracija.html` šablone. Pridėk validacijos klaidų rodymą.
* Sukurk vaizdą `views.py`, kuris priima POST užklausą su forma ir sukuria naują vartotoją, jei duomenys tinkami.
* Sukurk `LoginView` ir `LogoutView` maršrutus. Sukurk šabloną `prisijungti.html` su forma.
* Pagrindiniame puslapio šablone naudok `user.is_authenticated` ir parodyk skirtingą meniu prisijungusiam ir neprisijungusiam vartotojui.
* Sukurk slaptą puslapį ir apsaugok jį su `@login_required`.
* Patikrink, ar neprisijungęs naudotojas yra peradresuojamas į prisijungimo formą, jei bando patekti į apsaugotą puslapį.
* Sukurk testinį vartotoją per registracijos formą ir prisijunk su juo.

---

## Klausimai savikontrolei

* Kuo skiriasi `LoginView` ir `LogoutView`?
* Kaip Django atpažįsta, ar naudotojas prisijungęs?
* Kuo naudinga naudoti `UserCreationForm` vietoje savo formos?
* Kada naudoti `@login_required`, o kada `LoginRequiredMixin`?
* Kaip galima peradresuoti naudotoją į konkretų puslapį po prisijungimo ar atsijungimo?
* Kur Django saugo naudotojo autentifikacijos būseną tarp užklausų?


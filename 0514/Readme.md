# Formos ir POST užklausos Django projekte

## Tikslai

- Suprasti, kaip Django tvarko vartotojo pateikiamus duomenis per formas.
- Išmokti naudoti `forms.Form` ir `forms.ModelForm` klasėmis grįstas formas.
- Gebėti priimti ir apdoroti POST užklausas.
- Suprasti CSRF apsaugos mechanizmą.

---

## Teorija

### Formos Django sistemoje

Formos Django karkase gali būti kuriamos dviem pagrindiniais būdais:

- **`forms.Form`** – naudojama, kai forma nėra tiesiogiai susieta su jokiu modeliu.
- **`forms.ModelForm`** – naudojama, kai forma pagrįsta konkrečiu modeliu ir leidžia greitai generuoti laukus pagal modelio struktūrą.

#### `forms.Form` pavyzdys:

```python
from django import forms

class KontaktuForma(forms.Form):
    vardas = forms.CharField(max_length=100)
    el_pastas = forms.EmailField()
    zinute = forms.CharField(widget=forms.Textarea)
````

#### `forms.ModelForm` pavyzdys:

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
```

---

## POST užklausos ir `request.POST`

Kai naudotojas pateikia formą, ji siunčiama į serverį naudojant POST metodą. Django gali prieiti prie duomenų per `request.POST`.

Tipinė view funkcija atrodo taip:

```python
from django.shortcuts import render, redirect
from .forms import PostForm

def naujas_irasas(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagrindinis')
    else:
        form = PostForm()
    return render(request, 'naujas.html', {'form': form})
```

---

## CSRF apsauga

**CSRF (Cross-Site Request Forgery)** – Django mechanizmas, saugantis nuo neteisėto formų pateikimo.

Šablone būtina įdėti CSRF žymenį:

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Išsaugoti</button>
</form>
```

Jei žymens nebus, Django atmes POST užklausą kaip nesaugią.

---

## Praktika

1. Sukurk `forms.py` faile dvi formas:

   * Vieną paveldint iš `forms.Form`
   * Kitą – iš `forms.ModelForm`, susietą su modeliu `Post`

2. Sukurk view funkciją, kuri:

   * Tikrina, ar užklausa yra POST
   * Jei forma tinkama – išsaugo duomenis ir peradresuoja naudotoją
   * Jei GET – parodo tuščią formą

3. Sukurk `naujas.html` šabloną, kuriame būtų:

   * Forma
   * `{% csrf_token %}`
   * Mygtukas formai pateikti

4. Sukurk maršrutą `urls.py`, kuris nukreiptų į formos puslapį.

5. Išbandyk formą naršyklėje:

   * Patikrink, ar įrašai išsaugomi duomenų bazėje
   * Palik laukelį tuščią – patikrink, ar rodoma klaida

---

## Klausimai savikontrolei

* Kuo skiriasi `forms.Form` ir `forms.ModelForm`?
* Ką patikrina `form.is_valid()`?
* Kodėl reikia naudoti `{% csrf_token %}`?
* Kas nutiktų, jei POST užklausa neturėtų CSRF žymens?
* Kaip galima atvaizduoti formos klaidas šablone?

---

> **Pastaba:** Norėdami atvaizduoti formos klaidas šablone, naudokite `{{ form.errors }}` arba `{{ form.field_name.errors }}`.


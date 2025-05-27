# Django Class-Based Views (CBV)

## Tikslai

- Suprasti, kuo klasės pagrindu kuriami vaizdai (CBV) skiriasi nuo funkcinių vaizdų (FBV).
- Išmokti naudoti `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`.
- Suprasti, kaip naudoti `get_context_data()` papildomiems duomenims perduoti į šabloną.
- Naudoti `success_url` nurodant, kur peradresuoti po sėkmingos operacijos.

---

## Teorija

### Kuo skiriasi FBV ir CBV?

- **FBV** (Function-Based Views): įprastos Python funkcijos, kurios apdoroja užklausą ir grąžina atsakymą.
- **CBV** (Class-Based Views): Python klasės, paveldimos iš `django.views`, leidžia naudoti objektinį požiūrį ir sutrumpinti kodą, ypač CRUD operacijose.

---

## Dažniausiai naudojamos CBV klasės

- `ListView` – objektų sąrašo atvaizdavimas
- `DetailView` – vieno objekto detalus vaizdas
- `CreateView` – naujo objekto kūrimas
- `UpdateView` – esamo objekto redagavimas
- `DeleteView` – objekto ištrynimas

---

## Pavyzdžiai

### ListView

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
````

---

### DetailView

```python
from django.views.generic import DetailView

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
```

---

### CreateView ir UpdateView

```python
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')
```

---

### DeleteView

```python
from django.views.generic.edit import DeleteView

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
```

---

### get\_context\_data()

Papildomiems duomenims perduoti į šabloną:

```python
class PostListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kintamasis'] = 'Papildoma info'
        return context
```

---

## Praktika

### Maršrutai `urls.py` faile

```python
from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('naujas/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/redaguoti/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/istrinti/', PostDeleteView.as_view(), name='post_delete'),
]
```

---

### Šablonai

Sukurk šiuos šablonų failus:

* `post_list.html`
* `post_detail.html`
* `post_form.html`
* `post_confirm_delete.html`

---

### Patikrinimas

* Patikrink, ar veikia įrašų sąrašas ir detali peržiūra.
* Sukurk naują objektą.
* Redaguok esamą objektą.
* Ištrink objektą.

---

## Klausimai savikontrolei

1. Kuo skiriasi CBV nuo FBV ir kada verta naudoti CBV?
2. Kam naudojamas `success_url`?
3. Kaip pritaikyti `get_context_data()` konkretiems poreikiams?
4. Kokiais atvejais CBV tampa efektyvesni už funkcinius vaizdus?
5. Kodėl `reverse_lazy` naudojamas vietoje `reverse` CBV kontekste?

---
# Ryšiai tarp modelių (ForeignKey, ManyToMany, OneToOne)

## Tikslai
- Suprasti, kaip Django modeliai gali būti susieti tarpusavyje.  
- Išmokti naudoti ForeignKey, ManyToManyField ir OneToOneField laukus.  
- Suprasti, ką reiškia on_delete ir related_name argumentai.  
- Išmokti naudotis ryšiais vaizduose ir šablonuose.  

## Teorija

### Modelių ryšiai
Django leidžia kurti ryšius tarp modelių naudojant tris pagrindinius laukų tipus:

#### ForeignKey – vienas-prie-daugelio (many-to-one):
Pvz., kiekvienas komentaras priklauso vienam įrašui (Comment → Post).
```python
class Post(models.Model):
    title = models.CharField(max_length=200)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
````

#### OneToOneField – vienas-prie-vieno:

Pvz., kiekvienas naudotojo profilis turi vieną papildomą informacijos objektą.

```python
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

#### ManyToManyField – daug-prie-daug:

Pvz., įrašas gali turėti kelias kategorijas, o kategorija – daug įrašų.

```python
class Category(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category)
```

### on\_delete reikšmės

Naudojant ForeignKey ar OneToOneField, būtina nurodyti on\_delete elgseną:

* **CASCADE** – susijusiam objektui ištrynus, ištrinami ir priklausomi objektai
* **SET\_NULL** – nustatoma reikšmė null (reikia `null=True`)
* **PROTECT** – neleidžia ištrinti susijusio objekto
* **SET\_DEFAULT** – nustato numatytąją reikšmę

### related\_name

`related_name` nurodo, kaip galime pasiekti susijusius objektus iš kito modelio:

```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
```

Tada galime naudoti:

```python
post = Post.objects.get(id=1)
komentarai = post.comments.all()
```

## Praktika

1. Sukurk du modelius:

* `Post` (pavadinimas, turinys)
* `Comment` (tekstas, nuoroda į Post per ForeignKey)

2. Pridėk `related_name='comments'`, kad būtų galima gauti visus komentarus per `post.comments.all()`.

3. Sukurk `ManyToManyField` tarp `Post` ir `Category`, kad vienas įrašas galėtų turėti kelias kategorijas.

4. Sukurk `OneToOneField` ryšį tarp `User` ir `Profile` (pridėk lauką `bio`).

5. Atlik migracijas ir naudok shell:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py shell
```

6. Sukurk kelis `Post`, `Comment` ir `Category` įrašus ir patikrink jų ryšius per `post.comments.all()` ir `post.categories.all()`.

7. Sukurk šabloną, kuriame:

* Atvaizduojamas vienas `Post`
* Po juo rodomi visi komentarai
* Parodomos kategorijos

## Klausimai savikontrolei

* Kuo skiriasi `ForeignKey`, `OneToOneField` ir `ManyToManyField`?
* Kam naudojamas `related_name`? Ką jis keičia?
* Ką reiškia `on_delete=models.CASCADE` ir kokios yra kitos alternatyvos?
* Kaip iš šablono pasiekti visus susijusius objektus?
* Kodėl svarbu planuoti ryšius iš anksto kuriant duomenų struktūrą?



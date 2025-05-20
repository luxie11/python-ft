from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Many to one rysys
class Post(models.Model):
    title = models.CharField(max_length=200)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

# One to One rysys
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

# Many to Many
class Category(models.Model):
    title = models.CharField(max_length=200)

class Products(models.Model):
    title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
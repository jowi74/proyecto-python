from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    name = models.CharField(max_length=50)
    birth = models.DateField()
    slug = models.SlugField()
    propic = models.ImageField(upload_to='profile', default='images/imagen6.jpg')

    def __str__(self):
        return self.name
        
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    publishied = models.DateField()
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

CASAS = (
    ('CAS', 'Casa'),
    ('DEP', 'Departamento'),
    ('VIL', 'Villa'),
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.CharField(max_length=3, choices=CASAS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, by {self.user}"

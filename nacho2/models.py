from django.db import models

# Create your models here.

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

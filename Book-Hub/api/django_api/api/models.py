from django.db import models

 
class Book(models.Model):
    title = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    year = models.IntegerField()
    image = models.ImageField(upload_to='bookImages/',blank=True)


class User(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    type_of_user = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
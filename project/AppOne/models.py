from django.db import models

# Create your models here.
class ImageTest(models.Model):
    image = models.ImageField(upload_to='images/')

class User(models.Model):
    name = models.CharField(max_length= 100)
    age = models.IntegerField()
    address = models.CharField(max_length=200)

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)



class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    author = models.OneToOneField(Author, on_delete=  models.DO_NOTHING)
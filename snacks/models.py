from pydoc import describe
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    describtion = models.TextField()
    price = models.IntegerField()
    count = models.IntegerField()


    def __str__(self):
        return self.name

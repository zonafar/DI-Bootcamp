from django.db import models
from django.utils import timezone

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=30)
    def _str_(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    def _str_(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    def _str_(self):
        return f'{self.first_name} {self.last_name}'

class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(default= timezone.now)
    created_in_country = models.ForeignKey(Country, on_delete = models.CASCADE)
    available_in_countries = models.ManyToManyField(Country,related_name='countries', blank=True)
    category = models.ManyToManyField(Category,related_name='categories')
    director = models.ManyToManyField(Director,related_name='directors', blank=True)
    def _str_(self):
        return self.title



from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name}'


class Animal(models.Model):
    legs = models.IntegerField()
    weight = models.DecimalField(null=True,max_digits=5, decimal_places=2)
    height = models.IntegerField()
    speed = models.IntegerField()
    image = models.CharField(max_length=250,default = '')
    name = models.CharField(null=True,max_length=40,unique=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    # If you delete a person, his posts will be also deleted

    def __str__(self):
        return f'{self.name}'


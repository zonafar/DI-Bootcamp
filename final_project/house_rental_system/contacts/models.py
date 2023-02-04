from django.db import models
from datetime import datetime
# Create your models here.


class Contact(models.Model):
    annonce = models.CharField(max_length=200)
    annonce_id = models.IntegerField()
    nom = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    date_contact = models.DateTimeField(default=datetime.now,blank = True)
    user_id = models.IntegerField(blank=True)

    def _str_(self):
        return self.nom
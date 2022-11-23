from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name  = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = 'upload/')

    # def __str__(self):
    #     return self.name

    def elem(self):
        return self


class Todo(models.Model):
    title = models.CharField(max_length = 40)
    details = models.TextField()
    date_creation = models.DateTimeField(default = timezone.now)
    date_completion = models.DateTimeField(default=timezone.now)
    deadline_date  = models.DateTimeField()
    has_been_done = models.BooleanField(default = False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name = 'category')

    def __str__(self):
        return self.title
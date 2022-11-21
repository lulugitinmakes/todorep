from django.db import models

# Create your models here.

class Task(models.Model):
    name=models.CharField(max_length=222)
    priority=models.IntegerField()

class Task1(models.Model):
    name = models.CharField(max_length=222)
    priority = models.IntegerField()
    date=models.DateField()


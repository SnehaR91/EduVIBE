from django.db import models
# Create your models here.

class Event(models.Model):
    name=models.CharField(max_length=200)
    date=models.DateField()
    time_start=models.TimeField()
    time_end=models.TimeField()
    note=models.TextField()

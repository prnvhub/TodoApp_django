from django.db import models
from django.db.models.fields import CharField
import datetime

# Create your models here.
class Task(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    priority=models.IntegerField()
    date=models.DateField(default=datetime.date.today)
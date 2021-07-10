from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Mood(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    comment = models.CharField(max_length=100)
    date = models.DateField(null=False, blank=False, default=date.today, unique=True)

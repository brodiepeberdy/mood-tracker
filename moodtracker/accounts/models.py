from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quote = models.CharField(max_length=200, default="")
    location = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.user

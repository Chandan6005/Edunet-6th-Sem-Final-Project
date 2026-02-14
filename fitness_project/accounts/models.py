from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    height = models.FloatField(help_text="Height in centimeters", null=True, blank=True)
    weight = models.FloatField(help_text="Weight in kg", null=True, blank=True)
    goal = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username
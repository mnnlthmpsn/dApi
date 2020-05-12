from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, default='2020-04-19')
    phone = models.CharField(max_length=10, blank=True, default='0000000000')
    school = models.CharField(max_length=100, blank=True, default='University of Ghana, Legon')
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
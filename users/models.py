from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Newsfeed(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    body = models.TextField()

# class Session(models.Model):
# user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
# token = models.TextField()
#  is_active = models.BooleanField(null=True)

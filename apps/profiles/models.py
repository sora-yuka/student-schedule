from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class StudentProfileModel(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
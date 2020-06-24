from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.
class CustomUser(AbstractUser):
    id_no = models.CharField(max_length=8, blank=True)
    license_no = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    driver_status = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name+' '+self.last_name



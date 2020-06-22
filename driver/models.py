from django.db import models
from datetime import datetime


# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=200)
    license_no = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    email = models.CharField(max_length=255)
    id_no = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

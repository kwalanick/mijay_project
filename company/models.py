from django.db import models
from datetime import datetime


# Create your models here.
class Company(models.Model):
    company_code = models.CharField(max_length=8,primary_key=True)
    name = models.CharField(max_length=200)
    pin_no = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        if not self.company_code:
            code = Company.objects.filter(name__startswith=self.name[0]).count() + 1
            self.company_code = self.name[0] + format(code, '07')

        super(Company, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

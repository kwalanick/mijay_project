from django.db import models
from datetime import datetime
from company.models import Company

# Create your models here.
class Client(models.Model):
    client_number = models.CharField(max_length=8,null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    id_no = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    company = models.ForeignKey(Company,on_delete=models.DO_NOTHING,blank=True)

    def save(self, *args, **kwargs):
        if not self.client_number:
            code = Client.objects.filter(first_name__startswith=self.first_name[0],last_name__startswith=self.last_name[0]).count() + 1
            self.client_number = self.first_name[0]+self.last_name[0]+format(code,'06')
        super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name+' '+self.last_name

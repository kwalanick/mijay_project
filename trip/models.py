from django.db import models
from datetime import datetime

from client.models import Client
from company.models import Company
from driver.models import Driver

from django.core.mail import send_mail
import africastalking


# Create your models here.
class JourneyType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Journey Type'
        verbose_name_plural = 'Journey Types'


class Trip(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
    journey_type = models.ForeignKey(JourneyType, on_delete=models.DO_NOTHING, blank=True)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    travel_date = models.DateTimeField(default=datetime.now, blank=True)
    vehicle_no = models.CharField(max_length=20)

    def __str__(self):
        return self.company.name + ' ' + self.client.first_name + ' ' + self.driver.name

    class Meta:
        verbose_name = 'Trip'
        verbose_name_plural = 'Trip'

    def save(self, *args, **kwargs):
        # SEND EMAIL
        contact = '0715 195 779'
        send_mail(
            'Mijay Travels Ltd',
            'Dear ' + self.client.first_name + ' .Kindly note the below details for your pick up allocation'+''
                                               ' Plate No '+self.vehicle_no+''
                                               ' Driver '+self.driver.name+''
                                               ' Contact '+contact+''
                                               ' Thank you for choosing Mijay Travels',
            'mijaytravels@gmail.com',
            [self.client.email, 'terrygathonitrey@gmail.com'],
            fail_silently=False,
        )

        # Initialize SDK
        username = "mijay"  # use 'sandbox' for development in the test environment
        api_key = "99f1ef540cbb42b20c664986cd3a49be87761b5696863f2d59be64cceb91b002"  # use your sandbox app API key for development in the test environment
        africastalking.initialize(username, api_key)

        # Initialize a service e.g. SMS
        sms = africastalking.SMS

        # Use the service synchronously
        response = sms.send('Dear ' + self.client.first_name + ' .Kindly note the below details for your pick up allocation .'+''
                                               ' Plate No '+self.vehicle_no+''
                                               ' Driver '+self.driver.name+''
                                               ' Contact '+contact+''
                                               '. Thank you for choosing Mijay Travels.', [self.client.phone])
        print(response)

        super(Trip, self).save(*args, **kwargs)

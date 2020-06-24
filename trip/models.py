from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from users.models import CustomUser

from client.models import Client
from company.models import Company
from driver.models import Driver

from django.core.mail import send_mail
from smart_selects.db_fields import ChainedForeignKey

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
    client = ChainedForeignKey(
        Client,
        chained_field="company",
        chained_model_field="company",
        show_all=False,
        auto_choose=True,
        sort=True)
    driver = models.ForeignKey(CustomUser, limit_choices_to={'groups__pk': 1},
                               on_delete=models.DO_NOTHING, null=True)
    journey_type = models.ForeignKey(JourneyType, on_delete=models.DO_NOTHING, blank=True)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    travel_date = models.DateTimeField(default=datetime.now, blank=True)
    vehicle_no = models.CharField(max_length=20)
    start_mileage = models.IntegerField(null=True)
    end_mileage = models.IntegerField(null=True)
    start_time = models.DateTimeField(blank=True,null=True)
    end_time = models.DateTimeField(blank=True,null=True)
    trip_status = models.CharField(max_length=20,default='created')

    def distance_covered(self):
        return self.end_mileage - self.start_mileage

    def time_taken(self):
        return self.end_time - self.start_time

    def __str__(self):
        return self.company.name + ' ' + self.client.first_name + ' ' + self.driver.first_name

    class Meta:
        verbose_name = 'Trip'
        verbose_name_plural = 'Trip'

    def save(self, *args, **kwargs):
        # SEND EMAIL
        contact = '0715 195 779'
        send_mail(
            'Mijay Travels Ltd',
            'Dear ' + self.client.first_name + ' .Kindly note the below details for your pick up allocation' + ''
                                                                                                               ' Plate No ' + self.vehicle_no + ''
                                                                                                                                                ' Driver ' + self.driver.first_name + ''
                                                                                                                                                                                ' Contact ' + self.driver.phone + ''
                                                                                                                                                                                                                  ' Thank you for choosing Mijay Travels',
            'mijaytravels@gmail.com',
            [self.client.email, 'terrygathonitrey@gmail.com'],
            fail_silently=False,
        )

        # # Initialize SDK
        # username = "mijay"  # use 'sandbox' for development in the test environment
        # api_key = "99f1ef540cbb42b20c664986cd3a49be87761b5696863f2d59be64cceb91b002"  # use your sandbox app API key for development in the test environment
        # africastalking.initialize(username, api_key)
        #
        # # Initialize a service e.g. SMS
        # sms = africastalking.SMS
        #
        # # Use the service synchronously
        # response = sms.send(
        #     'Dear ' + self.client.first_name + ' .Kindly note the below details for your pick up allocation .' + ''
        #                                                                                                          ' Plate No ' + self.vehicle_no + ''
        #                                                                                                                                           ' Driver ' + self.driver.first_name + ''
        #                                                                                                                                                                           ' Contact ' + contact + ''
        #                                                                                                                                                                                                   '. Thank you for choosing Mijay Travels.',
        #     [self.client.phone])
        # print(response)
        # response1 = sms.send(
        #     'Dear ' + self.driver.first_name + ' .Kindly note that you have been allocated a trip with below details ' + ''
        #                                                                                                            ' .Client -' + self.client.first_name + ' ' + self.client.last_name + ''
        #                                                                                                                                                                                  ' .Contact -' + self.client.phone + ''
        #                                                                                                                                                                                                                      ' .Pick Point -' + self.source + ''
        #                                                                                                                                                                                                                                                       ' .Destination -' + self.destination + ''
        #                                                                                                                                                                                                                                                                                              ' Journey Type ' + self.journey_type.name + '',
        #     [self.driver.phone])
        # print(response1)

        super(Trip, self).save(*args, **kwargs)

from django.shortcuts import render, redirect
from .models import Trip
from datetime import datetime

# Create your views here.
def start_trip(request, trip_id):
    if request.method == 'POST':
        trip = Trip.objects.get(id=trip_id)
        trip.start_mileage = request.POST['start_mileage']
        trip.start_time = datetime.now()
        trip.trip_status = 'in progress'
        trip.save()
        return redirect('dashboard')


def end_trip(request, trip_id):
    if request.method == 'POST':
        trip = Trip.objects.get(id=trip_id)
        trip.end_mileage = request.POST['end_mileage']
        trip.trip_status = 'completed'
        trip.end_time = datetime.now()
        trip.save()
        return redirect('dashboard')

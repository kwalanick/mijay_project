from django.urls import path
from . import views

urlpatterns = [
    path('start/<int:trip_id>', views.start_trip,name='start_trip'),
    path('end/<int:trip_id>', views.end_trip,name='end_trip'),
]
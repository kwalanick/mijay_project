from django.contrib import admin
from .models import Trip, JourneyType


# Register your models here.
class JourneyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('name',)


admin.site.register(JourneyType, JourneyTypeAdmin)


class TripAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General Information',
         {'fields': ('company', 'client', 'driver')}
         ),
        ('Other Information',
         {'fields': ('journey_type', 'source','destination','vehicle_no')}
         ),
        ('TimeStamps',
         {'fields': ('travel_date',)}
         )
    )
    list_display = (
    'id', 'company', 'client', 'driver', 'journey_type', 'source',
            'destination', 'vehicle_no','start_time','end_time','start_mileage','end_mileage')
    list_display_links = ('id', 'company', 'client', 'driver')
    search_fields = ('id', 'company', 'client', 'driver')
    autocomplete_fields = ('company','driver','journey_type')
    #list_filter = ('company', 'client', 'driver', 'source', 'destination')


admin.site.register(Trip, TripAdmin)

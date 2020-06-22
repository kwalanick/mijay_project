from django.contrib import admin
from .models import Driver


# Register your models here.
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_no', 'id_no', 'phone', 'email', 'hire_date')
    list_per_page = 25
    list_display_links = ('name', 'license_no')
    search_fields = ('name', 'license_no')


admin.site.register(Driver, DriverAdmin)

from django.contrib import admin
from .models import Client


# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_number', 'first_name', 'last_name', 'id_no', 'phone', 'email')
    list_display_links = ('client_number', 'first_name', 'last_name', 'id_no')
    readonly_fields = ('client_number',)
    list_per_page = 25


admin.site.register(Client, ClientAdmin)

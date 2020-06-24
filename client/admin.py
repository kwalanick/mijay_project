from django.contrib import admin
from .models import Client


# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_number', 'first_name', 'last_name', 'id_no', 'phone', 'email','company')
    list_display_links = ('client_number', 'first_name', 'last_name', 'id_no')
    list_filter = ('company',)
    fieldsets = (
        ("Company Information" ,{"fields":('company',)}),
        ("Personal Information",{"fields":('first_name','last_name','id_no')}),
        ("Contact Information" ,{"fields":('phone','email','address')}),
        ("Timestamps", {"fields":('created_date',)}),
    )
    search_fields = ('company',)
    autocomplete_fields = ('company',)
    readonly_fields = ('client_number',)
    list_per_page = 25


admin.site.register(Client, ClientAdmin)

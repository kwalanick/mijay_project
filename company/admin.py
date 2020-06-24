from django.contrib import admin
from .models import Company


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General Information', {
            'fields': ('name', 'pin_no')
        }),
        ('Contact Us', {
            'fields': ('phone', 'email', 'address')
        }),
        ('TimeStamps', {'fields': ('created_date',)})
    )
    list_display = ('company_code', 'name', 'email', 'phone', 'address', 'pin_no', 'created_date')
    search_fields = ('name',)
    list_display_links = ('company_code', 'name')
    list_per_page = 25
    list_filter = ('created_date',)
    readonly_fields = ('company_code',)


admin.site.register(Company, CompanyAdmin)




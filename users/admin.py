# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'license_no','phone','id_no' ]
    search_fields = ('first_name','last_name')
    add_fieldsets = (
         ('User Information', {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name')
            }
         ),
         ('Contact Information',{
             'classes': ('wide',),
             'fields': ('email', 'phone')
         }),
         ('Password',{
           'classes': ('wide',),
           'fields': ('password1', 'password2')
         })
    )


admin.site.register(CustomUser, CustomUserAdmin)

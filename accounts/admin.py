from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserChangeForm,CustomUserCreationForm
from accounts.models import User



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ('name','email','is_active','is_staff','is_superuser','last_login',)

    list_filter = ('is_active','is_staff','is_superuser')

    fieldsets = (
        (None,{'fields':('name','email','profile_pic','gender','password')}),
        ('Permissions',{'fields':('is_staff','is_active','is_superuser','groups','user_permissions')}),
        ('Dates',{'fields':('last_login','date_joined')})
    )

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('name','profile_pic','email','phone','gender','password1','password2','is_staff','is_active')
        }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User,CustomUserAdmin)
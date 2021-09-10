# accounts/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username','email','kvk','Telefoon']
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

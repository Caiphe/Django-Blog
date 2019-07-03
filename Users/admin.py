from django.contrib import admin
from .models import Profile


class UsersDisplay(admin.ModelAdmin):
    list_display = ('username', 'email')


admin.site.register(Profile)

from django.contrib import admin

from authy.models import Profile



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'profile_image', 'url','created']
from django.contrib import admin
from Profile.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['location','User'] 
    fields = ['location','User']#can change order of things on admin site he
    search_fields = ['location','User'] #search bar
    list_filter = ['location'] #sort list by x

admin.site.register(Profile, ProfileAdmin)
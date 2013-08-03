from django.contrib import admin
from Profile.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'location','email'] 
    fields = ['user_id','email','location']#can change order of things on admin site he
    search_fields = ['user_id', 'location','email'] #search bar
    list_filter = ['user_id','location'] #sort list by x

admin.site.register(Profile, ProfileAdmin)
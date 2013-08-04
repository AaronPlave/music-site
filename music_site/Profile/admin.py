from django.contrib import admin
from Profile.models import Profile,Genre

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['location','User'] 
    fields = ['location','User','genre']#can change order of things on admin site he
    search_fields = ['location','User','genre'] #search bar
    list_filter = ['location','genre'] #sort list by x

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name'] 
    fields = ['name']#can change order of things on admin site he
    search_fields = ['name'] #search bar
    list_filter = ['name'] #sort list by x

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Genre, GenreAdmin)
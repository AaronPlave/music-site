from django.contrib import admin
from Profile.models import Profile,Genre,Instruments,SoundCloud

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['location','User'] 
    fields = ['location','User','genre','instruments','quote']#can change order of things on admin site he
    search_fields = ['location','User','genre','instruments'] #search bar
    list_filter = ['location','genre','instruments'] #sort list by x

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name'] 
    fields = ['name']#can change order of things on admin site he
    search_fields = ['name'] #search bar
    list_filter = ['name'] #sort list by x

class InstrumentsAdmin(admin.ModelAdmin):
    list_display = ['name'] 
    fields = ['name']#can change order of things on admin site he
    search_fields = ['name'] #search bar
    list_filter = ['name'] #sort list by x

class SoundCloudAdmin(admin.ModelAdmin):
    list_display = ['url','owner'] 
    fields = ['url','owner']#can change order of things on admin site he
    search_fields = ['url'] #search bar
    list_filter = ['url'] #sort list by x

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Instruments, InstrumentsAdmin)
admin.site.register(SoundCloud, SoundCloudAdmin)
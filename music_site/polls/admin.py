from django.contrib import admin
from polls.models import Poll

class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question'] #can change order of things on admin site here

admin.site.register(Poll, PollAdmin)
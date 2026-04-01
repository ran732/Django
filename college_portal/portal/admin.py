from django.contrib import admin
from portal.models import Notice, Event

class NoticeAdmin(admin.ModelAdmin):
    list_display=('title','description','notice_date')
    
class EventAdmin(admin.ModelAdmin):
    list_display=('name','event_date','details')    

# Register your models here.

admin.site.register(Notice, NoticeAdmin)
admin.site.register(Event, EventAdmin)

from django.shortcuts import render
from portal.models import Notice,Event,Note

from django.utils import timezone

def notice(request):    
    today = timezone.now().date()
    upcoming_notices = Notice.objects.filter(notice_date__gte=today).order_by('notice_date')
    past_notices = Notice.objects.filter(notice_date__lt=today).order_by('-notice_date')
    
    return render(request, "portal/notice.html",{
        "upcoming_notices": upcoming_notices,
        "past_notices": past_notices,
    })

def event(request):
     today = timezone.now().date()
     upcoming_events = Event.objects.filter(event_date__gte=today).order_by('event_date')
     past_events = Event.objects.filter(event_date__lt=today).order_by('-event_date')
     
     return render(request, "portal/event.html",{
         "upcoming_events": upcoming_events,
         "past_events": past_events
     })
    
def notes(request):
    all_notes = Note.objects.all().order_by('-uploaded_at')
    return render(request, "home/notes.html",{"notes":all_notes})
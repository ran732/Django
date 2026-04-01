from django.shortcuts import render
from portal.models import Notice,Event

def notice(request):
    
    notices = Notice.objects.all()
   
    
    return render(request, "portal/notice.html",{"notices": notices,})

def event(request):
    
     events = Event.objects.all()
     
     return render(request, "portal/event.html",{"events":events})
    
    
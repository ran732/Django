from django.urls import path
from portal.views import notice,event
from portal import views

app_name = "portal"

urlpatterns = [
    path('notice',views.notice,name='notice'),
    path('event',views.event,name='event'),
    path("notes",views.notes,name="notes"),
]

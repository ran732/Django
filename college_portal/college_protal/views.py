from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from portal.models import Notice, Event

def homepage(request):
    return HttpResponse("Hello!! This is Ranjeet Singh to help you in your projects.")

def frontpage(request):
    latest_notices = Notice.objects.order_by('-notice_date')[:3]
    upcoming_events = Event.objects.order_by('-event_date')[:3]
    
    context = {
        'latest_notices': latest_notices,
        'upcoming_events': upcoming_events
    }
    return render(request, "home/frontpage.html", context)

def login_view(request):
    if request.method == "POST":
        password = request.POST.get("password")
        username = request.POST.get("username")
        
         # check user credentials
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return render(request, "user/index.html",{ "error" : "Invalid username or password"})
    return render(request, "login/index.html")    


def ragister_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # username already exists
        if User.objects.filter(username=username).exists():
            return render(
                request,
                "login/ragistration.html",
                {"error": "Username already exists"}
            )

        # create user
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # redirect to login page
        return redirect("login")

    return render(request, "login/ragistration.html")
from django.shortcuts import render, HttpResponse
import datetime
from app2.models import employee
# Create your views here.

def welcome(request):
    message = "<h1>you are welcome to my first django project</h1>"
    return HttpResponse(message)

def one(request):
    message = "<h1>you are welcome to my second page</h1>"
    return HttpResponse(message)

def two(request):
    message = "<h1>you are welcome to my third page</h1>"
    return HttpResponse(message)

def three(request):
    message = "<h1>you are welcome to my fourth page</h1>"
    return HttpResponse(message)

def time(request):
    t = datetime.datetime.now()
    t1 = f"<h1> Time is now : {t}</h1>"
    return HttpResponse(t1)

def emp(request):
    name = employee.objects.all()
    
    return render(request, 'day2.html', {"k1":name})
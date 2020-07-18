from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return render(request, "website/welcome.html",
                  {"message":"This data was sent from the view to the template."})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("<h1>About me</h1><p>I am a remote worker programmer</p>")

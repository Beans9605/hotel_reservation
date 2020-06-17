from django.shortcuts import render

# Create your views here.

def home(request) :
    return render(request, "main/home.html")

def reservation(request) :
    return render(request, "main/reservation.html")

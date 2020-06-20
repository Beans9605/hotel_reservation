from django.shortcuts import render
from .models import Users
# Create your views here.

def logout(request):
    request.session.modified = True
    request.session['user'].delete()
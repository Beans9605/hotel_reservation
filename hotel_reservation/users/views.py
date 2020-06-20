from django.shortcuts import render
from .models import Users

def sign_up(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        number=request.POST['number']
        birth=request.POST['birth']
        
        if Users.objects.filter(username = username) is None :
            print("error")

        user=Users(
            username=username,
            password=password,
            number=number,
            birth=birth,
            )
        
        user.save()

def mypage(request):
    if request.session.get['user',True] :
        user = Users.objects.filter(username = request.session['user'])
        reservations = Reservation.objects.filter(user=user)
        context=['user':user, 'reservations':reservations]


# Create your views here.

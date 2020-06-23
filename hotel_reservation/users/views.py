from django.shortcuts import render
from .models import Users

def logout(request):
    request.session.modified = True
    request.session['user'].delete()

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
        context={'user':user, 'reservations':reservations}



def login(request):
    if request.method == 'post':   #post의 방식으로 정보를 가져오겠습니다
        username = request.POST['username']  # username 가져오기
        password = request.PODT['password']  # password 가져오기
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html',{'error': 'username or password is not correct'})
    else:
        return render(request, 'login.html')



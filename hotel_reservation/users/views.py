from django.shortcuts import render, get_object_or_404, redirect
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
    if request.session.get['user', True] :
        user = Users.objects.filter(username = request.session['user'])
        reservations = Reservation.objects.filter(user=user)
        context={'user':user, 'reservations':reservations}



# def login(request):
#     if request.method == 'post':   #post의 방식으로 정보를 가져오겠습니다
#         username = request.POST['username']  # username 가져오기
#         password = request.PODT['password']  # password 가져오기
#         user = auth.authenticate(username = username, password = password)
#         if user is not None:
            # 해당 구문은 auth 모듈을 사용한 걸로, 장고에서 제공하는 유저모델을 사용할때 사용 가능하다.
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html',{'error': 'username or password is not correct'})
#     else:
#         return render(request, 'login.html')


def login(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        # get_object_or_404는 해당 데이터를 검색하고 만약 없을 시에 404 not found 페이지를 보여줌
        user = get_object_or_404(Users, username=username)

        if password == user.password :
            request.session['user'] = user.username
            return redirect('home')

        else :
            context = {'err' : "비밀번호가 틀렸습니다."}
            return redirect('login', context)
        
    else :
        return render(request, "", {"err" : "형식이 잘못됐습니다."})
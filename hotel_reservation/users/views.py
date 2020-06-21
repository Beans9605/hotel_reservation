from django.shortcuts import render

# Create your views here.
#회원가입
#로그인
#로그아웃
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


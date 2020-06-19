from django.shortcuts import render

# Create your views here.
def mypage(request):
<<<<<<< HEAD
    return render(request, "mypage/mypage.html")
=======
    return render (request, "myPage/mypage.html")

def signup(request):
    return render (request, "login/signup.html")
    
def signin(request):
    return render (request, "login/signin.html")
>>>>>>> aeea75335779ce06d94068c7392260312ac7e7c0

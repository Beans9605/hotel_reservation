from django.shortcuts import render

# Create your views here.
def mypage(request):
    return render (request, "myPage/mypage.html")

def signup(request):
    return render (request, "login/signup.html")
    
def signin(request): 
    context={'A':A, "B":B}
    return render (request, "login/signin.html", context)

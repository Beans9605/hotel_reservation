from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('mypage/', views.mypage, name="mypage"),   
=======
    path('mypage/', views.mypage, name="mypage"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
>>>>>>> aeea75335779ce06d94068c7392260312ac7e7c0
]

from django.urls import path
from . import views

urlpatterns = [
    path('mypage/', views.mypage, name="mypage"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('sign2/', views.signup, name="signup2"),
]

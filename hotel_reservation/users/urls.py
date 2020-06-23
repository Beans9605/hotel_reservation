
from django.urls import path, include
from . import views

urlpatterns = [
    path("<pk:int>/", views.mypage, name="mypage"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.sign_up, name='signup'),
]

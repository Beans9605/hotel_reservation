from django.urls import path, include
from . import views
urlpatterns = [
    path('introduction/', views.introduction, name="introduction"),
    path('introdetail/', views.introdetail, name="introdetail"),
    path('reservation/', views.reservation_home, name="reservation"),
    path('location/', views.location, name="location"),
       
]

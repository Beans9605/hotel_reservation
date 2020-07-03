from django.urls import path, include
from . import views
urlpatterns = [

    path('reservation_home/', views.reservation_home, name="reservation_home"),
    path('reservation/', views.reservation, name="reservation"),
    path('reservation_modify/', views.reservation_modify, name="reservation_modify"),
    path('reservation_delete/<int:pk>', views.reservation_delete, name="reservation_delete"),
    path('introduction/', views.introduction, name="introduction"),
    path('introdetail/', views.introdetail, name="introdetail"),
    path('reservation/', views.reservation_home, name="reservation"),
    path('location/', views.location, name="location"),

]

from django.urls import path, include
from . import views
urlpatterns = [
<<<<<<< HEAD
    path('introduction/', views.introduction, name="introduction"),
    path('introdetail/', views.introdetail, name="introdetail"),
    path('reservation/', views.reservation_home, name="reservation"),
    path('location/', views.location, name="location"),
       
=======
    path('reservation/', views.reservation_home, name="reservation"),
    path('introduction/', views.introduction, name="introduction")
>>>>>>> cb8a8dbc160bd359c181c6a6e797b816b51405bb
]

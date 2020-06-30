from django.urls import path, include
from . import views
urlpatterns = [
    path('reservation/', views.reservation_home, name="reservation"),
    path('introduction/', views.introduction, name="introduction")
]

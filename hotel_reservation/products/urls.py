from django.urls import path, include
from . import views
urlpatterns = [
    path('introduction/', views.introduction, name="introduction")
]

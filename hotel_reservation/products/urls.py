from django.urls import path, include
from . import views
urlpatterns = [
    path('reservation/', views.reservation_home, name="reservation"),
]

from django.db import models
from users.models import Users
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=25)
    how_many_accepts = models.IntegerField(default=2)
    description = models.TextField()
    price=models.IntegerField()
    

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Reservation(models.Model) :
    # 방을 예약한 유저 정보
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    # 방에 대한 정보
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    # 예약 선정한 날
    reservation_date = models.DateField(default=timezone.now)
    # 예약 신청한 날 저장 = create_at
    request_date = models.DateField(auto_now_add=True)


    # 마지막으로 머무는 날
    enday_date = models.DateField(default=timezone.now)

    # 몇일 지내는지
    stay_day = models.IntegerField(default=1)

    # 몇 명이서 지내는지
    how_many_users = models.IntegerField(default=1)


from django.shortcuts import render, get_object_or_404
from datetime import date, datetime, timedelta
from .models import Product, Reservation
from users.models import Users
# Create your views here.

def reservation_home(request) :
    return render(request, 'reservation/reservation_home.html')

def reservation_user(request) :
    if request.method == "POST" and request.session.get('user') :
        reservation_date = request.POST['reservation_date']
        enday_date = request.POST['enday_date']
        user = request.session['user']
        how_many_people = request.POST['people']
        # 알맞는 date 형태로 만들어줌
        enday_date = datetime.strptime(enday_date, "%Y-%m-%d")
        reservation_date = datetime.strptime(reservation_date, "%Y-%m-%d")
        # 최초 시작 날짜와 끝나는 날짜를 계산해서 일수를 계산
        stay_day = int((enday_date-reservation_date).days)


        # 랜덤 배정
        products_all = Product.object.all()
        search_empty_room = Product()

        # 현재 내가 예약한 날짜에 예약이 잡혀있는 확인
        for i in range(0, stay_day) :
            search_date = reservation_date + timedelta(days=i)
            exReser = Reservation.objects.filter(reservation_day=search_date)
            # 예약이 있는 룸은 삭제 -instant field-
            for re in exReser :
                if re in products_all :
                    products_all.Remove(re.product)
        # 남는 룸에서 검색
        for product in products_all() :
            # 비어있는 룸을 이미 선택했을 경우
            if search_empty_room :
                # 만약 남아있는 룸이랑 더 인원이 비슷한 룸이 있다면 대체
                if how_many_people < product.how_many_accepts  and product.how_many_accepts < search_empty_room.how_many_accepts :
                    search_empty_room = product
            # 룸이 선택 되지 않을때 선택
            elif product.how_many_accepts >= how_many_people :
                search_empty_room = product
        # 유저와 룸이 존재하는지 확인
        user = get_object_or_404(Users, username=user)

        if enday_date == reservation_date :
            return render(request, "main/home.html", {"err" : "err_date"})
        elif search_empty_room.how_many_accepts < how_many_people :
            return render(request, "main/home.html", {"err" : "This is not correct"})
        else :
            reservation = Reservation (
                reservation_date = reservation_date,
                enday_date = enday_date,
                how_many_users = how_many_people,
                stay_day = stay_day,
                product = search_empty_room,
                user = user
            )

            reservation.save()

            return render(request, "")
    else :
        return render(request, "")


def reservation_modify(request) :
    if request.method == "POST" :
        reservation_pk = request.POST['reservation_pk']
        reservation_date = request.POST['reservation_date']
        enday_date = request.POST['enday_date']
        enday_date = datetime.strptime(enday_date, "%Y-%m-%d")
        reservation_date = datetime.strptime(reservation_date, "%Y-%m-%d")
        current_date = datetime.now(current_date, "%Y-%m-%d")
        user = request.POST['user']
        user = get_object_or_404(Users, username=user)

        reservation = get_object_or_404(Reservation, pk=reservation_pk)

        if reservation.user == user :
            product = reservation.product
            return render(request, "products/mod")

def introduction(request) :
    return render(request, "introduction/introduction.html")


def introdetail(request) :
    return render(request, "introduction/introdetail.html")

def location(request) :
    return render(request, "location/location.html")

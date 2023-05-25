from .models import Advertisment, User, Mark, City, Models, CarCat, Color, Transmission, Handlebar, Wheeldrive, Engine, Bodywork, DamageStatus, Car, Metro, TypeOfAd, AdStatus
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required


def edit_user(request, user_id):
    user = get_object_or_404(User, id_User=user_id)
    if request.method == 'POST':
        user.log_User = request.POST['username']
        user.pass_User = request.POST['password']
        user.phone_User = request.POST['phone']
        user.email_User = request.POST['email']
        user.city_User = City.objects.get(id_City=request.POST['city'])
        user.name_User = request.POST['first_name']
        user.surname_User = request.POST['last_name']
        user.birth_User = request.POST['birth_date']
        user.save()
        return redirect('profile')
    else:
        # Если пользователь просто зашел на страницу, отображаем форму для редактирования данных
        cities = City.objects.all()
        return render(request, 'edit_user.html', {'user': user, 'cities': cities})


def index(request):
    ads = Advertisment.objects.all()
    return render(request, 'index.html',  {'ads': ads})


def create(request):
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, id_User=user_id)
    if request.method == 'POST':
        vin_Car = request.POST.get('vin_Car')
        model_Car_id = request.POST.get('model_Car')
        year_Car = request.POST.get('year_Car')
        statenum_Car = request.POST.get('statenum_Car')
        cat_Car_id = request.POST.get('cat_Car')
        color_Car_id = request.POST.get('color_Car')
        trans_Car_id = request.POST.get('trans_Car')
        handle_Car_id = request.POST.get('handle_Car')
        wheel_Car_id = request.POST.get('wheel_Car')
        engine_Car_id = request.POST.get('engine_Car')
        numown_Car = request.POST.get('numown_Car')
        body_Car_id = request.POST.get('body_Car')
        damage_Car_id = request.POST.get('damage_Car')
        photo_Car = request.FILES.get('photo_Car')
        user_Car_id = request.POST.get('user_Car')

        user_Car = get_object_or_404(User, id_User=user_Car_id)

        car = Car(
            vin_Car=vin_Car,
            model_Car_id=model_Car_id,
            year_Car=year_Car,
            statenum_Car=statenum_Car,
            cat_Car_id=cat_Car_id,
            color_Car_id=color_Car_id,
            trans_Car_id=trans_Car_id,
            handle_Car_id=handle_Car_id,
            wheel_Car_id=wheel_Car_id,
            engine_Car_id=engine_Car_id,
            numown_Car=numown_Car,
            body_Car_id=body_Car_id,
            damage_Car_id=damage_Car_id,
            photo_Car=photo_Car,
            user_Car=user_Car
        )
        car.save()
        return redirect('create_ad')
    else:
        models = Models.objects.all()
        carcats = CarCat.objects.all()
        colors = Color.objects.all()
        transmissions = Transmission.objects.all()
        handles = Handlebar.objects.all()
        wheeldrives = Wheeldrive.objects.all()
        engines = Engine.objects.all()
        bodyworks = Bodywork.objects.all()
        damagestatuses = DamageStatus.objects.all()
        return render(request, 'create.html', {'user': user, 'models': models, 'carcats': carcats, 'colors': colors,
                                               'transmissions': transmissions, 'handles': handles,
                                               'wheeldrives': wheeldrives, 'engines': engines, 'bodyworks': bodyworks,
                                               'damagestatuses': damagestatuses})


def create_ad(request):
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, id_User=user_id)

    if request.method == 'POST':
        comm_Ad = request.POST.get('comm_Ad')
        metro_Ad_id = request.POST.get('metro_Ad')
        car_Ad_id = request.POST.get('car_Ad')
        price_Ad = request.POST.get('price_Ad')
        user_Ad_id = request.POST.get('user_Ad')
        date_Ad = request.POST.get('date_Ad')
        status_Ad_id = 1
        status_Ad = get_object_or_404(AdStatus, pk=status_Ad_id)
        type_Ad_id = 1
        type_Ad = get_object_or_404(TypeOfAd, pk=type_Ad_id)
        ad = Advertisment(
            comm_Ad=comm_Ad,
            loc_Ad_id=metro_Ad_id,
            car_Ad_id=car_Ad_id,
            price_Ad=price_Ad,
            user_Ad_id=user_Ad_id,
            date_Ad=date_Ad,
            status_Ad=status_Ad,
            type_Ad=type_Ad
        )
        ad.save()
        return redirect('home')

    else:
        cars = Car.objects.filter(user_Car=user)
        cities = City.objects.all()
        metros = Metro.objects.all()
        return render(request, 'create_ad.html', {'cities': cities, 'metros': metros, 'cars': cars, 'user': user})


def brands(request):
    marks = Mark.objects.all()
    return render(request, 'brands.html', {'marks':marks})


def profile(request):
    user_id = request.session.get('user_id')
    if user_id is not None:
        user = User.objects.get(id_User=user_id)
        return render(request, 'profile.html', {'user': user})
    else:
        return redirect('guest')


def guest(request):
    return render(request, 'guest.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(log_User=username, pass_User=password)
        except User.DoesNotExist:
            user = None
        if user is not None:
            request.session['user_id'] = user.id_User
            return redirect('profile')
        else:
            HttpResponse("Неправильный логин или пароль")
    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('home')


def error(request):
    return render(request, 'error.html', {'message': 'Ошибка!'})


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    ads = Advertisment.objects.filter(car_Ad=car_id)
    context = {'car': car, 'ads': ads}
    return render(request, 'car_detail.html', context)
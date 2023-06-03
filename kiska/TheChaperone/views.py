from datetime import timezone, datetime

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from .models import Advertisment, User, Mark, City, Models, CarCat, UserStatus, Roles, Color, Transmission, Handlebar, Wheeldrive, Engine, Bodywork, DamageStatus, Car, Metro, AdStatus
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.pdfbase.ttfonts import TTFont, pdfmetrics


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

    if user_id is None:
        return redirect('login')

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
        user_Car_id = user_id

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
        user_Ad_id = user.id_User
        date_Ad = datetime.now().strftime('%Y-%m-%d')
        status_Ad_id = 1
        status_Ad = get_object_or_404(AdStatus, pk=status_Ad_id)
        contact_Ad = 'https://web.telegram.org/k/#@' + request.POST.get('contact_Ad')
        ad = Advertisment(
            comm_Ad=comm_Ad,
            loc_Ad_id=metro_Ad_id,
            car_Ad_id=car_Ad_id,
            price_Ad=price_Ad,
            user_Ad_id=user_Ad_id,
            date_Ad=date_Ad,
            status_Ad=status_Ad,
            contact_Ad=contact_Ad,
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
    ads = Advertisment.objects.filter(user_Ad=user_id)
    if user_id is not None:
        user = User.objects.get(id_User=user_id)
        return render(request, 'profile.html', {'user': user, 'ads': ads})
    else:
        return redirect('login')


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
            if user.status_User_id == 2:
                return render(request, 'login.html', {'message': 'Ваш аккаунт заблокирован'})
            else:
                request.session['user_id'] = user.id_User
                return redirect('profile')
        else:
            return render(request, 'login.html', {'message': 'Неправильный логин или пароль'})
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
    context = {'car': car, 'ads': ads, 'session': request.session.get('user_id', None)}
    return render(request, 'car_detail.html', context)


def registration(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        phone = request.POST['phone']
        email = request.POST['email']
        city = City.objects.get(id_City=request.POST['city'])
        name = request.POST['name']
        surname = request.POST['surname']
        birth = request.POST['birth']
        role_id = 1
        role = get_object_or_404(Roles, pk=role_id)
        status_id = 1
        status = get_object_or_404(UserStatus, pk=status_id)

        user = User(log_User=login, pass_User=password, phone_User=phone,
                    email_User=email, city_User=city, name_User=name, surname_User=surname,
                    birth_User=birth, status_User=status, role_User=role)
        user.save()
        request.session['user_id'] = user.id_User
        return redirect('profile')
    else:
        cities = City.objects.all()
        return render(request, 'registration.html', {'cities': cities})


def ad_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        ads = Advertisment.objects.filter(date_Ad__range=[start_date, end_date])
        ad_count = ads.count()

        return render(request, 'ad_report_form.html', {
            'ads': ads,
            'ad_count': ad_count,
            'date': datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        })
    else:
        return render(request, 'ad_report_form.html')


def ad_report_pdf(request):
    font_path = '/Users/kiska/Documents/Документы — KISKA MACBOOK/PyCharmProjects/TheChaperone/kiska/TheChaperone/static/FreeSans.ttf'
    pdfmetrics.registerFont(TTFont('MyFont', font_path))
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        ads = Advertisment.objects.filter(date_Ad__range=[start_date, end_date])
        ad_count = ads.count()

        # Create PDF document
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="ad_report_{datetime.now(timezone.utc).strftime("%Y-%m-%d")}.pdf"'

        doc = SimpleDocTemplate(response, pagesize=letter)
        elements = []

        styles = getSampleStyleSheet()
        header = Paragraph('TheChaperone', styles['Heading1'])
        elements.append(header)

        # Add table to PDF
        data = [[u'Временной промежуток', u'Количество созданных объявлений'],
                [f'{start_date} - {end_date}', ad_count]]
        table = Table(data)
        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'MyFont'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 0), (-1, 0), colors.slategray),  # верхнее поле cветлосерое
            ('BACKGROUND', (0, 1), (-1, 1), colors.lightgreen),  # нижнее поле светлозеленое
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ]))
        elements.append(table)

        # Build PDF
        doc.build(elements)
        return response
    else:
        return render(request, 'ad_report_pdf.html')


def brand_view(request, name_Mark):
    mark = Mark.objects.get(name_Mark=name_Mark)
    cars = Car.objects.filter(model_Car__in=Models.objects.filter(name_Mark=mark))
    ads = Advertisment.objects.filter(car_Ad__in=cars)
    context = {'ads': ads}
    return render(request, 'brand.html', context)


def edit_ad(request, ad_id):
    ad = get_object_or_404(Advertisment, id_Ad=ad_id)
    if request.method == 'POST':
        ad.comm_Ad = request.POST.get('description')
        ad.loc_Ad.name_Met = request.POST.get('location')
        ad.price_Ad = request.POST.get('price')
        ad.contact_Ad = request.POST.get('contacts')
        ad.save()
        return redirect('profile') # перенаправляем пользователя на страницу с его объявлениями
    else:
        ad = Advertisment.objects.get(id_Ad=ad_id)
        metros = Metro.objects.all()
        return render(request, 'edit_ad.html', {'ad': ad, 'metros': metros})


def about(request):
    ads = Advertisment.objects.all()
    ad_count = ads.count()
    context = {'ad_count': ad_count}
    return render(request, 'about.html', context)


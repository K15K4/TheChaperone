from django.db import models
from .services import photo_сar
# Create your models here.


class Mark(models.Model):
    id_Mark = models.AutoField(primary_key=True)
    name_Mark = models.CharField(max_length=50)
    photo_Mark = models.ImageField(upload_to='photo_mark', null=True, blank=True)

    def __str__(self):
        return self.name_Mark

    class Meta:
        db_table = "Mark"


class Models(models.Model):
    id_Mod = models.AutoField(primary_key=True)
    name_Mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    name_Mod = models.CharField(max_length=50)

    def __str__(self):
        return self.name_Mod

    class Meta:
        db_table = "Models"


class Roles(models.Model):
    id_Roles = models.AutoField(primary_key=True)
    name_Roles = models.CharField(max_length=50)

    def __str__(self):
        return self.name_Roles

    class Meta:
        db_table = "Roles"


class CarCat(models.Model):
    id_CarCat = models.AutoField(primary_key=True)
    name_Cat = models.CharField(max_length=50)

    def __str__(self):
        return self.name_Cat

    class Meta:
        db_table = "CarCat"


class City(models.Model):
    id_City = models.AutoField(primary_key=True)
    name_City = models.CharField(max_length=50)

    def __str__(self):
        return self.name_City

    class Meta:
        db_table = "City"


class Metro(models.Model):
    id_Met = models.AutoField(primary_key=True)
    name_City = models.ForeignKey(City, on_delete=models.CASCADE)
    name_Met = models.CharField(max_length=50)

    def __str__(self):
        return self.name_Met

    class Meta:
        db_table = "Metro"


class Color(models.Model):
    id_Color = models.AutoField(primary_key=True)
    name_Color = models.CharField(max_length=50)

    def __str__(self):
        return self.name_Color

    class Meta:
        db_table = "Color"


class Transmission(models.Model):
    id_Trans = models.AutoField(primary_key=True)
    name_Trans = models.CharField(max_length=50)

    def __str__(self):
        return self.name_Trans

    class Meta:
        db_table = "Transmission"


class Handlebar(models.Model):
    id_Hand = models.AutoField(primary_key=True)
    name_Hand = models.CharField(max_length=50)

    def __str__(self):
        return self.name_Hand

    class Meta:
        db_table = "Handlebar"


class Wheeldrive(models.Model):
    id_Wheel = models.AutoField(primary_key=True)
    name_Wheel = models.CharField(max_length=50)

    def __str__(self):
        return self.name_Wheel

    class Meta:
        db_table = "Wheeldrive"


class Bodywork(models.Model):
    id_Body = models.AutoField(primary_key=True)
    name_Body = models.CharField(max_length=50)

    def __str__(self):
        return self.name_Body

    class Meta:
        db_table = "Bodywork"


class DamageStatus(models.Model):
    id_Dam = models.AutoField(primary_key=True)
    name_Dam = models.CharField(max_length=50)

    def __str__(self):
        return self.name_Dam

    class Meta:
        db_table = "DamageStatus"


class TypeOfAd(models.Model):
    id_TypeAd = models.AutoField(primary_key=True)
    name_TypeAd = models.CharField(max_length=50)

    def __str__(self):
        return self.name_TypeAd

    class Meta:
        db_table = "TypeOfAd"


class AdStatus(models.Model):
    id_AdStat = models.AutoField(primary_key=True)
    name_AdStat = models.CharField(max_length=50)

    def __str__(self):
        return self.name_AdStat

    class Meta:
        db_table = "AdStatus"


class FuelType(models.Model):
    id_Fuel = models.AutoField(primary_key=True)
    name_Fuel = models.CharField(max_length=50)

    def __str__(self):
        return self.name_Fuel

    class Meta:
        db_table = "FuelType"


class TypeOfEngine(models.Model):
    id_TypeEng = models.AutoField(primary_key=True)
    name_TypeEng = models.CharField(max_length=50)

    def __str__(self):
        return self.name_TypeEng

    class Meta:
        db_table = "TypeOfEngine"


class Engine(models.Model):
    id_Engine = models.AutoField(primary_key=True)
    name_Engine = models.CharField(max_length=50)
    hp_Engine = models.IntegerField(default=1)
    fuel_Engine = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    type_Engine = models.ForeignKey(TypeOfEngine, on_delete=models.CASCADE)
    capacity_Engine = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.name_Engine} {self.hp_Engine} {self.capacity_Engine}"

    class Meta:
        db_table = "Engine"


class User(models.Model):
    id_User = models.AutoField(primary_key=True)
    log_User = models.CharField(max_length=50)
    pass_User = models.CharField(max_length=50)
    phone_User = models.CharField(max_length=50)
    email_User = models.CharField(max_length=50)
    city_User = models.ForeignKey(City, on_delete=models.CASCADE)
    name_User = models.CharField(max_length=50)
    surname_User = models.CharField(max_length=50)
    birth_User = models.DateField()
    role_User = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.log_User} {self.pass_User} {self.phone_User} {self.email_User} {self.name_User} {self.surname_User} {self.birth_User}"

    class Meta:
        db_table = "User"


class Car(models.Model):
    id_Car = models.AutoField(primary_key=True)
    vin_Car = models.CharField(max_length=50)
    model_Car = models.ForeignKey(Models, on_delete=models.CASCADE)
    year_Car = models.DateField()
    statenum_Car = models.CharField(max_length=50)
    cat_Car = models.ForeignKey(CarCat, on_delete=models.CASCADE)
    color_Car = models.ForeignKey(Color, on_delete=models.CASCADE)
    trans_Car = models.ForeignKey(Transmission, on_delete=models.CASCADE)
    handle_Car = models.ForeignKey(Handlebar, on_delete=models.CASCADE)
    wheel_Car = models.ForeignKey(Wheeldrive, on_delete=models.CASCADE)
    engine_Car = models.ForeignKey(Engine, on_delete=models.CASCADE)
    numown_Car = models.IntegerField(default=1)
    body_Car = models.ForeignKey(Bodywork, on_delete=models.CASCADE)
    mileage_Car = models.IntegerField(default=1)
    damage_Car = models.ForeignKey(DamageStatus, on_delete=models.CASCADE)
    photo_Car = models.ImageField(upload_to='photo_сar', null=True, blank=True)
    user_Car = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vin_Car} {self.year_Car} {self.statenum_Car} {self.numown_Car} {self.mileage_Car}"

    class Meta:
        db_table = "Car"


"""class Photo(models.Model):
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE, primary_key=True)
    id_photo = models.ImageField(upload_to=get_path_upload_photo_workers, blank=True, null=True, primary_key=True)"""


class Advertisment(models.Model):
    id_Ad = models.AutoField(primary_key=True)
    user_Ad = models.ForeignKey(User, on_delete=models.CASCADE)
    car_Ad = models.ForeignKey(Car, on_delete=models.CASCADE)
    comm_Ad = models.CharField(max_length=90)
    type_Ad = models.ForeignKey(TypeOfAd, on_delete=models.CASCADE)
    date_Ad = models.DateField()
    loc_Ad = models.ForeignKey(Metro, on_delete=models.CASCADE)
    status_Ad = models.ForeignKey(AdStatus, on_delete=models.CASCADE)
    price_Ad = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.comm_Ad} {self.date_Ad} {self.price_Ad}"

    class Meta:
        db_table = "Advertisment"

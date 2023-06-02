from .models import Mark, Models, Roles, CarCat, City, Metro, Color, Transmission, Handlebar, Wheeldrive, Bodywork, DamageStatus, UserStatus, AdStatus, FuelType, TypeOfEngine, Engine, User, Car, Advertisment
from django.contrib import admin


@admin.register(Mark)
class DepartmentsAdmin(admin.ModelAdmin):
    pass


@admin.register(Models)
class PositionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Roles)
class GendersAdmin(admin.ModelAdmin):
    pass


@admin.register(CarCat)
class BrandsAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class ModelsAdmin(admin.ModelAdmin):
    pass


@admin.register(Metro)
class CarsAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class WorkersAdmin(admin.ModelAdmin):
    pass


@admin.register(Transmission)
class StatusesAdmin(admin.ModelAdmin):
    pass


@admin.register(Handlebar)
class AccessAdmin(admin.ModelAdmin):
    pass


@admin.register(Wheeldrive)
class AccessAdmin(admin.ModelAdmin):
    pass


@admin.register(Bodywork)
class AccessAdmin(admin.ModelAdmin):
    pass


@admin.register(DamageStatus)
class AccessAdmin(admin.ModelAdmin):
    pass


@admin.register(UserStatus)
class AccessAdmin(admin.ModelAdmin):
    pass


@admin.register(AdStatus)
class AccessAdmin(admin.ModelAdmin):
    pass


@admin.register(FuelType)
class AccessAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeOfEngine)
class AccessAdmin(admin.ModelAdmin):
    pass


@admin.register(Engine)
class AccessAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class AccessAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class AccessAdmin(admin.ModelAdmin):
    pass


@admin.register(Advertisment)
class AccessAdmin(admin.ModelAdmin):
    pass

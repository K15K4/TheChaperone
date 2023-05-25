from django.urls import path
from .views import index, brands, create, profile, login, logout, guest, edit_user, create_ad, car_detail

urlpatterns = [
    path('', index, name='home'),
    path('create', create, name='create'),
    path('brands', brands, name='brands'),
    path('profile', profile, name='profile'),
    path('login', login, name='login'),
    path('logout/', logout, name='logout'),
    path('guest/', guest, name='guest'),
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
    path('create_ad', create_ad, name='create_ad'),
    path('car/<int:car_id>/', car_detail, name='car_detail'),

]
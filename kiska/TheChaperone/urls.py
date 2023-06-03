from django.urls import path
from .views import index, ad_report_pdf, brands, create, profile, login, \
    logout, guest, edit_user, create_ad, car_detail, registration, ad_report, \
    brand_view, edit_ad, about

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
    path('registration', registration, name='registration'),
    path('ad_report_pdf', ad_report_pdf, name='ad_report_pdf'),
    path('ad_report_form', ad_report, name='ad_report'),
    path('brand/<str:name_Mark>/', brand_view, name='brand'),
    path('edit_ad/<int:ad_id>/', edit_ad, name='edit_ad'),
    path('about', about, name='about'),


]
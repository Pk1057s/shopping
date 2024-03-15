from django.contrib import admin
from django.urls import path, include
from accounts import views

app_name='ac'
urlpatterns = [
    path('serach/', views.login_view, name='search'),
    path('login/', views.login_view, name='login_search'),
    path('signin/', views.signup_view, name='signup_view'),
    path('', views.login_view, name='login_view'),
]

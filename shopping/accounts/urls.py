from django.contrib import admin
from django.urls import path, include
from accounts import views

app_name='ac'
urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('login_submit/', views.login_submit, name='login_submit'),
    path('signup/', views.signup_view, name='signup_view'),
    path('signup_submit/', views.signup_submit, name='signup_submit'),
    path('serach/', views.login_view, name='search'),
]

from django.contrib import admin
from django.urls import path, include
from . import views

app_name='md'
urlpatterns = [
    path('', views.render_extracted_tag, name='render_extracted_tag'), 
    
]
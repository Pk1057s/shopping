from django.urls import path
from . import views
from modeling import search_modeling as model_views

app_name='pr' 
urlpatterns = [
    path('', views.index, name='index'),
    path('input/', views.input_manage, name='input'),
    path('search/', views.search_results, name='search_results'),
    path('p/', views.person_tag, name='person_tag'),
    path('pr/', views.pr_tag, name='pr_tag'),
    path('detail/<str:urls>/', views.detail_view, name='detail'),
    
    #path(''),
]
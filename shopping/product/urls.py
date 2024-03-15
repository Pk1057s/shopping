from django.urls import path
from . import views

app_name='pr' 
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_results, name='search_results'),
    path('p/', views.person_tag, name='person_tag'),
    path('pr/', views.pr_tag, name='pr_tag'),
    #path('test/', views.test),
    path('login_test/', views.login_test, name='login_test'),
    path('logout/', views.logouts, name='logout'),
]
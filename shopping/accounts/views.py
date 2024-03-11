from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

def login_view(response):

    return render(response, "login.html")
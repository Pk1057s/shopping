from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from accounts.models import User
from accounts.forms import LoginForm, SignupForm
from django.urls import reverse

def index_view(request):
    print("aaa")
    return render(request, "indexs.html")

def login_view(request):

    return render(request, "login.html")

def login_submit(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # print(username)
            # print(role)
            info =f", {username}, {password}"
            # 해당하는 사용자가 있는지 확인
            is_auth = authenticate(username=username, password=password)
            print('11111111111111111111111111111')
            # 사용자가 존재하면 로그인 후 메인페이지로 이동
            if is_auth:
                print('22222222222222222222222222222222')
                login(request, is_auth)
                return render(request, "indexs.html")
            # 없으면 로그인 실패 문구 출력
            else:
                print('3333333333333333333333333333333')
                message = "fail" + info
                return render(request, 'login.html', {'message':message})
        else:
            print('4444444444444444444444444444')
            print(form)
            return render(request, "indexs.html")

def login_search(request):
    
    return render(request, "login.html")

def signup_view(request):

    return render(request, "signup.html")

def signup_submit(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            person_name = form.cleaned_data['person_name']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']

            user = User.objects.create_user(username=username, password=password, role='admin', person_name=person_name, phone_number=phone_number, address=address)
            login(request, user)
            message = f"{username} is signedup"
            return render(request,'login.html', {'message':message})
        else :
            return render(request, "signup.html")

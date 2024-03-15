from django.shortcuts import render, HttpResponse,redirect
from .models import Tag, Product
from accounts.models import User
## Test################################################################
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
def logouts(request):
    if 'username' in request.session:
        logout(request)
        request.session.flush()
    return render(request, 'index.html')

def login_test(request):
    if request.method == 'POST':
        username = request.POST['username']
        #user = User.objects.filter(person_name__icontains='t')
        user = User.objects.get(username=username)
        #user = authenticate(username=username)
        if user is not None:
            request.session['username'] = username
            request.session['is_login'] = username
            login(request, user)
            print('로그인 완료')
            return render(request, 'index.html')
    else:
        form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})
################################################################
def index(request):
    print(request.session.get('username'))
    if request.session.get('username'):
        username = request.session.get('username')
        return render(request, 'index.html', {'username': username})
    else:
        return render(request,'index.html')

def person_tag(request):
    if request.method == "POST":
        person_name = request.POST.get('person_name')
        tag = request.POST.get('tag')
        genre = request.POST.get('genre')
        print(person_name, tag, genre)
        if person_name and tag and genre:
            new_tag = Tag.objects.create(person_name=person_name, tag=tag, genre=genre)
            #new_tag.save()
        index(request)

def pr_tag(request):
    if request.method=="POST":
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        tag = request.POST.get('tag')
        genre = request.POST.get('genre')
        if product_name and tag and genre and price and discount:
            new_tag = Product.objects.create(product_name=product_name,price=price,discount=discount, tag=tag, genre=genre)
            #new_tag.save()
        index(request)
    else:
        index(request) 

def search_results(request):
    if request.method == "POST":
        search = request.POST.get('Search')
        products = Product.objects.filter(product_name__icontains=search)
        return render(request,'index.html',{'products': products,'query': search})
    else:
        index(request)


from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .models import SearchData, Product
from accounts.models import User
from django.db.models import Q


def index(request):
    data = Product.objects.all()
    return render(request, 'index.html', {'data': data})


def input_manage(request):
    return render(request, 'input.html')


def person_tag(request):
    if request.method == "POST":
        person_name = request.POST.get('person_name')
        tag = request.POST.get('tag')
        genre = request.POST.get('genre')
        print(person_name, tag, genre)
        if person_name and tag and genre:
            new_tag = SearchData.objects.create(
                person_name=person_name, tag=tag, genre=genre)
            # new_tag.save()
        return render(request, 'index.html')


def pr_tag(request):
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        tag = request.POST.get('tag')
        genre = request.POST.get('genre')
        if product_name and tag and genre and price and discount:
            new_tag = Product.objects.create(
                product_name=product_name, price=price, discount=discount, tag=tag, genre=genre)
            # new_tag.save()
        return redirect(reverse('pr:index'))
    else:
        return render(request, 'index.html')


def search_results(request):
    if request.method == "POST":
        search = request.POST.get('Search')
        # products = Product.objects.filter(product_name__icontains=search)
        products = Product.objects.filter(
            Q(product_name__icontains=search) |
            Q(tag__icontains=search) |
            Q(genre__icontains=search)
        ).distinct()
        if products:
            return render(request, 'index.html', {'products': products, 'query': search})
        else: 
            render(request, 'index.html')
    else:
        return render(request, 'index.html')


def detail_view(request, urls):
    data = Product.objects.get(urls=urls)
    username = request.session.get('user_id')
    if User.objects.filter(username = username).exists():
        SearchData.objects.create(tag = data.tag, genre = data.genre ,username = username, create_at = datetime.now(pytz.timezone('Asia/Seoul')))
    return render(request, 'detail.html', {'data': data})


from datetime import datetime
import pytz

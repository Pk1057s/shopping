from django.shortcuts import render, HttpResponse
from .models import Tag, Product

def index(request):
    return render(request,'index.html')





def person_tag(request):
    if request.method == "POST":
        person_name = request.POST.get('person_name')
        tag = request.POST.get('tag')
        genre = request.POST.get('genre')
        print(person_name, tag, genre)
        if person_name and tag and genre:
            new_tag = Tag.objects.create(person_name=person_name, tag=tag, genre=genre)
            new_tag.save()
        return render(request,'index.html')

def pr_tag(request):
    if request.method=="POST":
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        tag = request.POST.get('tag')
        genre = request.POST.get('genre')
        if product_name and tag and genre and price and discount:
            new_tag = Product.objects.create(product_name=product_name,price=price,discount=discount, tag=tag, genre=genre)
            new_tag.save()
        return render(request,'index.html') 
    else:
        return render(request,'index.html') 

def search_results(request):
    if request.method == "POST":
        search = request.POST.get('Search')
        products = Product.objects.filter(product_name__icontains=search)
        return render(request,'index.html',{'products': products,'query': search})
    else:
        return render(request,'index.html')


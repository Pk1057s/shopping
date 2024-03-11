from django.shortcuts import render, HttpResponse
from .models import Tag, Product
def products(request):
    return render(request,'index.html')


def search_results(request):
    query = request.GET.get('Search')
    return render(request,'Test.html',{'query': query})

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
    person_name = request.POST.get('person_name')
    price = request.POST.get('price')
    discount = request.POST.get('discount')
    tag = request.POST.get('tag')
    genre = request.POST.get('genre')
    if person_name and tag and genre and price and discount:
        new_tag = Product.objects.create(person_name=person_name,price=price,discount=discount, tag=tag, genre=genre)
        new_tag.save()
    return render(request,'index.html')

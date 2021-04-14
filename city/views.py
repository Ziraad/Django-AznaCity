from itertools import chain

from django.shortcuts import render

from .models import City, Place, Soghat, Category, Martyrs, Hotel


def homepage(request):
    categorys = Category.objects.filter(parent=None)
    print(categorys)
    places = Place.objects.all()
    city = City.objects.get(name='ازنا')
    gardesh = Place.objects.filter(category__slug='گردشگری')[:4]
    tarikhi = Place.objects.filter(category__slug='تاریخی-مذهبی')[:4]
    karkhane = Place.objects.filter(category__slug='کارخانجات')[:4]
    roosta = Place.objects.filter(category__slug='روستا')[:4]
    soghats = Soghat.objects.all()
    martyrs = Martyrs.objects.all()
    hotel_res = Hotel.objects.all()
    for i in places:
        des = i.description[:50]
    context = {
        'categorys': categorys,
        'places': places,
        'city': city,
        'gardesh': gardesh,
        'tarikhi': tarikhi,
        'karkhane': karkhane,
        'roosta': roosta,
        'soghats': soghats,
        'martyrs': martyrs,
        'hotel': hotel_res,
    }
    return render(request, 'city/home_page.html', context=context)


# def all_gardesh(request):
#     all_gardeshgari = Place.objects.filter(category='T')
#     context = {
#         'all_gardeshgari': all_gardeshgari
#
#     }
#     return render(request, 'city/category.html', context=context)


def place_details(request, slug):
    categorys = Category.objects.filter(parent=None)
    list1 = [Place, Soghat]
    for li in list1:
        product1 = li.objects.filter(slug=slug)
        if product1.exists():
            product2 = li.objects.get(slug=slug)
    context = {
        'place': product2,
        'categorys': categorys,
    }
    return render(request, 'city/places_details.html', context=context)


def category(request, slug):
    categorys = Category.objects.filter(parent=None)
    place = Place.objects.filter(category__slug=slug)
    soghat = Soghat.objects.filter(category__slug=slug)
    hotel = Hotel.objects.filter(category__slug=slug)
    martyr = Martyrs.objects.filter(category__slug=slug)
    cats = list(chain(place, soghat, hotel, martyr))
    context = {
        'cats': cats,
        'categorys': categorys,
    }

    if cats:
        cat_name = cats[0].category.name
        cat = cats[0].category
        # print('cat: ', cat)
        context['cat_name'] = cat_name
        context['cat'] = cat

    return render(request, 'city/category.html', context=context)

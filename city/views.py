from itertools import chain

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import AddForm
from .models import City, Place, Soghat, Category, Martyrs, Hotel


categorys = Category.objects.filter(parent=None)

def homepage(request):
    # print(categorys)
    places = Place.objects.all()
    city = City.objects.get(name='ازنا')
    gardesh = Place.objects.filter(category__slug='گردشگری', is_access=True)[:4]
    tarikhi = Place.objects.filter(category__slug='تاریخی-مذهبی', is_access=True)[:4]
    karkhane = Place.objects.filter(category__slug='کارخانجات', is_access=True)[:4]
    roosta = Place.objects.filter(category__slug='روستا', is_access=True)[:4]
    soghats = Soghat.objects.filter(is_access=True)
    martyrs = Martyrs.objects.filter(is_access=True)
    hotel_res = Hotel.objects.filter(is_access=True)
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
    list1 = [Place, Soghat, Hotel]
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
    cat = Category.objects.get(slug=slug)

    place = Place.objects.filter(category__slug=slug, is_access=True)
    soghat = Soghat.objects.filter(category__slug=slug, is_access=True)
    hotel = Hotel.objects.filter(category__slug=slug, is_access=True)
    martyr = Martyrs.objects.filter(category__slug=slug, is_access=True)
    cats = list(chain(place, soghat, hotel, martyr))

    context = {
        'cat': cat,
        'cats': cats,
        'categorys': categorys,
    }

    # if cats:
    #     cat_name = cats[0].category.name
    #     cat = cats[0].category
    #     # print('cat: ', cat)
    #     context['cat_name'] = cat_name
    #     context['cat'] = cat

    return render(request, 'city/category.html', context=context)


def add_sub_cat(request, slug):
    if request.method == 'POST':
        add_form = AddForm(request.POST, request.FILES)
        if add_form.is_valid():
            try:
                new = add_form.save(commit=False)
                name = request.POST.get('name')
                new.slug = "-".join(name.split())
                new.category = Category.objects.get(slug=slug)
                new.save()
                return HttpResponseRedirect(reverse('city:unique_slug', kwargs={'slug': slug}))
            except Exception as e:
                print('error to save: ', str(e))
        else:
            print('form oninvalid')
    else:
        add_form = AddForm()

    context = {
        'add_form': add_form,
        'categorys': categorys,
        'slug': slug,
    }
    return render(request, 'city/add_sub_cat.html', context=context)
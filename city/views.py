from itertools import chain

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import AddPlaceForm, AddSoghatForm, AddHotelForm, CommentForm
from .models import City, Place, Soghat, Category, Martyrs, Hotel, Comment, IpClass

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

    list1 = [Place, Soghat, Hotel, Martyrs]
    for li in list1:
        case1 = li.objects.filter(slug=slug)
        if case1.exists():
            case = li.objects.get(slug=slug)

    ip = get_client_ip(request)
    if not IpClass.objects.filter(ip=ip).exists():
        IpClass.objects.create(ip=ip)

    case.views.add(IpClass.objects.get(ip=ip))

    context = {
        'case': case,
        'categorys': categorys,
    }

    # ******************* Start Comment *************************
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            message = request.POST.get('comment')
            comment = Comment(content_object=case, fullname=fullname, email=email, comment=message)
            comment.save()
            # try:
            #     comment = comment_form.save(commit=False)
            #     comment.content_object = case
            #     comment.save()
            #     error_form = 'نظر شما با موفقیت ثبت شد.'
            # except Exception as e:
            #     error_form = str(e)
            #     print('error to save: ', str(e))
            # context['error_form'] = error_form
    else:
        comment_form = CommentForm()

    comments = Comment.objects.filter(object_id=case.id, confirm=True)
    context['comments'] = comments
    context['comment_form'] = comment_form
    # ******************* End Comment ***************************

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


@login_required
def add_sub_cat(request, slug):
    context = {
        'categorys': categorys,
        'slug': slug,
    }
    print('slug is: ', slug)
    if request.method == 'POST':
        if slug == 'سوغات':
            add_form = AddSoghatForm(request.POST, request.FILES)
        elif slug == 'هتل':
            add_form = AddHotelForm(request.POST, request.FILES)
        else:
            add_form = AddPlaceForm(request.POST, request.FILES)
        if add_form.is_valid():
            try:
                new = add_form.save(commit=False)
                name = request.POST.get('name')
                new.slug = "-".join(name.split())
                new.category = Category.objects.get(slug=slug)
                new.save()
                return HttpResponseRedirect(reverse('city:unique_slug', kwargs={'slug': slug}))
            except Exception as e:
                context['error_form'] = str(e)
                print('error to save: ', str(e))
        else:
            print('form oninvalid')
    else:
        if slug == 'سوغات':
            add_form = AddSoghatForm()
        # elif Q(slug == 'هتل') | Q(slug == 'رستوران'):
        elif slug == 'هتل' or slug == 'رستوران':
            add_form = AddHotelForm()
        else:
            add_form = AddPlaceForm()

    context['add_form'] = add_form

    return render(request, 'city/add_sub_cat.html', context=context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def like_post(request, pk_p, pk_c):
    list1 = [Place, Soghat, Hotel, Martyrs]
    for li in list1:
        case1 = li.objects.filter(id=pk_p)
        if case1.exists():
            case = get_object_or_404(case1, id=pk_p)
            print('case: ', case1)

    comment = Comment.objects.get(id=request.POST.get('comment_id'))

    ip = get_client_ip(request)

    if not IpClass.objects.filter(ip=ip).exists():
        IpClass.objects.create(ip=ip)
    if comment.likes.filter(id=IpClass.objects.get(ip=ip).id).exists():
        comment.likes.remove(IpClass.objects.get(ip=ip))
    else:
        comment.likes.add(IpClass.objects.get(ip=ip))

    return HttpResponseRedirect(case.get_absolute_url())


def dislike_post(request, pk_p, pk_c):
    list1 = [Place, Soghat, Hotel, Martyrs]
    for li in list1:
        case1 = li.objects.filter(id=pk_p)
        if case1.exists():
            case = get_object_or_404(case1, id=pk_p)

    comment = Comment.objects.get(id=request.POST.get('comment_id'))

    ip = get_client_ip(request)

    if not IpClass.objects.filter(ip=ip).exists():
        IpClass.objects.create(ip=ip)
    if comment.dislikes.filter(id=IpClass.objects.get(ip=ip).id).exists():
        comment.dislikes.remove(IpClass.objects.get(ip=ip))
    else:
        comment.dislikes.add(IpClass.objects.get(ip=ip))

    return HttpResponseRedirect(case.get_absolute_url())

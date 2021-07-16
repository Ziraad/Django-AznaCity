from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages

from news.models import News
from .forms import MyUserForm, ProfileForm, PostForm
from .models import Profile
from city.models import Category

# -*- coding: utf-8 -*-

categorys = Category.objects.all


def login_view(request):
    next_url = request.GET.get('next')

    # search_form = SearchForm(data=request.GET)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Successful login
            login(request, user)
            redirect_url = next_url if next_url else reverse('city:home_page')
            return HttpResponseRedirect(redirect_url)
        else:
            # undefined user or wrong password
            context = {
                'categorys': categorys,

                'username': username,
                # 'search_form': search_form,
                'login_error': 'کاربری با این مشخصات یافت نشد!'
            }
    else:
        print('request is get')
        context = {
            'categorys': categorys,

            # 'search_form': search_form,
        }
    # search_form_method(request, context)
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('city:home_page'))


@login_required
def profile_details(request):
    profile = request.user.profile
    # search_form = SearchForm(data=request.GET)
    context = {
        'categorys': categorys,

        # 'search_form': search_form,
        'profile': profile,
    }
    # search_form_method(request, context)
    return render(request, 'accounts/profile_details.html', context)


@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        user_form = MyUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, files=request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            try:
                user_form.save()
                profile_form.save()
                return HttpResponseRedirect(reverse('accounts:profile_details'))
            except Exception as e:
                print('form is invalid ...', str(e))
        else:
            print('error ...')
    else:
        user_form = MyUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    # search_form = SearchForm(data=request.GET)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
        # 'search_form': search_form,
        'categorys': categorys,

    }
    # search_form_method(request, context)
    return render(request, 'accounts/profile_edit.html', context)


def register_user(request):
    # search_form = SearchForm(data=request.GET)
    context = {
        'categorys': categorys,

        # 'search_form': search_form,
    }
    # search_form_method(request, context)
    if request.method == 'POST':
        try:
            # f_name = request.POST.get('f_name')
            # l_name = request.POST.get('l_name')
            # email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            # gender = request.POST.get('gender')
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.create_user(username=username, password=password)
            Profile.objects.create(user=user, mobile=mobile)
            context['message_in_register'] = 'حساب کابری شما با موفقیت ثبت شد'
        except Exception as e:
            print('error in register: ', str(e))
            context['message_in_register'] = 'لطفاً اطلاعات خواسته شده را به درستی وارد نمایید.'
    return render(request, 'accounts/register_form.html', context=context)


@login_required()
def post_list(request):
    post = News.objects.filter(author=request.user.profile).order_by('-pub_date')
    print('post :', post)
    # search_form = SearchForm(data=request.GET)

    context = {
        'post': post,
        'categorys': categorys,

        # 'search_form': search_form,
    }
    # search_form_method(request, context)

    return render(request, 'accounts/post_list_page.html', context=context)


@login_required()
def add_post_view(request):
    # search_form = SearchForm(data=request.GET)

    context = {
        'categorys': categorys,

        # 'search_form': search_form,
    }

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        slug = request.POST.get('slug')

        news = News.objects.filter(slug=slug)

        if form.is_valid():
            if len(news) == 0:
                instance = form.save(commit=False)
                instance.author = request.user.profile
                if instance.category.parent is not None:
                    instance.save()
                    print('form submit')
                    return redirect('accounts:post_list')
                else:
                    context[
                        'error_message'] = 'در ثبت اطلاعات مشکلی پیش آمده است! لطفاً برای انتخاب دسته بندی از زیر گروه استفاده کنید.'
            else:
                context[
                    'error_message'] = 'در ثبت اطلاعات مشکلی پیش آمده است! ممکن است پستی با این اسلاگ قبلاَ ثبت شده باشد. لطفاً اسلاگ را تصحیح کنید!'
        else:
            print('form invalid')
            context['error_message'] = 'در ثبت اطلاعات مشکلی پیش آمده است! لطفاً خطاها را اصلاح کنید.'

    else:
        form = PostForm()

    context['form'] = form

    # search_form_method(request, context)

    return render(request, 'accounts/add_post_page.html', context=context)


@login_required()
def post_edit(request, slug):
    # search_form = SearchForm(data=request.GET)
    instance = get_object_or_404(News, slug=slug)
    form = PostForm(request.POST, request.FILES, instance=instance)
    context = {
        'instance': instance,
        # 'search_form': search_form,
        'categorys': categorys,

    }
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Post Saved")
            return HttpResponseRedirect(reverse('accounts:post_list'))
        else:
            print('form invalid')

    else:
        form = PostForm(instance=instance)

    context['form'] = form

    # search_form_method(request, context)

    return render(request, 'accounts/post_edit.html', context)

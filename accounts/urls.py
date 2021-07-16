from django.urls import path, re_path

from accounts import views

# -*- coding: utf-8 -*-

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/details', views.profile_details, name='profile_details'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('register', views.register_user, name='register_user'),

    path('post/add/', views.add_post_view, name='add_post_view'),
    path('post-list', views.post_list, name='post_list'),
    re_path(r'^post-edit/(?P<slug>[-\w]+)/$', views.post_edit, name='post_edit'),
]
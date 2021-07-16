from django.urls import path, re_path
# from django.conf.urls import handler400, handler403, handler404, handler500


from news import views

# -*- coding: utf-8 -*-

app_name = 'news'
urlpatterns = [
    re_path(r'^category/(?P<slug>[-\w]+)/(?P<sub_slug>[-\w]+)/(?P<title>[-\w]+)/$', views.news_detail_page,
            name='news_detail_page'),
]

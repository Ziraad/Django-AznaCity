from django.urls import path, re_path

from city import views

app_name = 'city'
urlpatterns = [
    path('', views.homepage, name='home_page'),
    # path('gardeshgari/', views.all_gardesh, name='all_gardesh'),
    # path('gardeshgari/details/<int:place_id>/', views.place_details, name='places_details'),
    re_path(r'^category/(?P<slug>[-\w]+)/$', views.category, name='unique_slug'),
    # path('main/Kaveh/<slug:slug>/', views.details, name='details'),
    re_path(r'^p/(?P<slug>[-\w]+)/$', views.place_details, name='place_details'),
    re_path(r'^p/(?P<slug>[-\w]+)/add$', views.add_sub_cat, name='add_sub_cat'),
    path('like/<int:pk_p>/<int:pk_c>/', views.like_post, name='like_post'),
    path('dislike/<int:pk_p>/<int:pk_c>/', views.dislike_post, name='dislike_post'),
]

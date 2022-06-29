from django.contrib import admin
from django.urls import re_path
from . import views
#from photos import views

urlpatterns=[
    re_path('^today/$',views.news_of_day,name='newsToday'),
    re_path('^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    re_path('^search/$',views.search_results,name='search_results'),
    re_path('',views.index,name = 'index'),
    re_path('^article/(\d+)',views.article,name = 'article'),
]
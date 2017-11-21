from django.contrib.auth.views import login, logout
from django.conf.urls import url, include
from django.contrib import admin
from .views import room, list_rooms


urlpatterns = [
    url(r'^$', list_rooms, name='list_rooms'),
    url(r'^room/$', room, name='room'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
]

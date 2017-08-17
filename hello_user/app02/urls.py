#-*- coding:utf8 -*-

from django.conf.urls import url
from django.contrib import admin
from app02.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', index),
]

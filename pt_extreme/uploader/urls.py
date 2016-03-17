# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('uploader.views',
    url(r'^uploads/$', 'list', name='list'),
)

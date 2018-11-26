# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views
# Create your urls here.

urlpatterns = [
	url(r'^$',views.index , name='index'),
	url(r'^home',views.home , name='home'),
	url(r'^RunTest',views.RunTest , name='RunTest'),
	url(r'^Novel',views.GetNovel , name='GetNovel'),
	url(r'^Chapter',views.GetChapter , name='GetChapter'),
	url(r'^Page',views.GetPage , name='GetPage'),
]

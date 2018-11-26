# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views
# Create your urls here.

urlpatterns = [
	url(r'^$',views.index , name='index'),
	url(r'^home',views.home , name='home'),
	url(r'^EnableS',views.enableS , name='enableS'),
	url(r'^DisableS',views.disableS , name='disableS'),
	url(r'^EnableAll',views.enableAll , name='enableAll'),
        url(r'^DisableAll',views.disableAll , name='disableAll')
]

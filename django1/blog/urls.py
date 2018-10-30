# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:42:10 2018

@author: Admin
"""

from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='blog-home'),
        path('about/', views.about, name='blog-about'),
#        path('contact/', views.contact, name='blog-contact'),
        ]
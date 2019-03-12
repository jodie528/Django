# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Weishi Li
# time: 2019-03-12

from django.urls import path

from . import  views

urlpatterns = [
    path('index/', views.index),
    path('article/<article_id>', views.article_page, name='article_page'),
    path('edit/', views.edit_page),
]
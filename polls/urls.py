# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:41:01 2017

@author: irene_qwewxh7
"""

from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test1/$',views.etat_nutri,name='test_nutri'),
    url(r'^test2/(?P<id_image>\d{2})$',views.test_image,name='test_image'),
    url(r'^accueil/$',views.accueil,name='accueil'),
    url(r'^inscription/$',views.inscription,name='inscription'),
    url(r'^connexion/$', views.connexion,name='connexion'),
    url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),
    url(r'^question_supp/$',views.question_supp,name='question_supp'),
    url(r'^reglement/$',views.reglement,name='reglement'),
       
]
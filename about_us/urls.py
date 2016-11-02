from django.conf.urls import url

import views


urlpatterns =[

    url(r'^about_us$/', views.about_us, name='about_us'),
    url(r'^history$/', views.history, name='history'),
    url(r'^facts$/', views.facts, name='facts'),
    url(r'^QandA/', views.QandA, name='QandA'),



]
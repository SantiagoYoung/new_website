from django.conf.urls import url
import views

urlpatters =[


    url(r'^contacts$/', views.contacts, name='contacts'),
    url(r'^message$/', views.message, name='message'),

]
from django.conf.urls import url
import views
urlpatterns =[

    url(r'^archive/$', views.archive, name='archive'),


]
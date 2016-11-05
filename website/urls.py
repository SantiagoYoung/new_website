from django.conf.urls import url
import views


urlpatterns = [

    url(r'^all_service/$', views.all_service, name='all_service'),
    url(r'^feature_service/$', views.feature_service, name='feature_sercice'),
    url(r'^carousel_figure/$', views.carousel_figure, name='carousel_figure'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^client_words/$', views.client_words, name='client_words'),
    url(r'^section/$', views.section, name='section'),
    url(r'^excel_export', views.excel_export, name='excel_export'),


]














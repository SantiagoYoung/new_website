from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from contact import views as contact_views
from website import views as website_views
from about_us import views as about_views






urlpatterns = [

    # Examples:
    # url(r'^$', 'new_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # url(r'^website/', include('website.urls')),
    # url(r'^contact/', include('contact.urls')),
    # url(r'^news/', include('news.urls')),
    # url(r'^about/', include('about_us.urls')),

    url(r'^home/', website_views.home_page, name='home_page'),
    url(r'^contact', contact_views.contact_page, name='contact_page'),
    url(r'^about', about_views.about_page, name='about_page'),
    url(r'^portfolio/', website_views.portfolio_page,  name='portfolio',),
    url(r'^service/', website_views.service_page,  name='service'),



]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
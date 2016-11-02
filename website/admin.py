from django.contrib import admin
from .models import Portfolio, Service, Carousel_figure, Client_words, Structure
# Register your models here.


admin.site.register(Portfolio)
admin.site.register(Service)
admin.site.register(Client_words)
admin.site.register(Structure)
admin.site.register(Carousel_figure)
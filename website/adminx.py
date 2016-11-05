from .models import Portfolio, Service, Carousel_figure, Client_words, Structure
import xadmin


xadmin.autodiscover()



xadmin.site.register(Portfolio)
xadmin.site.register(Service)
xadmin.site.register(Carousel_figure)
xadmin.site.register(Client_words)
xadmin.site.register(Structure)




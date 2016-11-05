from models import About_us, History, Facts, QnA

import xadmin


xadmin.autodiscover()


xadmin.site.register(About_us)
xadmin.site.register(History)
xadmin.site.register(Facts)
xadmin.site.register(QnA)





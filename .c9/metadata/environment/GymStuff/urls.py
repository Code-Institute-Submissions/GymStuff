{"filter":false,"title":"urls.py","tooltip":"/GymStuff/urls.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":21,"column":0},"action":"remove","lines":["\"\"\"GymStuff URL Configuration","","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url","from django.contrib import admin","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","]",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":36,"column":1},"action":"insert","lines":["\"\"\"ecommerce URL Configuration","","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","","from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts","from products import urls as urls_products","from cart import urls as urls_cart","from search import urls as urls_search","from checkout import urls as urls_checkout","from products.views import all_products","from django.views import static","from .settings import MEDIA_ROOT","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', all_products, name='index'),","    url(r'^accounts/', include(urls_accounts)),","    url(r'^products/', include(urls_products)),","    url(r'^cart/', include(urls_cart)),","    url(r'^checkout/', include(urls_checkout)),","    url(r'^search/', include(urls_search)),","    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})","]"]}]]},"ace":{"folds":[],"scrolltop":179,"scrollleft":0,"selection":{"start":{"row":36,"column":1},"end":{"row":36,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1594724406151,"hash":"99c5c166a717749dfd134a1574abc348f8d132f1"}
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
#all the urls in an app, like stamp(app)
# must be pointed in the project urls file(yupay/urls)
from .views  import index,forms,searchForm,search
from .views import stamping
urlpatterns = [
    path('', index,name='index'),
    path('forms/', forms,name='forms'),
    path('searchform/', searchForm,name='searchForm'),
    #path('searchform/?userid=<int:id>', search,name='search'),
    path('searchform/search/',search,name='search'),
    # path('certificado/', certificados,name='certifado'),
    path('forms/stamp/', stamping.as_view(),name='stamp'),
    #    route, view, name, 
] 
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
#all the urls in an app, like stamp(app)
# must be pointed in the project urls file(yupay/urls)
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('forms/', views.forms,name='forms'),
    path('stamp/', views.post,name='stamp'),
    #    route, view, name, 
] 
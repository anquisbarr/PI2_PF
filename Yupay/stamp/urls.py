from django.urls import path
#all the urls in an app, like stamp(app)
# must be pointed in the project urls file(yupay/urls)
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('io', views.stamp,name='stamp'),
    #    route, view, name, 
]
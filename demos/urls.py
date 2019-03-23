from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.demo_list),
	url(r'^detail=.+$', views.demo_detail),
]


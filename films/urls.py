from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.film_list),
	url(r'bigbangtheory/(?P<video_url>.*)/(?P<video_title>.*)$', views.bigbangtheory, name="video_info"),
	url(r'bigbangtheory$', views.bigbangtheory),
	url(r'gameofthrone/(?P<video_url>.*)/(?P<video_title>.*)$', views.gameofthrone, name="gameofthrone"),
	url(r'gameofthrone$', views.gameofthrone),
]


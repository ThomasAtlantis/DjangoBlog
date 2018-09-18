"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from . import view
from . import upload
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', view.index),
    url(r'^$', view.index),
    url(r'^e_books/', include('e_books.urls')),
    url(r'^photos/', include('gallery.urls')),
    url(r'^single/', view.single),
	url(r'^films/', include('films.urls')),
    url(r'^short-codes/', view.short_codes),
    url(r'^mail/', view.mail),
    url(r'^articles/', include('articles.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^admin/uploads/(?P<dir_name>[^/]+)$', upload.upload_image, name='upload_image'),
	url(r"^uploads/(?P<path>.*)$", 'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
]

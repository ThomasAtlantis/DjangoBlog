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
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^archive/$', views.article_all),
	url(r'^tags/$', views.article_tags),
    url(r'^(\d+)/$', views.article_details, name='article-details'),
	url(r'^(\d+)/comment/$', views.article_comments, name='article-comment'),
    url(r'^(.*)/$', views.article_list, name='article-list'),
]

from django.db.models.aggregates import Count
from django.shortcuts import render
from .models import Films
from Category.models import Category

def get_cate():
	return Category.objects.annotate(num_posts=Count('article'))

def film_list(request):
	films = Films.objects.all().order_by("kind")
	categorys = get_cate()
	return render(request, "films/films.html", {"films": films, "categorys": categorys})

def bigbangtheory(request, video_url="", video_title=""):
	categorys = get_cate()
	return render(request, "films/bigbangtheory.html", {'video_url': video_url, 'video_title': video_title, 'categorys': categorys})

def gameofthrone(request, video_url="", video_title=""):
	categorys = get_cate()
	return render(request, "films/gameofthrone.html", {'video_url': video_url, 'video_title': video_title, 'categorys': categorys})

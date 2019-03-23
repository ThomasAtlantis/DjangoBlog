from django.db.models.aggregates import Count
from django.shortcuts import render
from Category.models import Category

def index(request):
	categorys = Category.objects.annotate(num_posts=Count('article'))
	return render(request, "index.html", {'categorys': categorys})

def photos(request):
	return render(request, 'photos.html')

def single(request):
	return render(request, 'single.html')

def short_codes(request):
	return render(request, 'short-codes.html')

def mail(request):
	categorys = Category.objects.annotate(num_posts=Count('article'))
	return render(request, 'mail.html', {'categorys': categorys})

def page_not_found(request):
	return render(request, '404.html')

def page_error(request):
	return render(request, '500.html')

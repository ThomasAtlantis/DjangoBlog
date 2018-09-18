from django.db.models.aggregates import Count
from django.shortcuts import render
from .models import Gallery
from Category.models import Category
# Create your views here.

def gallery(request):
	image_list = Gallery.objects.all()
	categorys = Category.objects.annotate(num_posts=Count('article'))
	return render(request, 'gallery/gallery.html', {
		'image_list': image_list,
		'categorys': categorys
        })


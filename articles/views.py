from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404 
from django.shortcuts import render
from .models import Article
from Category.models import Category
from Tag.models import Tag
# Create your views here.

def get_cate():
	return Category.objects.annotate(num_posts=Count('article'))

def article_list(request, cate_name):
	cate = get_object_or_404(Category, name=cate_name)
	article_tmp = Article.objects.filter(category=cate).order_by('-date')
	categorys = get_cate()
	paginator = Paginator(article_tmp, 20)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	return render(request, "articles/articles.html", {"articles": articles, "categorys": categorys, "cate_name": cate_name})

def article_details(request, id):
	article = Article.objects.get(id=id)
	categorys = get_cate()
	return render(request, "articles/article_details.html", {"article": article, "categorys": categorys})

def article_all(request):
	article_tmp = Article.objects.all().order_by('-date')
	categorys = get_cate()
	paginator = Paginator(article_tmp, 20)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	return render(request, "articles/article_list.html", {"articles": articles, "categorys": categorys})

def article_tags(request):
	categorys = get_cate()
	tags = Tag.objects.annotate(num_posts=Count('tag_articles'))
	return render(request, "articles/article_tags.html", locals())

def article_comments(request, id):
	article = Article.objects.get(id=id)
	categorys = get_cate()
	return render(request, "articles/article_comments.html", {"article": article, "categorys": categorys})

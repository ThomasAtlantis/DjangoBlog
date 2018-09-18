from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Article
from Category.models import Category
from Tag.models import Tag
from comments.models import Comments
from .forms import CommentForm
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
	form = CommentForm()
	comment_list = article.comments_set.all()
	return render(request, "articles/article_details.html", locals())

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
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comments()
			comment.article = article
			comment.user_name = form.cleaned_data['user_name']
			comment.body = form.cleaned_data['body']
			comment.save()
		comment_list = article.comments_set.all().order_by('created_time')
		context = {
            'article': article,
            'form': form,
            'comment_list': comment_list,
			'categorys': categorys
        }
		return render(request,'articles/article_details.html',context=context)
	return render(request, "articles/article_details.html", {"article": article, "categorys": categorys})

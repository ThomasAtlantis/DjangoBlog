from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Article
from Category.models import Category
from Tag.models import Tag
from comments.models import Comments
from .forms import CommentForm
import markdown
from captcha.models import CaptchaStore  
from captcha.helpers import captcha_image_url
import re
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


def anchor_offset(html):
	tocs = re.findall(re.compile(r'(<h[1-9] id="[^\"]+">)'), html)
	anchor_format = '<a class="target-fix" id="{}"></a>\n'
	for toc in tocs:
		id = re.search(r'id="([^\"]+)"', toc).group(1)
		new = anchor_format.format(id) + toc.replace('id="%s"' % id, '')
		html = html.replace(toc, new)
	return html

def list_guard(html):
	html = html.replace('<li>', '<li class="md-list">')
	return html

def toc_polish(html):
	if '<li>' not in html:
		hidden = '''
			<style type="text/css">
			.mulu {
				visibility: hidden;
			}
			.article_detail {
				margin-right: 0px;
			}
			</style>
			<script language="javascript">
				document.getElementById('article_detail').style.marginRight = '0px';
			</script>
		'''
		return hidden
	html = html.replace('<li>', '<li class="mulu-item">')
	html = html.replace('<ul>', '<ul class="mulu-ul">')
	html = html.replace('<a href', '<a class="toc-a" href')
	html = html + '\n' + '''
		<style type="text/css">
		.mulu-item {
			padding-top: 1px;
			padding-bottom: 1px;
			list-style-type: none;
		}
		.mulu-ul {
			list-style-type: none;
			padding-right: 5px;
		}
		.toc {
			padding-bottom: 20px;
		}
		.toc-a {
			color: black;
		}
		.toc-a:hover {
			font-weight: bold;
			text-decoration: none;
			border-left: 4px solid #1F2837;
			padding-left: 4px;
			background-color: #dddddd;
			width: 100%;
			display: block;
		}
		</style>
	'''
	return html

def article_details(request, id):
	article = Article.objects.get(id=id)
	if not article.editor_type:
		md = markdown.Markdown(extensions=[
        	'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
		article.body = md.convert(article.body)
		toc = md.toc
		article.body = article.body.replace(toc, '')
		article.body = anchor_offset(article.body)
		article.body = list_guard(article.body)
		toc = toc_polish(toc)
	else:
		toc = toc_polish("")
	categorys = get_cate()
	hashkey = CaptchaStore.generate_key()
	image_url = captcha_image_url(hashkey)
	form = CommentForm()
	comment_list = article.comments_set.all()
	return render(request, "articles/article_details.html", locals())

def article_all(request):
	article_tmp = Article.objects.all().order_by('-date')
	categorys = get_cate()
	articles = {}
	for article in article_tmp:                                                                      	
		articles.setdefault(article.date.year, {}).setdefault(article.date.month, []).append(article)
	articles = sorted([[y, sorted(a.items(), key=lambda d1: d1[0], reverse=True)] for  y, a in  articles.items()], key=lambda d2: d2[0], reverse=True)
	return render(request, "articles/article_list.html", {"articles": articles, "categorys": categorys})

def article_tags(request):
	categorys = get_cate()
	tags = Tag.objects.annotate(num_posts=Count('tag_articles')).filter(num_posts__gt=0).order_by('-num_posts')
	return render(request, "articles/article_tags.html", locals())

def article_comments(request, id):
	article = Article.objects.get(id=id)
	categorys = get_cate()
	if request.is_ajax():
		hashkey = CaptchaStore.generate_key()
		context = {
			'hashkey': hashkey,
			'image_url': captcha_image_url(hashkey),
		}
		return render(request,'articles/article_details.html',context=context) 
	elif request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comments()
			comment.article = article
			comment.user_name = form.cleaned_data['user_name']
			comment.body = form.cleaned_data['body']
			comment.save()
		comment_list = article.comments_set.all().order_by('created_time')
		hashkey = CaptchaStore.generate_key()
		context = {
			'hashkey': hashkey,
			'image_url': captcha_image_url(hashkey),
            'article': article,
            'form': form,
            'comment_list': comment_list,
			'categorys': categorys
        }
		return render(request,'articles/article_details.html',context=context)

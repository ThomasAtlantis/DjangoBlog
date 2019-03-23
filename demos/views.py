from django.db.models.aggregates import Count
from django.shortcuts import render, redirect
from .models import Demo
from Category.models import Category
from django.http import HttpResponse
import sys, re
# Create your views here.

def get_cate():
	return Category.objects.annotate(num_posts=Count('article'))

def demo_list(request):
	demos = Demo.objects.all()
	for demo in demos:
		demo.href = "detail=" + demo.href
	categorys = get_cate()
	return render(request, 'demos/demo_list.html', {'demos': demos, 'categorys': categorys})

def demo_detail(request):
	categorys = get_cate()
	template = request.path.replace('detail=', '').encode('utf-8')[1:]
	if template.endswith(".py"):
		try:
			file_name = re.search(r'(\w+\.py)', template).group(1)
			sys.path.append('/home/admin/django/my_blog/demos/templates/' + template.replace(file_name, ''))
			m = __import__(file_name[:-3])
			response_body = m.application(dict(request.POST))
		except Exception as error:
			response_body = str(error)
		return HttpResponse(response_body)
	else:
		return render(request, template, {'categorys': categorys})

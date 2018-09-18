from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.aggregates import Count
from django.shortcuts import render
from .models import E_Book
from Category.models import Category

# Create your views here.
def e_book_list(request):
	e_books = E_Book.objects.all().order_by("kind")
	categorys = Category.objects.annotate(num_posts=Count('article'))
	return render(request, "e_books/e_books.html", {"e_books": e_books, "categorys": categorys})

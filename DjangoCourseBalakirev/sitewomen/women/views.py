from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect

from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
menu = ['О сайте', 'Обо мне', 'Категории', 'Архив']

class MyClass:
	def __init__(self, a, b):
		self.a = a
		self.b = b


def index(request):
	data = {
		'title': 'главная страница',
		'menu': menu,
		'float': 27.64,
		'lst': [1, 2, 'fdc', True],
		'set': {1, 2, 3, 4, 5},
		'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
		'obj': MyClass(10, 20)
	}
	return render(request, 'women/index.html', context=data)

def about(request):
	return render(request, 'women/about.html',{'title': 'О сайте'} )

def categories(request, cat_id):
	return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')

def categories_by_slug(request, cat_slug):
	if request.method == 'POST':
		print(request.POST)
	return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')

def archive(request, year):
	if year > 2023:
		uri = reverse('cats', args=('sport', ))
		return HttpResponsePermanentRedirect(uri)
	return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def page_not_found(request, exception):
	return HttpResponseNotFound('<h1>Страница не найдена</h1>')



from django.shortcuts import render
from .models import Article
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

def news(request):
	latest_articles_list = Article.objects.order_by('-article_date')[:10]
	return render(request, 'articles/list.html', {'latest_articles_list' : latest_articles_list})

def index(request):
	latest_articles_list = Article.objects.order_by('-article_date')[:3]
	return render(request, 'home/index.html', {'latest_articles_list' : latest_articles_list})

def detail(request, article_alias):
	try:
		a = Article.objects.get(article_alias = article_alias)
	except:
		raise Http404("Not found")

	return render(request, 'articles/detail.html', {'article': a})
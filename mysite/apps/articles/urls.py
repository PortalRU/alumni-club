from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
	path('news/', views.news, name='news'), 
	path('news/<article_alias>', views.detail, name='detail'), 
	path('', views.index, name='index')
]
from django.contrib import admin
from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView


app_name = 'articles'

urlpatterns = [

	path('main/',ArticleListView.as_view(),name='main'),
	path('create/',ArticleCreateView.as_view(),name='article-create'),
	path('<int:pk>/',ArticleDetailView.as_view(),name='article-detail'),
]
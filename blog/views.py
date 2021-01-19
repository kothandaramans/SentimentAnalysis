from django.shortcuts import render
from .models import Article
from .forms import ArticleModelForm
from django.views.generic import ListView, DetailView, CreateView

class ArticleCreateView(CreateView):
	template_name = 'article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()
	#success_url = '/'
	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

class ArticleListView(ListView):
	template_name = 'article_list.html'
	queryset = Article.objects.all()

class ArticleDetailView(DetailView):
	template_name = 'article_detail.html'
	queryset = Article.objects.all()
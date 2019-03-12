from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Django中所有的请求都用函数处理

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})

def edit_page(request):
    return render(request, 'blog/edit_page.html')
# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {"articles": articles})


def get_detail(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})


def create_or_edit(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/create.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'blog/create.html', {'article': article})


def action_create(request):
    title = request.POST.get('title', '标题')
    content = request.POST.get('content', '空白内容')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        return HttpResponseRedirect('/blog')
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request, 'blog/article_detail.html', {'article': article})

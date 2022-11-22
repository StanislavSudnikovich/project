from django.shortcuts import render
from .models import *


def news(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'news.html', context)


def new(request, pk):
    new = News.objects.get(pk=pk)
    context = {
        'new': new
    }
    return render(request, 'new.html', context)

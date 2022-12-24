from django.shortcuts import render
from .models import *
from .forms import *


def news_index(request):
    news = News.objects.all()

    context = {
        'news': news
    }
    return render(request, 'news_index.html', context)


def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    post = News.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comments.save()
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'news': news
    }
    return render(request, 'news_detail.html', context)

from django.shortcuts import render
from .models import *
from .forms import *


def phone_index(request):
    phones = Phone.objects.all()
    context = {
        'phones': phones
    }
    return render(request, 'phone_index.html', context)


def phone_detail(request, pk):
    phone = Phone.objects.get(pk=pk)
    post = Phone.objects.get(pk=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviews = Review(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            reviews.save()
    reviews = Review.objects.filter(post=post)
    context = {
        'post': post,
        'reviews': reviews,
        'form': form,
        'phone': phone
    }
    return render(request, 'phone_detail.html', context)

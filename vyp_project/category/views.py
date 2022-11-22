from django.shortcuts import render
from .models import *


def phones(request):
    phones = Phone.objects.all()
    context = {
        'phones': phones
    }
    return render(request, 'phones.html', context)


def phone(request, pk):
    phone = Phone.objects.get(pk=pk)
    context = {
        'phone': phone
    }
    return render(request, 'phone.html', context)

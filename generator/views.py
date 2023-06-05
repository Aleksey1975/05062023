from django.http import HttpResponse
from django.shortcuts import render
import string
import random


def index(request):
    context = {
        'title': 'Создайте свой пароль',

    }

    return render(request, 'generator/index.html', context=context)

def password(request):
    nabor = string.ascii_lowercase
    if request.GET.get('uppercase'):
        nabor += string.ascii_uppercase
    if request.GET.get('digit'):
        nabor += '0123456789'
    if request.GET.get('special'):
        nabor += string.punctuation

    L = int(request.GET.get('length'))
    parol = ''
    nabor = list(nabor)
    print(nabor)
    for _ in range(L):
        parol += random.choice(nabor)
    context = {
        'title': 'Ваш пароль',
        'parol': parol

    }

    return render(request, 'generator/password.html', context=context)
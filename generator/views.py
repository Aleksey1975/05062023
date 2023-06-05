from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Создайте свой пароль',

    }

    return render(request, 'generator/index.html', context=context)

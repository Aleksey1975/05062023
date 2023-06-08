from django.shortcuts import render
from .models import Project

def index_portfolio(request):
    projects = Project.objects.all()

    context = {
        'title': 'Портфолио',
        'projects': projects,

    }

    return render(request, 'portfolio/index_portfolio.html', context=context)

from django.shortcuts import render, get_object_or_404
from .models import Articles

def index_blog2(request):
    articles = Articles.objects.order_by('-dat_e')
    context = {
        'title': 'blog2',
        'articles': articles
    }

    return render(request, 'blog2/index_blog2.html', context)

def detail2(request, blog_id):
    blog = get_object_or_404(Articles, pk=blog_id)
    context = {
        'title': 'blog2',
        'blog': blog
    }

    return render(request, 'blog2/detail2.html', context)
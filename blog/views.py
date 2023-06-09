from django.shortcuts import render, get_object_or_404
from .models import Articles

def index_blog(request):
    articles = Articles.objects.order_by('-date_creation')

    context = {
        'title': 'blog',
        'articles': articles,

    }

    return render(request, 'blog/index_blog.html', context=context)

def detail(request, blog_id):
    blog = get_object_or_404(Articles, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})

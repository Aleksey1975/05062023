from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [

    path('', index_blog, name='index_blog'),
    path('<int:blog_id>', detail, name='detail'),

    ]

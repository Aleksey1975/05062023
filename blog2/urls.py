from django.urls import path
from .views import *



urlpatterns = [

    path('', index_blog2, name='index_blog2'),
    path("<int:blog_id>", detail2, name='detail2'),

    ]
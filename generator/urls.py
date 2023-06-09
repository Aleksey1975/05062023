from django.urls import path

from .views import *
app_name = 'generator'

urlpatterns = [

    path('', index, name='index'),
    path('password/', password, name='password'),

]
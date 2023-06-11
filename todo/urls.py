from django.urls import path
from .views import *



urlpatterns = [

    path('signup/', signupuser, name='todo'),
    path('current/', currenttodos, name='currenttodos'),


    ]
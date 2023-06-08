from django.urls import path

from .views import *

urlpatterns = [

    path('', index_portfolio, name='index_portfolio'),


]
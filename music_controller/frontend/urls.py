from cgitb import html
from .views import index
from django.urls import path

urlpatterns = [
    path('', index)

]
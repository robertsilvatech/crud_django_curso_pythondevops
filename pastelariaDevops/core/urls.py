from django.urls import path
from .views import create_loja
from .views import read_loja

urlpatterns = [
    path('', create_loja, name='create_loja'),
    path('lista', read_loja, name='read_loja')
]
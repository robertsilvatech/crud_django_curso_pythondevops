from django.urls import path
from .views import create_loja
from .views import read_loja
from .views import update_loja
from .views import delete_loja

urlpatterns = [
    path('', create_loja, name='create_loja'),
    path('lista', read_loja, name='read_loja'),
    path('update/<int:id>', update_loja, name='update_loja'),
    path('delete/<int:id>', delete_loja, name='delete_loja')
]
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', product, name='produto'),
    path('servicos/', servicos, name='servicos'),
    path('quem_somos/', quem_somos, name='quem_somos'),
]

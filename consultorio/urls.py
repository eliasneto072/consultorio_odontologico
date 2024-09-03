from django.urls import path, include
from .views import *


urlpatterns = [
    path('', homeView, name='home'),
    path('cadastro/', pacienteCadastroView, name='cadastro'),
]
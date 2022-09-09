from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id_noticia>', views.exibir_noticia, name='exibir_noticia'),

]
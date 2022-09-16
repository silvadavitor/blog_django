from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id_noticia>', views.exibir_noticia, name='exibir_noticia'),
    path('Dia-a-Dia/', views.index_2),
    path('Mercado_transferencia/', views.index_3),
    path('sobre/', views.sobre),

]
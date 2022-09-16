from django.shortcuts import render, get_object_or_404
from .models import Publicacao


# Create your views here.


def index(request):
    publicacoes = Publicacao.objects.all()
    return render(request, 'publicacoes/index.html',
                  {'publicacoes': publicacoes})


def exibir_noticia(request, id_noticia):
    publicacao = get_object_or_404(Publicacao, id=id_noticia)
    return render(request, 'publicacoes/exibir_noticia.html',
                  {'noticia': publicacao})


def index_2(request):
    publicacoes = Publicacao.objects.filter(categorias='1')
    return render(request, 'publicacoes/index.html',
                  {'publicacoes': publicacoes})


def index_3(request):
    publicacoes = Publicacao.objects.filter(categorias='3')
    return render(request, 'publicacoes/index.html',
                  {'publicacoes': publicacoes})


def sobre(request):
    return render(request, 'publicacoes/sobre.html',
                  {'sobre': sobre})

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

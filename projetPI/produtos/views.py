from django.shortcuts import render
from .import models


       


def listagem(request):
    alunos = models.Aluno.objects.all()
    return render(request, 'produtos/listagem.html', {'alunos': alunos})

def detalhes(request, id):
    aluno = models.Aluno.objects.get(id=id)
    return render(request, 'produtos/detalhes.html', {'aluno': aluno})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Projeto, Material
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    context = {
        'total_p': Projeto.objects.filter(ativo=True).count(),
        'total_l': Material.objects.filter(ativo=True).count(),
    }
    return render(request, 'gestao/index.html', context)

@login_required
def lista_projetos(request):
    projetos = Projeto.objects.filter(ativo=True).order_by('-data_inicio')
    return render(request, 'gestao/projectos.html', {'projetos': projetos})

@login_required
def lista_biblioteca(request):
    materiais = Material.objects.filter(ativo=True)
    return render(request, 'gestao/minibiblioteca.html', {'materiais': materiais})

# Ações para Projetos
def ocultar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    projeto.ativo = False
    projeto.save()
    return redirect('lista_projetos')

def eliminar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    projeto.delete()
    return redirect('lista_projetos')

# Ações para Biblioteca
def ocultar_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    material.ativo = False
    material.save()
    return redirect('lista_biblioteca')
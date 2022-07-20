from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

def homepage(request):
    return render(request,"main/inicio.html", {"cursos": Curso.objects.all})
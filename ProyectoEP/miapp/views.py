from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

def cursos(request):
    return render(request, 'cursos.html', {

    })

def crear_cursos(request):
    return render(request, 'crear_cursos.html', {

    })

def carreras(request):
    return render(request,'carreras.html',{

    })
def crear_carreras(request):
    return render(request, 'crear_carreras.html', {

    })
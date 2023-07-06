from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

def index(request):
    estudiantes = [ 'Isabella Caballero',
                    'Alejandro Hermitaño',
                    'Joan Palomino',
                    'Pierre Bernaola']
    estudiantes = []
    return render(request, 'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto Web Con DJango',
        'estudiantes': estudiantes
    })

def saludo(request):
    return render(request, 'saludo.html', {
        'titulo':'Saludo',
        'autor_saludo':'Mg. Flor Elizabeth Cerdán León'
    })

def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a,b+1)
    return render(request,'rango.html',{
        'titulo':'Rango',
        'a':a,
        'b':b,
        'rango_numeros':rango_numeros
    })
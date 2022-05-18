from django.shortcuts import render
from .models import caracteristicas
from .VBPR import Recomendacion, listar

def home(request):
    return render(request,'inicio.html')

def extraction(request):
    return render(request, 'extraction.html')

def recomendacion(request):
    
    datos = request.POST
    Recomendacion(datos)
    resultados, Metricas = listar()
    
    print(resultados)

    return render(request, 'formulario_recomendacion.html', {'resultados':resultados, 'Metricas':Metricas})

def VBPR(request):
    carac = caracteristicas.objects.all()

    return render(request,'formulario_recomendacion.html', {'carac': carac})
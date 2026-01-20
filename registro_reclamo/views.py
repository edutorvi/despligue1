from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from django.http import HttpResponse

def verhola(request):    
    return HttpResponse("Hola mundo")

def inicio(request):    
    return HttpResponse("Esta es la pagina por defecto")

def Verbase(request):
    return render(request, 'base.html')

def VerGrafico(request):
    return render(request, "registro_reclamo/grafico.html")



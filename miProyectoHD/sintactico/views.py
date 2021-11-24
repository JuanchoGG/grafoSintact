from django.shortcuts import render
from home.models import Tessiu
import math

# Create your views here.

L=Tessiu.objects.get_queryset()

def sintactico(request):

    diccionario={'lista':L, 'distan':distancias,}
    template_name= 'sintactico\index.html'
    return render(request, template_name, diccionario)

def dist(lista):
    matriz = []
    for x in lista:
        fila=[]
        for y in lista:
            d= math.sqrt(((x.temperatura - y.temperatura)**2) + ((x.color - y.color)**2) + ((x.inflamation - y.inflamation)**2))
            fila.append(d)
        matriz.append(fila)
    return matriz

distancias=dist(L)

def grafo (distancias, umbral):
    tabla=[]
    for x in range(len(distancias)):
        filaDist=distancias[x]
        for y in range(len(distancias)):
            if y>=x:
                if filaDist[y]<umbral:
                    tabla.append(['R'+str(x+1),'R'+str(y+1),filaDist[y],'Si'])
                else:
                    tabla.append(['R'+str(x+1),'R'+str(y+1),filaDist[y],'No'])
    print(len(tabla))
    return tabla

def enviar(request):
    template_name= 'sintactico\index.html'

    if(request.method == 'POST'):
        umbral = int(request.POST['umbral'])
        print(umbral)
    tabla=grafo(distancias,umbral)

    diccionario={'lista':L, 'distan':distancias, 'grafo':tabla}
    return render(request, template_name, diccionario)
    
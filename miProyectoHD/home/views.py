from django.shortcuts import render
from .models import Tessiu

# Create your views here.

def home(request):
    #return HttpResponse('Bienvenido a casa')
    L=Tessiu.objects.get_queryset()

    diccionario={'lista':L}

    template_name= 'home\index.html'
    return render(request, template_name, diccionario)

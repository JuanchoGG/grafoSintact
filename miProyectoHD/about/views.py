from django.shortcuts import render

# Create your views here.

def about(request):
    #return HttpResponse('Bienvenido a casa')
    template_name= 'about\index.html'
    return render(request, template_name, {})
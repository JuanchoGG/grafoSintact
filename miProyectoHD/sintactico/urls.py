from django.urls import path
from .views import enviar, sintactico

app_name= 'sintactico'
urlpatterns=[
    path('', sintactico, name='sintactico'),
    path('grafo/', enviar, name='grafo')
]

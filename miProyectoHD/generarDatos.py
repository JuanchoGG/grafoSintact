import csv
import random

nRegistros= int(input('Número de registros a generar: '))
valMax= int(input('Valor numérico máximo a generar en las columnas: '))

with open('datos.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(nRegistros):
        texto = [random.randint(0,valMax), random.randint(0,valMax), random.randint(0,valMax)]
        writer.writerow(texto)
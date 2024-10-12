#escribe un programa que te pregunta un radio de un circulo. Calcula la circumfrerncia.
# Round la circumferencia. y calculas al cuadrado el circumference.


import math



radius =float(input('Write the radius of the circle '))

circumference = radius * math.pi * 2
circumference = round(circumference)
circumference = pow(circumference ,2)
print(f'your result is {circumference}')

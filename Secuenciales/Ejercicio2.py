"""
Calcular el perímetro y área de un rectángulo dada su base y su altura.
"""

base = int(input("Dime la base: "))
altura = int(input("Dime la altura: "))

area = base * altura
perimetro = (base * 2) + (altura * 2)

print("El area es: ", area)
print("El perimetro es: ", perimetro)

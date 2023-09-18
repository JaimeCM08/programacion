"""
Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
"""

cateto1 = int(input("Dime el valor del primer cateto: "))
cateto2 = int(input("Dime el valor del segundo cateto: "))

hipotenusa = ((cateto2 ** 2) + (cateto1 ** 2)) ** (1/2)

print("La hipotenusa es: ", hipotenusa)

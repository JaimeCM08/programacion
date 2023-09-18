"""
Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
"""

num1 = int(input("Dime el primer numero: "))
num2 = int(input("Dime el segundo numero: "))

suma = num1 + num2
res = abs(num1 - num2)
mul = num1 * num2
div = num1 // num2

print("La suma es: ", suma)
print("La resta es: ", res)
print("La multiplicacion es: ", mul)
print("La division es: ", div)

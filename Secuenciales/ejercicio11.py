"""
Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia, de modo que el
resultado sea siempre positivo).
"""

num1 = int(input("Dime el primer punto: "))
num2 = int(input("Dime el segundo punto: "))

distancia = abs(num1 - num2)

print("La distancia entre esos puntos es: ", distancia)

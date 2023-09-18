"""
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
"""

faren = int(input("Dime los grados fahrenheit que quieras pasar a grados centigrados: "))

celsius = (faren - 32) * 5 / 9

print(faren, "º Fahrenheit son: ", celsius, "º Celsius")

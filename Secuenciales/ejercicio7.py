"""
Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
"""

minutos = int(input("Dime los minutos que quieres transformar en horas y minutos corresponde: "))

horas = minutos // 60
minutos = minutos - (horas * 60)

print(horas, " horas y ", minutos, " minutos")

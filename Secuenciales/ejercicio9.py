"""
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar
finalmente por su compra.
"""

DESCUENTO = 0.15

compra = int(input("Dime cuanto cuesta la compra: "))

total = compra - (compra * DESCUENTO)

print("El total de la compra es: ", total)

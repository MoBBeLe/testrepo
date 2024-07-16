# -*- coding: utf-8 -*-
"""
Created on Wed May 29 21:17:19 2024

@author: laura
"""

# Clase 1 

print("datos de la primera persona")

nombre1 = input("Ingrese el nombre del producto: ")
precio1 = int(input("Ingrese el precio: "))
nombre2 = input("Ingrese el nombre del producto: ")
precio2 = int(input("Ingrese el precio: "))

BONIFICACION = 20 #una constante 

precio_compra = precio1 + precio2
comparar = precio1 >= precio2
logico = (precio1 < precio2 and precio1 == precio2)

cabecera = "resultado del producto {0} y del producto {1}:"

print(cabecera.format(nombre1, nombre2))
print("El precio del primer valor es mayor o igual a el precio del segundo valor:")
print(comparar)

print("La suma de los dos productos es: " + str(precio_compra))
print("precio1 < precio2 and precio1 == precio2")
print(logico)

precio_compra += BONIFICACION
print("al precio total le incrementamso su valor que tiene la constante:" + str(precio_compra))



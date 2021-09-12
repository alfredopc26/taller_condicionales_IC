# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 11:06:49 2021

@author: Carlos Perez
"""
import random


#
#Punto 1
#Calcular total a pagar por camisas con descuento por mas de 3 camisas


def total_pago(cantidad, precio):
    
    
    subtotal = cantidad * precio
    
    if cantidad >= 3:
        descuento = subtotal * 0.30
    else:
        descuento = subtotal * 0.10
        
    return subtotal - descuento


precio = int(input('Digite el precio de la camisa: \n'))
cantidad = int(input('Digite la cantidad a comprar: \n'))
print(f'El valor total a pagar es : {total_pago(cantidad, precio)}')
#
#Punto 2
#Descuento por numero escogido al azar
#

def descuento_num_azar(subtotal):
    
    
    num = random.randint(0, 99)
    if num >= 74:
        descuento = subtotal * 0.20
    else:
        descuento = subtotal * 0.15
    
    return { 'num': num, 'descuento': descuento }

subtotal = int(input('Digite el subtotal de la compra: \n'))
result = descuento_num_azar(subtotal)
print(f"El numero al azar es : {result['num']}")
print(f"El descuento es de : $ {result['descuento']}")
#
#Punto 3
#cuota a pagar al cliente por monto
#

def cuota_pagar(monto):
    
    
    if monto >= 50000:
        cuota = monto * 0.02
    else:
        cuota = monto * 0.03
        
    return cuota

monto = int(input('Digite el monto del cliente: \n'))
print(f'La cuota a pagar es de: $ {cuota_pagar(monto)}')
#
#Punto 4
#Dinero de multa por contaminacion
#

def check_multa(puntos, g_diarias):
    
    multa = 0
    
    if(puntos > 170):
        multa = (g_diarias * 5) * 0.50
    
    return multa

g_diarias = float(input('Digite las ganancias diarias de la fabrica: \n'))
puntos = float(input('Registre los puntos de contaminacion de la fabrica:'))
print(f'La multa a pagar es de: $ {check_multa(puntos, g_diarias)}')
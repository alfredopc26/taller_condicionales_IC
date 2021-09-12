# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 11:06:49 2021

@author: Carlos Perez
"""
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
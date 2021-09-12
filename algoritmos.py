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
#
#Punto 5
#Ayuda a decidir compra de terreno o automovil

def det_compra(dev_auto, inc_terreno):
    
    mit_terreno = inc_terreno / 2
    comprar = False
    if dev_auto < mit_terreno:
        comprar = True
        
    return comprar

dev_auto = int(input('Digite devaluacion de Automovil: '))
inc_terreno = int(input('Digite incremento de terreno: '))
compra = det_compra(dev_auto, inc_terreno)
if compra:
    print('Si debes comprar el Automovil')
else:
    print('No debes comprar el Automovil.')
#
#Punto 6
#descuento por numeros de computadoras compradas

def desc_computadores(cant_comp):
    
    precio_base = 11000
    if cant_comp < 5:
        descuento = 0.10
    elif cant_comp >= 5 and cant_comp < 10:
        descuento = 0.20
    else:
        descuento = 0.40
    return { 'descuento': descuento, 'total': (precio_base*cant_comp) - descuento}

cant_comp = int(input('Digite la cantidad de computadores a comprar: \n'))
result = desc_computadores(cant_comp)
print(f"Se le hizo un descuento de : % {result['descuento']*100}")
print(f"El total de la compra fue : $ {result['total']}")
#
#Punto 7
#Descuento sobre precio sin iva

def desc_preciosiniva(p_unit, marca):
    
    descuento1 = 0
    descuento2 = 0
    iva = p_unit*0.16
    
    if p_unit >= 2000:
        descuento1 = p_unit * 0.10
        
    if marca == 1:
        descuento2 = p_unit * 0.05
        
    return { 
        'descuento_valor': descuento1,
        'descuento_marca': descuento2,
        'total': p_unit - descuento1 - descuento2 + iva
        }


p_unit = float(input('Digite el precio del aparato: \n'))
marca = int(input('Seleccione la marca: \n 1. NOSY \n 2. Sungsam \n 3. GL\n 4. Otra \n '))
result = desc_preciosiniva(p_unit, marca)
print(f"El descuento por precio aplicado es de : $ {result['descuento_valor']}")
print(f"El descuento por marca aplicado es de : $ {result['descuento_marca']}")
print(f"El total de la compra es de : $ {result['total']}")
#
#Punto 8
#Pago a fabricante, cantidad a invertir, valor prestamo, valor credito e intereses

def compra_fabricante(monto):
    
    prestamo = 0
    if monto >= 500000:
        invertir = monto * 0.55
        prestamo = monto * 0.30
        credito = monto * 0.15        
    else:
        invertir = monto * 0.70
        credito = monto * 0.30
    interes = credito * 0.20
    
    return {
        'invertir' : invertir,
        'prestamo' : prestamo,
        'credito' : credito,
        'intereses' : interes
        }

monto = float(input('Digite el monto de la compra: \n'))
result = compra_fabricante(monto)
print(f"La cantidad a invertir es : $ {result['invertir']}")
print(f"El valor del prestamo : $ {result['prestamo']}")
print(f"El valor del credito es: $ {result['credito']}")
print(f"El valor de los intereses son : $ {result['intereses']}")
#
# Punto 9
# Leer dos numeros, iguales mult, may sum, rest

def num_operacion(numA, numB):
    
    if numA == numB:
        result = numA * numB
    elif numA > numB:
        result = numA - numB
    else:
        result = numA + numB
        
    return result

numA = int(input('Digite el primer numero: \n'))
numB = int(input('Digite el segundo numero: \n'))
print(f"El resultado es : {num_operacion(numA, numB)}")
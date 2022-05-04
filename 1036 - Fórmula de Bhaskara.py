# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
import math

A,B,C = input().split()
A,B,C = float(A),float(B),float(C)

#Calculando o Delta:

delta = B**2 - 4*A*C

if A==0 or delta<0:
    print('Impossivel calcular')
else:
    R1 = (-B + math.sqrt(delta))/(2*A)
    R2 = (-B - math.sqrt(delta))/(2*A)
    print('R1 = {:.5f}'.format(R1))
    print(f'R2 = {R2:.5f}')
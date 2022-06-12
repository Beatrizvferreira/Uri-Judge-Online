# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from math import pow
A,B,C = input().split()
A=float(A)
B=float(B)
C=float(C)


if A >= B and B >= C:
    maior_1 = A
    maior_2 = B
    maior_3 = C

elif A>=B and C>=A :
    maior_1 = C
    maior_2 = A
    maior_3 = B
    
elif B>=A and A>=C:
    maior_1 = B
    maior_2 = A
    maior_3 = C

elif B>=A and C>=B:
    maior_1 = C
    maior_2 = B
    maior_3 = A

elif C>=A and A>=B:
    maior_1 = C
    maior_2 = A
    maior_3 = B

elif C>=A and B>=C:
    maior_1 = B
    maior_2 = C
    maior_3 = A

if maior_1 >= maior_2 + maior_3:
    print('NAO FORMA TRIANGULO')
else:
    if pow(maior_1,2) == pow(maior_2,2) + pow(maior_3,2):
        print('TRIANGULO RETANGULO')
        
    if pow(maior_1,2) > pow(maior_2,2) + pow(maior_3,2):
        print('TRIANGULO OBTUSANGULO')

    if pow(maior_1,2) < pow(maior_2,2) + pow(maior_3,2):
        print('TRIANGULO ACUTANGULO')

    if maior_1 == maior_2 and maior_2 == maior_3:
        print('TRIANGULO EQUILATERO')

    elif maior_1 == maior_2 or  maior_2 == maior_3 or maior_1 == maior_3:
        print('TRIANGULO ISOSCELES')
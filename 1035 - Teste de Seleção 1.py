# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
A,B,C,D = input().split()
A,B,C,D =  int(A),int(B),int(C),int(D)

E=C+D
F=A+B

if B>C and D>A and E>F and C>=0 and D>=0 and A%2==0:
    print('Valores aceitos') 
else:
    print('Valores nao aceitos')


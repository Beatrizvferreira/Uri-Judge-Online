# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

x,y = input().split()
x = float(x)
y = float(y)

if x == 0 and y == 0:
    print('Origem')
else:
    if x == 0:
        print('Eixo Y')
    else:
        if y == 0:
            print('Eixo X')
        else:
            if x>0 and y>0:
                print('Q1')
            else:
                if x>0 and y<0:
                    print('Q4')
                else:
                    if x<0 and y>0:
                        print('Q2')
                    else:
                        if x<0 and y<0:
                            print('Q3')
    



# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

x,y,z = input().split()
x = int(x)
y = int(y)
z = int(z)

if x>y and x>z:
    maior_1 = x
    if y>z:
        maior_2 = y
        maior_3 = z
    else:
        maior_2 = z
        maior_3 = y
else:
    if y>x and y>z:
        maior_1 = y
        if x>z:
            maior_2 = x
            maior_3 = z
        else:
            maior_2 = z
            maior_3 = x
    else:
        maior_1 = z
        if x>y:
            maior_2 = x
            maior_3 = y
        else:
            maior_2 = y
            maior_3 = x

print(f'{maior_3}')
print(f'{maior_2}')
print(f'{maior_1}\n')

print(f'{x}')
print(f'{y}')
print(f'{z}')
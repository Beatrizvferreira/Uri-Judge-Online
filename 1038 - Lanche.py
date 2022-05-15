# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
cod, qnt = input().split()
cod = int(cod)
qnt = int(qnt)

preco = [4, 4.5, 5, 2, 1.5]


aux = preco[cod-1]
valor = aux*qnt
print(f'Total: R$ {valor:.2f}')
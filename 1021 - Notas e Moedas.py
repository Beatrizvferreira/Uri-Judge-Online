# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    qt_notas = int(valor / nota)
    print('{} nota(s) de R$ {:.2f}'.format(qt_notas, nota))
    valor -= qt_notas * nota

print('MOEDAS:')
for moeda in moedas:
    valor = round(valor, 2)
    qt_moedas = int(valor / moeda)
    print('{} moeda(s) de R$ {:.2f}'.format(qt_moedas, moeda))
    valor -= qt_moedas * moeda
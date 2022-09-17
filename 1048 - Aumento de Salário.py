# -*- coding: utf-8 -*-

salario = float(input())

if salario>=0 and salario<=400:
    aumento = salario*1.15
elif salario>400 and salario<=800:
    aumento = salario*1.12
elif salario>800 and salario<=1200:
    aumento = salario*1.10
elif salario>1200 and salario<=2000:
    aumento = salario*1.07
else:
    aumento = salario*1.04

percentual = (aumento/salario - 1)*100
percentual = round(percentual)
reajuste  = aumento - salario

print(f'Novo salario: {aumento:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')
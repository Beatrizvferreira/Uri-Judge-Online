# -*- coding: utf-8 -*-

salario = float(input())

if salario <= 2000:
    print('Isento')
else:
    aux = salario - 2000
    if aux <= 1000:
        imposto = aux*0.08
    else:
        aux = aux - 1000
        imposto = 1000*0.08
        if aux <= 1500:
            imposto = imposto + aux*0.18
        else:
            aux = aux - 1500
            imposto = imposto + 1500*0.18 + aux*0.28
    print(f'R$ {imposto:.2f}')
        
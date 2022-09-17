# -*- coding: utf-8 -*-

lista = []

for i in range(4):
    lista.append(input().split(' '))
    if i == 0 or i == 2:
        lista[i][1] = int(lista[i][1])
    else:
        for j in range(0,5,2):
            lista[i][j] = int(lista[i][j])     

dia = lista[2][1] - lista[0][1]
if lista[1][0] <= lista[3][0]:
    horas = lista[3][0] - lista[1][0]
else:
    horas = 24 - lista[1][0] + lista[3][0]
    dia -=1

if lista[1][2] <= lista[3][2]:  
    minutos = lista[3][2] - lista[1][2]
else:
    minutos = 60 - lista[1][2] + lista[3][2]
    horas -=1

if horas < 0:
    horas = 24 + horas
    dia -=1

if lista[1][4] <= lista[3][4]:
    segundos = lista[3][4] - lista[1][4]
else:
    segundos = 60 - lista[1][4] + lista[3][4]
    minutos -=1
    

print('{} dia(s)'.format(dia))
print('{} hora(s)'.format(horas))
print('{} minuto(s)'.format(minutos))
print('{} segundo(s)'.format(segundos)) 
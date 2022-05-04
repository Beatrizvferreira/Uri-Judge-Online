# -*- coding: utf-8 -*-


from math import floor

seg = int(input())

horas = seg/3600
horas = floor(horas)

seg = seg - horas*3600
minutos = seg/60
minutos = floor(minutos)

segundos = seg - minutos*60
segundos = seg % 60

print(f'{horas}:{minutos}:{segundos}')
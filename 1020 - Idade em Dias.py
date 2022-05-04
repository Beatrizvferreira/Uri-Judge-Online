# -*- coding: utf-8 -*-

import math

Qnt_dias = int(input())

anos = Qnt_dias/365
anos = math.floor(anos)
Qnt_dias = Qnt_dias - anos*365

meses = Qnt_dias/30
meses = math.floor(meses)
Qnt_dias = Qnt_dias - meses*30

dias = Qnt_dias 

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')








# -*- coding: utf-8 -*-

h_i,h_f = input().split()
h_i = int(h_i)
h_f = int(h_f)


if h_i == h_f:
    h=24
else:
    if h_i<h_f:
        h = h_f-h_i
    else:
        h = 24 - h_i + h_f

print(f'O JOGO DUROU {h} HORA(S)')
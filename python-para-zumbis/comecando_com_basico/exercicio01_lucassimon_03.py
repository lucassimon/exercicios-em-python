# -*- coding: utf-8 -*-
__author__ = u'lucas simon'

u"""
lista de exercicios 01

Url: https://pingmind-private.s3.amazonaws.com/exercises/attachments/Lista_de_Exerc%C3%ADcios_I_Python_para_Zumbis.pdf?Signature=m20t0GoOXGi3SuVG8WujkY6YJUA%3D&Expires=1380467241&AWSAccessKeyId=AKIAIEIV5JA2YZL4TUJA

Enunciado:
Escreva um programa que leia a quantidade de dias, horas, minutos
e segundos do usuário. Calcule o total em segundos.

LOGICA:
1 DIA = 86400 seg
1 HORA = 3600 seg
1 MIN = 60 seg

"""


dias = int(input(u'Informe o numero de DIAS:\n>'))
horas = int(input(u'Informe o numero de HORAS:\n>'))
min = int(input(u'Informe o numero de MINUTOS:\n>'))
seg = int(input(u'Informe o numero de SEGUNDOS:\n>'))

total = (dias*84600) + (horas*3600) + (min*60) + seg

print(
    u'O total em segundos é, %ds'
    % (total)
)

# -*- coding: utf-8 -*-
__author__ = u'lucas simon'

u"""
lista de exercicios 01

Url: https://pingmind-private.s3.amazonaws.com/exercises/attachments/Lista_de_Exerc%C3%ADcios_I_Python_para_Zumbis.pdf?Signature=m20t0GoOXGi3SuVG8WujkY6YJUA%3D&Expires=1380467241&AWSAccessKeyId=AKIAIEIV5JA2YZL4TUJA

Enunciado:
Faça um programa que peça dois números inteiros e imprima
a soma desses dois números
"""


num1 = int(input(u'Informe o primeiro número:\n>'))
num2 = int(input(u'Informe o segundo número:\n>'))

print(
    u'A soma dos números (%d+%d) é, %d'
    % (num1, num2, num1+num2)
)

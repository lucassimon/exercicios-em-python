# -*- coding: utf-8 -*-
__author__ = u'lucas simon'

u"""
lista de exercicios 01

Url: https://pingmind-private.s3.amazonaws.com/exercises/attachments/Lista_de_Exerc%C3%ADcios_I_Python_para_Zumbis.pdf?Signature=m20t0GoOXGi3SuVG8WujkY6YJUA%3D&Expires=1380467241&AWSAccessKeyId=AKIAIEIV5JA2YZL4TUJA

Enunciado:
Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
"""


num1 = int(input(u'Informe a quantidade em metros:\n>'))

print(
    u'A quantidade de %dm convertido para milimetros é, %dmm'
    % (num1, num1*(10**3))
)

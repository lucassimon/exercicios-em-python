# -*- coding: utf-8 -*-
__author__ = u'lucas simon'

u"""
lista de exercicios 01

Url: https://pingmind-private.s3.amazonaws.com/exercises/attachments/Lista_de_Exerc%C3%ADcios_I_Python_para_Zumbis.pdf?Signature=m20t0GoOXGi3SuVG8WujkY6YJUA%3D&Expires=1380467241&AWSAccessKeyId=AKIAIEIV5JA2YZL4TUJA

Enunciado:
Faça agora o contrário, de Fahrenheit para Celsius
"""

valor_farenheint = float(input(u'Informe a temperatura em celsius:\n>'))

print(
    u'O valor %.2f celsius em fareheints é %.2f'
    % (valor_farenheint, ((valor_farenheint - 32) * 5/9))
)

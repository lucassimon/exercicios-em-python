# -*- coding: utf-8 -*-
__author__ = u'lucas simon'

u"""
lista de exercicios 01

Url: https://pingmind-private.s3.amazonaws.com/exercises/attachments/Lista_de_Exerc%C3%ADcios_I_Python_para_Zumbis.pdf?Signature=m20t0GoOXGi3SuVG8WujkY6YJUA%3D&Expires=1380467241&AWSAccessKeyId=AKIAIEIV5JA2YZL4TUJA

Enunciado:
Solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.
"""


preco_mercadoria = float(input(u'Informe o preço da mercadoria:\n>'))
porcentagem_desconto = float(input(u'Informe a porcentagem de desconto:\n>'))

total = preco_mercadoria - ((porcentagem_desconto*preco_mercadoria)/100)

print(
    u'O total recebido é, %.2f'
    % (total)
)

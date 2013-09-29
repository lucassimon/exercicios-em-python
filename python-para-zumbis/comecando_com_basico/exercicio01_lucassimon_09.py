# -*- coding: utf-8 -*-
__author__ = u'lucas simon'

u"""
lista de exercicios 01

Url: https://pingmind-private.s3.amazonaws.com/exercises/attachments/Lista_de_Exerc%C3%ADcios_I_Python_para_Zumbis.pdf?Signature=m20t0GoOXGi3SuVG8WujkY6YJUA%3D&Expires=1380467241&AWSAccessKeyId=AKIAIEIV5JA2YZL4TUJA

Enunciado:
Escreva um programa que pergunte a quantidade de km percorridos por um carro
alugado pelo usuário, assim como a quantidade de dias pelos quais o carro
foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00
por dia e R$ 0,15 por km rodado.
"""

CARRO_DIA = 60.00
KM_RODADO = 0.15

quilometros_percorridos = float(input(u'Informe os quilometros percorridos:\n>'))
dias_alugados = int(input(u'Informe a quantidade de dias alugados:\n>'))

total = (dias_alugados * CARRO_DIA) + (quilometros_percorridos * KM_RODADO)

print(
    u'O valor total %.2f'
    % (total)
)

# -*- coding: utf-8 -*-
__author__ = u'lucas simon'

u"""
lista de exercicios 01

Url: https://pingmind-private.s3.amazonaws.com/exercises/attachments/Lista_de_Exerc%C3%ADcios_I_Python_para_Zumbis.pdf?Signature=m20t0GoOXGi3SuVG8WujkY6YJUA%3D&Expires=1380467241&AWSAccessKeyId=AKIAIEIV5JA2YZL4TUJA

Enunciado:
Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer
e a velocidade média esperada para a viagem.
"""

print ("""
Entenda a equação básica: D = r*t. Onde "D" é a distância,
"v" é a velocidade e "t" é o tempo.
Se lhe forem dadas a velocidade a qual alguém está viajando
e o tempo que demora a viagem, pode-se usar a equação
para calcular a distância total percorrida.
\n\n
""")

print("""
Resolva um problema usando a fórmula. Por exemplo, se um carro
viaja a 100 quilômetros por hora e a viagem dura 2 horas,
pode-se facilmente calcular a distância que o carro percorre:
Distância = 100 Km/h x 2 horas Distância = 200 quilômetros
\n\n
""")
velocidade = int(input(u'Informe a velocidade media (Km/h):\n>'))
horas = int(input(u'Informe a quantidade de horas:\n>'))

print(
    u'\nO total percorrido, %.2f'
    % (velocidade * horas)
)

print("""
Modifique a fórmula para calcular o tempo. Se D = v*t, pode-se isolar "t"
em um dos lados da equação dividindo ambos os lados por "v".
Então a nova fórmula seria t = D/v. Suponha que se queira saber quanto
tempo demoraria para viajar 200 quilômetros a uma velocidade de 100 Km/h:
Tempo = 200 quilômetros / 100 Km/h Tempo = 2 horas
\n\n
""")
quilometros = float(input(u'Informe a quantidade de quilometros:\n>'))
velocidade = int(input(u'Informe a velocidade media (Km/h):\n>'))
horas_em_decimal = quilometros / velocidade
hora = int(horas_em_decimal)
minutos_em_decimal = (hora - horas_em_decimal).__abs__()
minutos = int(minutos_em_decimal * 60)

print(
    u'\nO tempo de viagem de carro foi de %dH:%dm.'
    % (hora, minutos)
)

print("""
Modifique a equação novamente para calcular a velocidade.
Se D = v*t, pode-se isolar "v" dividindo ambos os lados da equação
port "t" para chegar à fórmula v = D/t. Agora suponha que um carro
tenha viajado por 2 horas e coberto 200 quilômetros.
Um problema poderia pedir a que taxa de velocidade o carro estava viajando:
Velocidade = 200 quilômetros / 2 horas Velocidade = 100 Km/h
\n\n
""")
quilometros = float(input(u'Informe a quantidade de quilometros:\n>'))
velocidade = int(input(u'Informe a velocidade media (Km/h):\n>'))

print(
    u'\nO total percorrido, %.2f'
    % (quilometros / horas)
)

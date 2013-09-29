# -*- coding: utf-8 -*-
__author__ = u'lucas simon'

u"""
lista de exercicios 01

Url: https://pingmind-private.s3.amazonaws.com/exercises/attachments/Lista_de_Exerc%C3%ADcios_I_Python_para_Zumbis.pdf?Signature=m20t0GoOXGi3SuVG8WujkY6YJUA%3D&Expires=1380467241&AWSAccessKeyId=AKIAIEIV5JA2YZL4TUJA

Enunciado:
Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário.

"""


salario = float(input(u'Informe o salário atual:\n>'))
porcentagem = float(input(u'Informe a porcentagem de aumento:\n>'))

total = salario + ((porcentagem*salario)/100)

print(
    u'O total recebido é, %.2f'
    % (total)
)

u"""
A maneira mais simples de se resolver este problema é dividirmos o novo valor
do salário pelo valor antigo:

900 : 800 = 1,125

Subtraia 1 do valor encontrado e o multiplique por 100%.

O resultado é 12,5%, este é o percentual procurado.

Mas você sabe o porque destes cálculos? Vejamos, é simples!

Ao dividirmos 900 por 800 estamos encontrando a razão de 900 para 800,
ou seja, estamos comparando os dois valores. Esta comparação nos diz que o
número 900 é 1,125 vezes maior que o número 800.

E porque subtraímos 1 deste valor?

Bem, vejamos. Você se lembra, dos seus estudos de porcentagem, 
que 100% corresponde ao todo?

O todo neste caso seria o salário de R$ 800,00.

Lembra-se também que 100% equivale a 1 na sua forma decimal?

Pois então, ao subtrairmos 1 unidade, estamos na realidade descontando 
o valor do salário e ficando apenas com a parte correspondente ao aumento
que foi de R$ 100,00, ou seja, o 0,125 que sobrou nada mais é que o
percentual de aumento, só que na sua forma decimal.

É por isto que no último passo o multiplicamos por 100%.
Não acredita?!?!? É simples! Multiplique 800 por 0,125 e veja quanto dá!
Dá 100, exatamente o valor do aumento.
Uma outra prova seria realizarmos o cálculo inverso. Dividindo-se 100 por 0,125.
O resultado desta conta seria o valor inicial do salário.

Portanto:
Resposta

Os R$ 100,00 de aumento do meu salário correspondem a um aumento percentual de 12,5%.
"""
novo_salario = float(input(u'Informe o aumento de salário recebido:\n>'))

porcentagem_aumento = (1 - (novo_salario/salario)) * 100

valor_aumento = (salario * porcentagem_aumento.__abs__()) / 100

print(
    u'Os R$ %.2f de aumento do meu salario correspondem\
a um aumento percentual de %.2f.'
    % (valor_aumento, porcentagem_aumento.__abs__())
)

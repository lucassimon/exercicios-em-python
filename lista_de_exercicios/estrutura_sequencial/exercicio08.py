# -*- coding: utf-8 -*-
__author__ = 'lucas'

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# 8*5+4 = 44 horas por semana
# vezes 5 semanas
# = 220 por mes

# pega seu salario e divide por 220
# = salario por hora
# mas a conta pe assim q faz

horas_trabalhadas = int(input('Informe a quantidade de horas \
trabalhadas por dia:\n>'))

horas_semanais = horas_trabalhadas * 5 + 4
print 'Sua carga horaria por semana é %d horas * 5 semanas + 4 \
 horas do sabado, totalizando %d por semana' \
        % (horas_trabalhadas, horas_semanais)

horas_mensais = horas_semanais * 5

print 'Suas horas mensais é %d' % (horas_mensais)

salario = float(input('Informe o seu salario bruto:\n>'))

salario_hora = salario / horas_mensais

print 'Salario por hora %f' % (salario_hora)

# -*- coding: utf-8 -*-
__author__ = 'lucas'

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

lista_notas = [0,1,2,3]

for bimestre in range(0,4):
	numero = float( raw_input('Informe a nota do bimestre:\n> '))
	lista_notas[bimestre] = numero

print sum(lista_notas) / len(lista_notas)
# -*- coding: utf-8 -*-
__author__ = 'lucas'

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = input('Informe o raio do circulo:\n>')

area = math.pi * math.pow(raio, 2)

print 'O area do circulo é de %f' % area

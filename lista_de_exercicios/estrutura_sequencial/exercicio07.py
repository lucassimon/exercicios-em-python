# -*- coding: utf-8 -*-
__author__ = 'lucas'

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro
# desta área para o usuário.

import math

lado = input('Informe o lado do quadrado:\n>')

area = math.pow(lado, 2)

perimetro = 4 * lado

print 'O area do quadrado informado é %f' % area

print 'O perimetro do quadrado informado é %f' % perimetro

# -*- coding: utf-8 -*-
__author__ = 'lucas'

import unittest
from cheque import Cheque

class TestCheques(unittest.TestCase):
    def setUp(self):
        """
            Teste De inicializacao da classe Cheque
        """
        self.c = Cheque(150)

    def test_Object(self):
        """
            Teste para verificar se o objeto foi montado corretamente
        """
        self.assertTrue(self.c)

    def test_GetterNumeroInformado(self):
        """
            Teste do getter do número informado
        """
        self.assertEqual(self.c.numero,150)

    def test_SetterNumero(self):
        """
            Teste do setter do numero informado
        """
        self.c.numero = 151
        self.assertEqual(self.c.numero,151)

    def test_InitExcecaoString(self):
        """
            Teste do __init__ da classe Cheque
            para avaliar se esta levantando a excecão ao passar uma string
        """
        self.assertRaises(ValueError,Cheque,'2555')

    def test_SetterExcecaoString(self):
        """
            teste do @numero.setter da classe Cheque
            para avaliar se esta levantando a exceção ao passar uma string
        """
        self.assertRaises(ValueError,setattr,self.c,'numero','11111')


    def test_RetornoQuantidadeDeDigitos(self):
        """
            Teste para retonar a quantidade de parte inteira do numero
        """
        self.c.numero = 151
        self.assertEqual(self.c.qtdeNumeros(self.c.numero),5)

    def test_RetornoDoSplitDoNumero(self):
        """
            Teste que verifica se foi realizado o split do numero
        """
        self.c.numero = 1566.08
        self.assertListEqual(self.c.splitNumero(),['1566','08'])

if __name__ == '__main__':
    unittest.main()

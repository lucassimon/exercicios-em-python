# -*- coding: utf-8 -*-
__author__ = 'lucas'

class Cheque(object):

    def __init__(self,num):
        self._num = self._validaNumero(num)

    @property
    def numero(self):
        """
            Getter do numero informado
        """
        return self._num

    @numero.setter
    def numero(self,num):
        """
            Setter do numero informado
        """
        self._num = self._validaNumero(num)

    def _validaNumero(self,num):
        """
            Valida se o numero informado é uma string, se
            verdadeiro lança uma exceção.

            Senão converte o numero informado para float
        """
        # verifica se o numero é uma string
        if isinstance(num,str):
            # lanca uma exceção do tipo ValueError
            raise ValueError('Informe somente numeros')

        # retorna o numero convertido em float
        return float(num)

    def qtdeNumeros(self,numero):
        """
            Retorna a quantidade de digitos
        """
        return  len(str(numero))

    def splitNumero(self):
        """
            Transforma o numero do tipo float em string e
            depois faz um split dessa string devolvendo uma
            lista.

            Essa lista contém a parte inteira e a parte decimal

            Exemplo:
            >>> num ='1566.08'
            >>> a = num.split('.')
            >>> a[0]
            '1566'
            >>> a[1]
            '08'
            >>> a
            ['1566', '08']
        """
        return str(self._num).split('.')

    def retornaParteinteira(self):
        parte = self.splitNumero()
        return parte[0]

    def retornaPartedecimal(self):
        parte = self.splitNumero()
        return parte[1]

    def imprimirNumeroPorExtenso(self):

        dicionarioCasasDigitos = {
            1 : {1:'Um', 2:'Dois',3:'Tres',4:'Quatro',5:'Cinco',6:'Seis',7:'Sete',8:'Oito',9:'Nove',},
            2 : {1:'Dez', 2:'Vinte',3:'Trinta',4:'Quarenta',5:'Cinquenta',6:'Sesenta',7:'Setenta',8:'Oitenta',9:'Noventa',},
            3 : {1:'Cento',2:'Duzentos',3:'Trezentos',4:'Quatrocentos',5:'Quinhentos',6:'Seissentos',7:'Setecentos',8:'Oitocentos',9:'Novecentos',},
            4 : {1:'Um mil',2:'Dois mil',3:'Tres mil',4:'Quatro mil',5:'Cinco mil',6:'Seis mil',7:'Sete mil',8:'Oito mil',9000:'Nove mil',10000:'Dez mil'},
            7 : 'milhoes',
        }


        j = int(self.qtdeNumeros(self.retornaParteinteira())) + 1
        for i in  range(0,self.qtdeNumeros(self.retornaParteinteira())):
            j = j -1
            a = self.retornaParteinteira()
            print dicionarioCasasDigitos[j][int(a[i])]

      




if __name__ == '__main__':
    val1 = Cheque(116.0)
    print 'valor do numero é %0.2f' % val1.numero
    print val1.qtdeNumeros(val1.numero)

    print '======================================'
    val2 = Cheque(1566.08)
    print 'valor do numero é %0.2f' % val2.numero
    particionarNumero = val2.splitNumero()
    print 'parte inteira %s, parte decimal %s' % (val2.qtdeNumeros(particionarNumero[0]),val2.qtdeNumeros(particionarNumero[1]))

    val2.imprimirNumeroPorExtenso()
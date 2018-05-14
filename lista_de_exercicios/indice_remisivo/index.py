import re


class Index():

    def __init__(self, items):

        self._index = {}

        # Devido a entrada de dados ser obrigatóriamente um separados
        # por vírgula, criamos uma lista com as palavras digitadas pelo
        # usuário

        keywords = items.split(',')
        # TODO: verify if the keyword is a word or alphanumerical
        # see the method is_word

        # Inicializamos o dicionario/indice remissico removendo espaços
        self._index = {i.strip(): [] for i in keywords}

    @property
    def index(self):
        '''
        Propriedade index é um dicionário em python com uma lista
        '''
        return self._index

    def get_keywords(self):
        '''
        Retorna somente as keywords do indice remissivo como uma lista
        '''
        return list(self.index.keys())

    def add(self, word, line_number):
        '''
        Adiciona a ocorrencia da linha que encontrou uma palavra
        '''
        self.index[word].append(line_number)

    def is_word(self, word):
        '''
        Cabe ressaltar que uma palavra é considerada como uma
        sequência de letras e dígitos, começando
        com uma letra.
        '''
        if re.match("^[a-zA-Z]+.*", word):
            return True

        return False

    def verify(self, word, line):
        '''
        Verifica se a palavra do indice remissivo está na linha
        '''
        if word in line:
            return True

        return False

    def show(self):
        '''
        Imprime em ordem alfabética o indice remissivo
        '''
        keywords = self.get_keywords()
        keywords.sort()
        for i in keywords:
            items = ','.join(str(v) for v in self.index[i] if i)
            print('{} {}'.format(i, items))

    def search(self, word):
        '''
        Pesquisa uma palavra nas keywords do indice remissivo
        '''
        if word in self.index.keys():
            print('{} {}'.format(word, self.index[word]))

        else:
            print('Not found.')

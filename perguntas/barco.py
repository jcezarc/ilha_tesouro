from perguntas.pergunta import Pergunta
from perguntas.vermelha import Vermelha
from perguntas.azul import Azul


class Barco(Pergunta):
    def __init__(self):
        self.enunciado = '''
        Você atravessou o lago e encontrou uma cabana com 2 portas:
        Uma porta `vermelha` e uma porta `azul`. Qual você escolhe?
        '''
        self.opcoes = {'vermelha': Vermelha, 'azul': Azul}

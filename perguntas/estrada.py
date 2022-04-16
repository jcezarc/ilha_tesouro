from perguntas.pergunta import Pergunta
from perguntas.lago import Lago
from perguntas.floresta import Floresta


class Estrada(Pergunta):
    def __init__(self):
        self.enunciado = '''
        Seu carro quebrou numa bifurcação da estrada.
        Para onde você vai?
        '''
        self.opcoes = {'esquerda': Lago, 'direita': Floresta}

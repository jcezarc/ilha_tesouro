from perguntas.pergunta import Pergunta
from perguntas.crocodilo import Crocodilo
from perguntas.barco import Barco


class Lago(Pergunta):
    def __init__(self):
        self.enunciado = '''
        Você está na beira de um lago.
        Você pode nadar ou esperar o barco para atravessar.
        '''
        self.opcoes = {'nadar': Crocodilo, 'barco': Barco}

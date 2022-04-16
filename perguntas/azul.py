from perguntas.pergunta import Pergunta


class Azul(Pergunta):
    def __init__(self):
        self.enunciado = '''
        Atrás da porta azul havia uma armadilha...
        VOCÊ MORREU!
        '''
        self.opcoes = {}

    def proxima(self, resposta):
        return None

from perguntas.pergunta import Pergunta


class Crocodilo(Pergunta):
    def __init__(self):
        self.enunciado = '''
        O lago está infestado de crocodilos...
        VOCÊ MORREU!
        '''
        self.opcoes = {}

    def proxima(self, resposta):
        return None

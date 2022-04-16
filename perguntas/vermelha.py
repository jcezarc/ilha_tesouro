from perguntas.pergunta import Pergunta


class Vermelha(Pergunta):
    def __init__(self):
        self.enunciado = '''
        Parabéns você encontrou o tesouro!
        * * *  VOCÊ VENCEU!!! * * *
        '''
        self.opcoes = {}

    def proxima(self, resposta):
        return None

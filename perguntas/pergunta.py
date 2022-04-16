class Pergunta:
    def __init__(self):
        self.opcoes = {}
        self.enunciado = ''

    def proxima(self, resposta: str):
        classe = self.opcoes.get(resposta)
        if classe:
            return classe()
        return None

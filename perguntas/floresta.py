from perguntas.pergunta import Pergunta
# from perguntas.estrada import Estrada  # <<--- Referência Circular !!! CUIDADO * * * 
from perguntas.lago import Lago


class Floresta(Pergunta):
    extra = {}

    def __init__(self):
        self.enunciado = '''
        Você está perdido na floresta, à frente há um grande lago.
        Você pode voltar para a `estrada` ou ir em direção ao `lago`.
        '''
        self.opcoes = {
            'lago': Lago,
            # 'estrada': Estrada  # <<--- PROBLEMA...
        }
        self.opcoes.update(self.extra)

    # --- ...SOLUÇÃO: -----------------
    @classmethod
    def inclui_opcao(cls, nome: str, classe: type):
        cls.extra[nome] = classe

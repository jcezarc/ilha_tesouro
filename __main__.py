from perguntas.estrada import Estrada
from perguntas.floresta import Floresta

MENSAGEM_FIM = 'Pressione uma tecla para continuar...'

def jogo():
    print('Ilha do Tesouro'.center(50, '='))
    Floresta.inclui_opcao('estrada', Estrada)
    pergunta = Estrada()
    while pergunta:
        print(pergunta.enunciado)
        resposta = input('{} {} >>'.format(
            'Escolha:' if pergunta.opcoes else MENSAGEM_FIM,
            ', '.join(pergunta.opcoes.keys())
        ))
        pergunta = pergunta.proxima(resposta)


jogo()

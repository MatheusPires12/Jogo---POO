import pygame
from jogo import Jogo, mostrar_tela_selecao_nivel

if __name__ == "__main__":
    pygame.init()
    largura = 640
    altura = 480
    tela = pygame.display.set_mode((largura, altura))
    nivel_selecionado = mostrar_tela_selecao_nivel(tela)
    jogo = Jogo(nivel_selecionado)
    jogo.executar()
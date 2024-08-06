import pygame
from random import randint
from gerenciador_de_imagem import GerenciadorDeImagens

class Comida:
    def __init__(self, largura, altura, gerenciador_imagens):
        self.x_comida = randint(40, largura - 40)
        self.y_comida = randint(50, altura - 50)
        self.gerenciador_imagens = gerenciador_imagens

    def reposicionar(self, largura, altura):
        self.x_comida = randint(40, largura - 40)
        self.y_comida = randint(50, altura - 50)

    def get_rect(self):
        return pygame.Rect(self.x_comida, self.y_comida, 20, 20)

    def desenhar(self, tela):
        tela.blit(self.gerenciador_imagens.comida, (self.x_comida, self.y_comida))

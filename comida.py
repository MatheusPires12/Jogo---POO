import pygame
from random import randint

class Comida:
    def __init__(self, largura, altura):
        self.x_comida = randint(40, largura - 40)
        self.y_comida = randint(50, altura - 50)

    def reposicionar(self, largura, altura):
        self.x_comida = randint(40, largura - 40)
        self.y_comida = randint(50, altura - 50)

    def get_rect(self):
        return pygame.Rect(self.x_comida, self.y_comida, 20, 20)

    def desenhar(self, tela):
        pygame.draw.rect(tela, (255, 0, 0), (self.x_comida, self.y_comida, 20, 20))
import pygame
from random import randint

class Comida:
    def __init__(self, largura, altura, gerenciador_imagens):
        self.x_comida = randint(40, largura - 40)
        self.y_comida = randint(50, altura - 50)
        self.gerenciador_imagens = gerenciador_imagens

    def reposicionar(self, largura, altura, lista_cobra):
        while True:
            nova_posicao = (randint(20, largura - 40), randint(20, altura - 40)) 
            if nova_posicao not in lista_cobra:
                self.x_comida, self.y_comida = nova_posicao
                return

    def get_rect(self):
        return pygame.Rect(self.x_comida, self.y_comida, 20, 20)

    def desenhar(self, tela):
        tela.blit(self.gerenciador_imagens.comida, (self.x_comida, self.y_comida))


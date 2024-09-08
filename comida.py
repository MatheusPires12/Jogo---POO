import pygame
from random import randint

class Comida:
    def __init__(self, largura, altura, gerenciador_imagens):
        self.largura = largura
        self.altura = altura
        self.gerenciador_imagens = gerenciador_imagens
        self.x_comida = 0
        self.y_comida = 0
        self.reposicionar()  # Inicializa a posição da comida

    def reposicionar(self, lista_cobra=None, lista_obstaculos=None):
        if lista_cobra is None:
            lista_cobra = []
        if lista_obstaculos is None:
            lista_obstaculos = []

        while True:
            nova_posicao = (randint(20, self.largura - 40), randint(20, self.altura - 40))
            nova_comida_rect = pygame.Rect(nova_posicao[0], nova_posicao[1], 35, 35)
            
            # Verifica colisão com a cobra
            colisao = False
            for segmento in lista_cobra:
                segmento_rect = pygame.Rect(segmento[0], segmento[1], 35, 35)
                if nova_comida_rect.colliderect(segmento_rect):
                    colisao = True
                    break
            
            # Verifica colisão com obstáculos
            for obstaculo in lista_obstaculos:
                if nova_comida_rect.colliderect(obstaculo):
                    colisao = True
                    break
            
            # Se não houver colisão, posiciona a comida
            if not colisao:
                self.x_comida, self.y_comida = nova_posicao
                return

    def get_rect(self):
        return pygame.Rect(self.x_comida, self.y_comida, 20, 20)

    def desenhar(self, tela):
        tela.blit(self.gerenciador_imagens.comida, (self.x_comida, self.y_comida))

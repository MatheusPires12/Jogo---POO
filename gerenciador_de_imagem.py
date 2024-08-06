import pygame
import os

class GerenciadorDeImagens:
    def __init__(self):
        self.fundo = pygame.image.load("Imagens/fundo.png")
        self.comida = pygame.image.load("Imagens/Comida.png")
        self.cabeca = pygame.image.load("Imagens/Cabeça.png")
        self.corpo = pygame.image.load("Imagens/corpo.png")

    def desenhar_fundo(self, tela):
        tela.blit(self.fundo, (0, 0))

'''
    def desenhar_comida(self, tela):
        tela.blit(self.comida, (0, 0))
        self.cabeca = pygame.image.load("Jogo---POO/Imagens/Cabeça.png")
        self.corpo = pygame.image.load("Jogo---POO/Imagens/corpo.png")
        self.comida = pygame.image.load("Jogo---POO/Imagens/Comida.png")
        '''
    


import pygame
import os

class GerenciadorDeImagens:
    def __init__(self):
        self.fundo = pygame.image.load("Imagens/fundo.png")
        self.comida = pygame.image.load("Imagens/Comida.png")
        self.cabeca = pygame.image.load("Imagens/Cabeça.png")
        self.corpo = pygame.image.load("Imagens/corpo.png")
        self.rabo = pygame.image.load("Imagens/Rabo.png")

    def desenhar_fundo(self, tela):
        tela.blit(self.fundo, (0, 0))
    


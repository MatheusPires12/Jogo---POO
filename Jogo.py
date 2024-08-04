import pygame
from pygame.locals import *
from sys import exit
from cobra import Cobra
from comida import Comida

class Jogo:
    def __init__(self):
        pygame.init()
        self.largura = 600
        self.altura = 400
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Jogo da Cobrinha")
        self.relogio = pygame.time.Clock()
        self.fonte = pygame.font.SysFont('arial', 40, True, True)
        self.cobra = Cobra(self.largura, self.altura)
        self.comida = Comida(self.largura, self.altura)

    def executar(self):
        while True:
            self.relogio.tick(10)
            self.tela.fill((255, 255, 255))
            self.lidar_com_eventos()
            self.atualizar_jogo()
            self.desenhar_elementos()
            pygame.display.update()

    def lidar_com_eventos(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
            if evento.type == KEYDOWN:
                self.lidar_com_tecla_pressionada(evento)

    def lidar_com_tecla_pressionada(self, evento):
        if evento.key == K_a:
            self.cobra.x_controle = -self.cobra.velocidade
            self.cobra.y_controle = 0
        if evento.key == K_d:
            self.cobra.x_controle = self.cobra.velocidade
            self.cobra.y_controle = 0
        if evento.key == K_w:
            self.cobra.x_controle = 0
            self.cobra.y_controle = -self.cobra.velocidade
        if evento.key == K_s:
            self.cobra.x_controle = 0
            self.cobra.y_controle = self.cobra.velocidade
    
    def atualizar_jogo(self):
        self.cobra.mover()
        self.cobra.atualizar()
        self.checar_colisoes()

    def checar_colisoes(self):
        if self.cobra.x_cobra > self.largura:
            self.cobra.x_cobra = 0
        if self.cobra.x_cobra < 0:
            self.cobra.x_cobra = self.largura
        if self.cobra.y_cobra > self.altura:
            self.cobra.y_cobra = 0
        if self.cobra.y_cobra < 0:
            self.cobra.y_cobra = self.altura
    
    def desenhar_elementos(self):
        self.cobra.aumenta_cobra(self.tela)
        self.comida.desenhar(self.tela)

jogo = Jogo()

jogo.executar()

        


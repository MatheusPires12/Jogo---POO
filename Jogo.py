import pygame
from pygame.locals import *
from sys import exit

class Jogo:
    def __init__(self):
        pygame.init()
        self.largura = 600
        self.altura = 400
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Jogo da Cobrinha")
        self.relogio = pygame.time.Clock()
        self.fonte = pygame.font.SysFont('arial', 40, True, True)

    def executar(self):
        while True:
            self.relogio.tick(10)
            self.tela.fill((255, 255, 255))
            pygame.display.update()
            self.lidar_com_eventos()
    def lidar_com_eventos(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
jogo = Jogo()
jogo.executar()

        


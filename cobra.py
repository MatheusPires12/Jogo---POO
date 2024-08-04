import pygame

class Cobra:

    def __init__(self, largura, altura):
        self.x_cobra = int(largura / 2)
        self.y_cobra = int(altura / 2)
        self.velocidade = 10
        self.x_controle = self.velocidade
        self.y_controle = 0
        self.lista_cobra = []
        self.comprimento_inicial = 5

    def mover(self):
        self.x_cobra += self.x_controle
        self.y_cobra += self.y_controle
    
    def atualizar(self):
        lista_cabeca = [self.x_cobra, self.y_cobra]
        self.lista_cobra.append(lista_cabeca)
        if len(self.lista_cobra) > self.comprimento_inicial:
            del self.lista_cobra[0]
    
    def aumenta_cobra(self, tela):
        for XeY in self.lista_cobra:
            pygame.draw.rect(tela, (255, 255, 0), (XeY[0], XeY[1], 20, 20))
import pygame

class Cobra:

    def __init__(self, largura, altura, imagem_cabeca, imagem_corpo, imagem_rabo):
        self.x_cobra = int(largura / 2)
        self.y_cobra = int(altura / 2)
        self.velocidade = 10
        self.x_controle = self.velocidade
        self.y_controle = 0
        self.lista_cobra = []
        self.comprimento_inicial = 5
        self.imagem_cabeca = imagem_cabeca
        self.imagem_corpo = imagem_corpo
        self.imagem_rabo = imagem_rabo

    def mover(self):
        self.x_cobra += self.x_controle
        self.y_cobra += self.y_controle
    
    def atualizar(self):
        lista_cabeca = [self.x_cobra, self.y_cobra]
        self.lista_cobra.append(lista_cabeca)
        if len(self.lista_cobra) > self.comprimento_inicial:
            del self.lista_cobra[0]
    
    def aumenta_cobra(self, tela):
        for index, XeY in enumerate(self.lista_cobra):
            if index == len(self.lista_cobra) - 1:
                tela.blit(self.imagem_cabeca, (XeY[0], XeY[1]))
            if index == 0:
                tela.blit(self.imagem_rabo, (XeY[0], XeY[1]))
            else:
                tela.blit(self.imagem_corpo, (XeY[0], XeY[1]))
    
    def checar_colisao(self, comida):
        cobra_rect = pygame.Rect(self.x_cobra, self.y_cobra, 20, 20)
        return cobra_rect.colliderect(comida.get_rect())

    def reiniciar(self, largura, altura, imagem_cabeca, imagem_corpo, imagem_rabo):
        self.__init__(largura, altura, self.imagem_cabeca, self.imagem_corpo, self.imagem_rabo)

    def aumentar_velocidade(self, incremento):
        self.velocidade += incremento

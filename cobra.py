import pygame

class Cobra:

    def __init__(self, largura, altura, imagem_cabeca, imagem_corpo, imagem_rabo):
        self.x_cobra = int(largura / 2)
        self.y_cobra = int(altura / 2)
        self.velocidade = 10
        self.x_controle = self.velocidade
        self.y_controle = 0
        self.lista_cobra = []
        self.comprimento_inicial = 7
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
            
    def rotacionar_imagem(self, imagem, angulo):
        imagem_rotacionada = pygame.transform.rotate(imagem, -angulo)
        return imagem_rotacionada
    
    def aumenta_cobra(self, tela):
        for index, XeY in enumerate(self.lista_cobra):
            if index == len(self.lista_cobra) - 1:
                angulo = self.calcular_angulo()
                imagem_cabeca_rotacionada = self.rotacionar_imagem(self.imagem_cabeca, angulo)
                tela.blit(imagem_cabeca_rotacionada, (XeY[0], XeY[1]))
            elif index == 0:
                tela.blit(self.imagem_rabo, (XeY[0], XeY[1]))
            else:
                tela.blit(self.imagem_corpo, (XeY[0], XeY[1]))
    
    def calcular_angulo(self):
        if self.x_controle > 0:
            return 0
        elif self.x_controle < 0:
            return 180
        elif self.y_controle > 0:
            return 90
        elif self.y_controle < 0:
            return 270
        return 0
    
    def checar_colisao(self, comida):
        cobra_rect = pygame.Rect(self.x_cobra, self.y_cobra, 20, 20)
        return cobra_rect.colliderect(comida.get_rect())

    def reiniciar(self, largura, altura, imagem_cabeca, imagem_corpo, imagem_rabo):
        self.__init__(largura, altura, self.imagem_cabeca, self.imagem_corpo, self.imagem_rabo)

    def aumentar_velocidade(self, incremento):
        self.velocidade += incremento

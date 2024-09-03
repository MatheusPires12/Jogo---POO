import pygame

# Classe mãe que gerencia as imagens do jogo
class GerenciadorDeImagens:
    def __init__(self):
        self.comida = pygame.image.load("Imagens/Comida.png")
        self.cabeca = pygame.image.load("Imagens/Cabeça.png")
        self.corpo = pygame.image.load("Imagens/corpo.png")
        self.rabo = pygame.image.load("Imagens/Rabo.png")
        self.tela_inicial = pygame.image.load("Imagens/Comida.png")
        
    def desenhar_fundo(self, tela):
        tela.blit(self.tela_inicial, (0, 0))


class NivelFacil(GerenciadorDeImagens):
    def __init__(self):
        super().__init__()  
        self.fundo = pygame.image.load("Imagens/fundo.png")
        #self.velocidade = 5  # Exemplo de atributo específico

    def desenhar_fundo(self, tela):
        tela.blit(self.fundo, (0, 0))


class NivelMedio(GerenciadorDeImagens):
    def __init__(self):
        super().__init__()
        self.fundo = pygame.image.load("Imagens/Fundo_Game_Over.png")
        #self.velocidade = 10  # Exemplo de atributo específico

    def desenhar_fundo(self, tela):
        tela.blit(self.fundo, (0, 0))

class NivelDificil(GerenciadorDeImagens):
    def __init__(self):
        super().__init__()
        self.fundo = pygame.image.load("Imagens/fundo.png")
        #self.velocidade = 15  # Exemplo de atributo específico

    def desenhar_fundo(self, tela):
        tela.blit(self.fundo, (0, 0))

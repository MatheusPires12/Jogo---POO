import pygame

# Classe mãe que gerencia as imagens do jogo
class GerenciadorDeImagens:
    def __init__(self):
        self.fundo = pygame.image.load("Imagens/fundo.png")
        self.comida = pygame.image.load("Imagens/Comida.png")
        self.cabeca = pygame.image.load("Imagens/Cabeça.png")
        self.corpo = pygame.image.load("Imagens/corpo.png")
        self.rabo = pygame.image.load("Imagens/Rabo.png")
        self.tela_inicial = pygame.image.load("Imagens/INICIO.png")
        self.facil = pygame.image.load("Imagens/EASY.png")
        self.medio = pygame.image.load("Imagens/MEDIUM.png")
        self.dificil = pygame.image.load("Imagens/HARD.png")
        
    def desenhar_inicial(self, tela):
        tela.blit(self.tela_inicial, (0, 0))
        tela.blit(self.facil, (37, 373))
        tela.blit(self.medio, (230.72, 373))
        tela.blit(self.dificil, (424.44, 373))
        
    
    def desenhar_fundo(self, tela):
        tela.blit(self.fundo, (0, 0))


class NivelFacil(GerenciadorDeImagens):
    def __init__(self):
        super().__init__()  
        #self.velocidade = 5  # Exemplo de atributo específico


class NivelMedio(GerenciadorDeImagens):
    def __init__(self):
        super().__init__()
        self.obstaculo = pygame.image.load("Imagens/OBSTACULO_M.png")
        #self.velocidade = 10  # Exemplo de atributo específico

    def criar_rect_obstaculo(self):
        return pygame.Rect(279, 99.79, 114, 115) and pygame.Rect(279, 289.4, 114, 115)

    def desenhar_medio(self, tela):
        tela.blit(self.obstaculo, (279, 99.79))
        tela.blit(self.obstaculo, (279, 289.4))

class NivelDificil(GerenciadorDeImagens):
    def __init__(self):
        super().__init__()
        self.obstaculo = pygame.image.load("Imagens/OBSTACULO_M.png")
        #self.velocidade = 10  # Exemplo de atributo específico

    def criar_rect_obstaculo(self):
        return pygame.Rect(87, 63, 114, 115) and pygame.Rect(454, 63, 114, 115) and pygame.Rect(87, 309, 114, 115) and pygame.Rect(454, 309, 114, 115)

    def desenhar_dificil(self, tela):
        tela.blit(self.obstaculo, (87, 63))
        tela.blit(self.obstaculo, (454, 63))
        tela.blit(self.obstaculo, (87, 309))
        tela.blit(self.obstaculo, (454, 309))

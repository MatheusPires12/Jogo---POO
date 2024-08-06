import pygame
from pygame.locals import *
from sys import exit
from cobra import Cobra
from comida import Comida
from gerenciador_de_imagem import GerenciadorDeImagens
from gerenciador_de_som import GerenciadorDeSom

class Jogo:
    def __init__(self):
        pygame.init()
        self.largura = 600
        self.altura = 400
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Jogo da Cobrinha")
        self.relogio = pygame.time.Clock()
        self.pontos = 0
        self.morreu = False
        self.fonte = pygame.font.SysFont('arial', 40, True, True)
        self.cobra = Cobra(self.largura, self.altura)
        self.gerenciador_imagens = GerenciadorDeImagens()
        self.comida = Comida(self.largura, self.altura, self.gerenciador_imagens)
        self.sons = GerenciadorDeSom()
        self.velocidade_incremento = 1

    def executar(self):
        while True:
            self.relogio.tick(10)
            self.tela.fill((0, 255, 80))
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
        if evento.key == K_LEFT:
            if self.cobra.x_controle != self.cobra.velocidade:
                self.cobra.x_controle = -self.cobra.velocidade
                self.cobra.y_controle = 0
        if evento.key == K_RIGHT:
            if self.cobra.x_controle != -self.cobra.velocidade:
                self.cobra.x_controle = self.cobra.velocidade
                self.cobra.y_controle = 0
        if evento.key == K_UP:
            if self.cobra.y_controle != self.cobra.velocidade:
                self.cobra.x_controle = 0
                self.cobra.y_controle = -self.cobra.velocidade
        if evento.key == K_DOWN:
            if self.cobra.y_controle != -self.cobra.velocidade:
                self.cobra.x_controle = 0
                self.cobra.y_controle = self.cobra.velocidade
        if evento.key == K_SPACE and self.morreu:
            self.reiniciar_jogo()

    def atualizar_jogo(self):
        self.cobra.mover()
        if self.cobra.checar_colisao(self.comida):
            self.comida.reposicionar(self.largura, self.altura)
            self.cobra.comprimento_inicial += 2
            self.pontos += 1
            self.sons.tocar_som_colisao()
            if self.pontos % 10 == 0:
                self.cobra.aumentar_velocidade(self.velocidade_incremento)
        self.cobra.atualizar()
        self.checar_posicoes()

    def checar_posicoes(self):
        if self.cobra.lista_cobra.count([self.cobra.x_cobra, self.cobra.y_cobra]) > 1:
            self.morreu = True
        if self.cobra.x_cobra > self.largura:
            self.cobra.x_cobra = 0
        if self.cobra.x_cobra < 0:
            self.cobra.x_cobra = self.largura
        if self.cobra.y_cobra > self.altura:
            self.cobra.y_cobra = 0
        if self.cobra.y_cobra < 0:
            self.cobra.y_cobra = self.altura

    def desenhar_elementos(self):
        self.gerenciador_imagens.desenhar_fundo(self.tela)
        mensagem = f'Pontuação: {self.pontos}'
        self.fonte = pygame.font.Font(None, 25)
        texto_formatado = self.fonte.render(mensagem, True, (0, 0, 0))
        self.tela.blit(texto_formatado, (470, 10))
        self.cobra.aumenta_cobra(self.tela)
        self.comida.desenhar(self.tela)
        if self.morreu:
            self.game_over()

    def game_over(self):
        font2 = pygame.font.SysFont("arial", 20, True, True)
        mensagem = "Game Over! Pressione a tecla espaço para reiniciar."
        texto_formatado = font2.render(mensagem, True, (0, 0, 0))
        ret_texto = texto_formatado.get_rect()
        ret_texto.center = (self.largura // 2, self.altura // 2)
        self.tela.blit(texto_formatado, ret_texto)
        pygame.display.update()
        self.sons.parar_musica()
        self.sons.tocar_game_over()
        while self.morreu:
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
                if evento.type == KEYDOWN:
                    if evento.key == K_SPACE:
                        self.reiniciar_jogo()

    def reiniciar_jogo(self):
        self.pontos = 0
        self.cobra.reiniciar(self.largura, self.altura)
        self.comida.reposicionar(self.largura, self.altura)
        self.morreu = False
        self.sons.parar_game_over()
        self.sons.tocar_musica()

jogo = Jogo()

jogo.executar()

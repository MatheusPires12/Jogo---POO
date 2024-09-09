import pygame
from pygame.locals import *
from sys import exit
from random import randint
from cobra import Cobra
from comida import Comida, ComidaDourada, ComidaPrata, ComidaPodre
from gerenciador_de_imagem import NivelFacil, NivelMedio, NivelDificil, GerenciadorDeImagens
from gerenciador_de_som import GerenciadorDeSom
import time

class Jogo:
    def __init__(self, nivel):
        pygame.init()
        self.largura = 640
        self.altura = 480
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Jogo da Cobrinha")
        self.relogio = pygame.time.Clock()
        self.pontos = 0
        self.morreu = False
        self.fonte = pygame.font.SysFont('arial', 40, True, True)

        self.gerenciador_imagens = nivel
        self.cobra = Cobra(self.largura, self.altura, self.gerenciador_imagens.cabeca, self.gerenciador_imagens.corpo, self.gerenciador_imagens.rabo)
        self.sons = GerenciadorDeSom()
        self.velocidade_incremento = 1

        self.controles_invertidos = False  # Flag para os controles invertidos
        self.tempo_inverter_controles = 0  # Variável para controlar o tempo de duração do efeito

        lista_obstaculos = []
        if isinstance(self.gerenciador_imagens, (NivelMedio, NivelDificil)):
            lista_obstaculos = self.gerenciador_imagens.criar_rect_obstaculo()
        
        self.comida = self.criar_comida()
        self.comida.reposicionar(self.cobra.lista_cobra, lista_obstaculos)
        
    def criar_comida(self):
        opcao = randint(1, 6)  
        if opcao == 1:
            return ComidaDourada(self.largura, self.altura, self.gerenciador_imagens)
        elif opcao == 2:
            return ComidaPrata(self.largura, self.altura, self.gerenciador_imagens)
        elif opcao == 3:
            return ComidaPodre(self.largura, self.altura, self.gerenciador_imagens)
        else:
            return Comida(self.largura, self.altura, self.gerenciador_imagens)

    def executar(self):
        while True:
            self.relogio.tick(10)
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
        if self.controles_invertidos:
            # Inverte as teclas enquanto o poder está ativo
            if evento.key == K_LEFT:
                if self.cobra.x_controle != -self.cobra.velocidade:
                    self.cobra.x_controle = self.cobra.velocidade
                    self.cobra.y_controle = 0
            if evento.key == K_RIGHT:
                if self.cobra.x_controle != self.cobra.velocidade:
                    self.cobra.x_controle = -self.cobra.velocidade
                    self.cobra.y_controle = 0
            if evento.key == K_UP:
                if self.cobra.y_controle != -self.cobra.velocidade:
                    self.cobra.x_controle = 0
                    self.cobra.y_controle = self.cobra.velocidade
            if evento.key == K_DOWN:
                if self.cobra.y_controle != self.cobra.velocidade:
                    self.cobra.x_controle = 0
                    self.cobra.y_controle = -self.cobra.velocidade
        else:
            # Controles normais
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

    def atualizar_jogo(self):
        self.cobra.mover()
        if self.cobra.checar_colisao(self.comida):
            lista_obstaculos = []
            if isinstance(self.gerenciador_imagens, (NivelMedio, NivelDificil)):
                lista_obstaculos = self.gerenciador_imagens.criar_rect_obstaculo()
            if isinstance(self.comida, ComidaPrata):
                self.pontos = self.comida.poder_prata(self.pontos)
            if isinstance(self.comida, ComidaPodre):
                self.comida.poder_podre(self)

            # Reposiciona a comida e aumenta o tamanho da cobra
            self.comida = self.criar_comida()
            self.comida.reposicionar(self.cobra.lista_cobra, lista_obstaculos)
            self.cobra.comprimento_inicial += 2
            self.pontos += 1  # Incrementa pontos após consumir qualquer comida
            self.sons.tocar_som_colisao()
            
            # Aumenta a velocidade a cada 10 pontos
            if self.pontos % 10 == 0:
                self.cobra.aumentar_velocidade(self.velocidade_incremento)

        self.cobra.atualizar()
        self.checar_posicoes()
        
        if self.controles_invertidos and time.time() - self.tempo_inverter_controles >= 5:
            self.controles_invertidos = False

    def checar_posicoes(self):
        # Verificação de colisão com as bordas da tela
        limites = [
            self.cobra.x_cobra > self.largura - 50,
            self.cobra.x_cobra < 20,
            self.cobra.y_cobra > self.altura - 50,
            self.cobra.y_cobra < 20
        ]

        # Verificação de colisão com o próprio corpo
        if self.cobra.lista_cobra.count([self.cobra.x_cobra, self.cobra.y_cobra]) > 1 or any(limites):
            self.morreu = True

        # Verificação de colisão com obstáculos
        if isinstance(self.gerenciador_imagens, (NivelMedio, NivelDificil)):
            obstaculos = self.gerenciador_imagens.criar_rect_obstaculo()
            cabeca_cobra_rect = pygame.Rect(self.cobra.x_cobra, self.cobra.y_cobra, 20, 20)  # Retângulo da cabeça da cobra
            
            for obstaculo in obstaculos:
                if cabeca_cobra_rect.colliderect(obstaculo):
                    self.morreu = True
                    break

    def desenhar_elementos(self):
        self.gerenciador_imagens.desenhar_fundo(self.tela)
        mensagem = f'Pontuação: {self.pontos}'
        self.fonte = pygame.font.Font(None, 25)
        texto_formatado = self.fonte.render(mensagem, True, (255, 255, 255))
        self.tela.blit(texto_formatado, (510, 1))
        self.cobra.aumenta_cobra(self.tela)
        self.comida.desenhar(self.tela)

        # Desenha os obstáculos, se existirem no nível
        if isinstance(self.gerenciador_imagens, NivelMedio) or isinstance(self.gerenciador_imagens, NivelDificil):
            self.gerenciador_imagens.desenhar_obstaculos(self.tela)
            
        if self.morreu:
            self.game_over()

    def game_over(self):
        gerenciador_imagens = GerenciadorDeImagens()  # Pode ser qualquer um dos níveis, pois o fundo é o mesmo
        gerenciador_imagens.desenhar_fim(self.tela)
        pygame.display.update()

        self.sons.parar_musica()
        self.sons.tocar_game_over()
        while self.morreu:
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
                if evento.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # Verifica se o clique foi na imagem de fácil
                    if 58 <= x <= 58 + gerenciador_imagens.reiniciar.get_width() and 350 <= y <= 350 + gerenciador_imagens.reiniciar.get_height():
                        return self.reiniciar_jogo()
                    # Verifica se o clique foi na imagem de médio
                    elif 370 <= x <= 370 + gerenciador_imagens.sair.get_width() and 350 <= y <= 350 + gerenciador_imagens.sair.get_height():
                        return exit()
                    
    def reiniciar_jogo(self):
        self.gerenciador_imagens = mostrar_tela_selecao_nivel(self.tela) 
        self.pontos = 0
        self.cobra.reiniciar(self.largura, self.altura, self.gerenciador_imagens.cabeca, self.gerenciador_imagens.corpo, self.gerenciador_imagens.rabo)
        
        # Garante que a comida é reposicionada corretamente com os obstáculos
        lista_obstaculos = []
        if isinstance(self.gerenciador_imagens, (NivelMedio, NivelDificil)):
            lista_obstaculos = self.gerenciador_imagens.criar_rect_obstaculo()
        
        self.comida = Comida(self.largura, self.altura, self.gerenciador_imagens)
        self.comida.reposicionar(self.cobra.lista_cobra, lista_obstaculos)
        
        self.morreu = False
        self.sons.parar_game_over()
        self.sons.tocar_musica()

        # Desativa o poder após 8 segundos
        if self.controles_invertidos and time.time() - self.tempo_inverter_controles >= 5:
            self.controles_invertidos = False

def mostrar_tela_selecao_nivel(tela):
    gerenciador_imagens = NivelFacil()  # Pode ser qualquer um dos níveis, pois o fundo é o mesmo
    gerenciador_imagens.desenhar_inicial(tela)
    pygame.display.update()

    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
            if evento.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Verifica se o clique foi na imagem de fácil
                if 37 <= x <= 37 + gerenciador_imagens.facil.get_width() and 373 <= y <= 373 + gerenciador_imagens.facil.get_height():
                    return NivelFacil()
                # Verifica se o clique foi na imagem de médio
                elif 230.72 <= x <= 230.72 + gerenciador_imagens.medio.get_width() and 373 <= y <= 373 + gerenciador_imagens.medio.get_height():
                    return NivelMedio()
                # Verifica se o clique foi na imagem de difícil
                elif 424.44 <= x <= 424.44 + gerenciador_imagens.dificil.get_width() and 373 <= y <= 373 + gerenciador_imagens.dificil.get_height():
                    return NivelDificil()

if __name__ == "__main__":
    pygame.init()
    largura = 640
    altura = 480
    tela = pygame.display.set_mode((largura, altura))

    # Exibe a tela de seleção de nível
    nivel_selecionado = mostrar_tela_selecao_nivel(tela)

    # Inicia o jogo com o nível selecionado
    jogo = Jogo(nivel_selecionado)
    jogo.executar()

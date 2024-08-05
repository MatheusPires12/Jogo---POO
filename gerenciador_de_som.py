import pygame
import os

class GerenciadorDeSom:
    def __init__(self):
        pygame.mixer.music.set_volume(1)
        musica_fundo = os.path.join("Musicas", "Game_Music.mp3")
        pygame.mixer.music.load(musica_fundo)
        pygame.mixer.music.play(-1)
        som_colisao = os.path.join("Musicas", "som_colisao.wav")
        self.som_colisao = pygame.mixer.Sound(som_colisao)
        self.som_colisao.set_volume(1)
        som_game_over = os.path.join("Musicas", "Game_Over.wav")
        self.som_game_over = pygame.mixer.Sound(som_game_over)
        self.som_game_over.set_volume(1)

    def tocar_som_colisao(self):
        self.som_colisao.play()

    def parar_musica(self):
        pygame.mixer.music.stop()

    def tocar_game_over(self):
        self.som_game_over.play()

    def parar_game_over(self):
        self.som_game_over.stop()

    def tocar_musica(self):
        pygame.mixer.music.play(-1)
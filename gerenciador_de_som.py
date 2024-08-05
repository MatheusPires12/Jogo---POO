import pygame

class GerenciadorDeSom:
    def __init__(self):
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.load("/Musicas/musica_fundo.mp3")
        pygame.mixer.music.play(-1)
        self.som_colisao = pygame.mixer.Sound("/Musicas/som_colisao.wav")
        self.som_colisao.set_volume(0.1)
        self.som_game_over = pygame.mixer.Sound("/Musicas/Game_Over.wav")
        self.som_game_over.set_volume(0.1)

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

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
# Clase para representar un solo alien de la flota
    def __init__(self, ai_game):
        # Inicializa al alien y establece su posicion inicial
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting

        # Carga la imagen del Alien y configura su atributo rect
        self.imagen = pygame.image.load("images/alien.png")
        self.imagen_redimention = pygame.transform.scale(self.imagen, (ai_game.setting.img_width, ai_game.setting.img_height))
        self.image = self.imagen_redimention
        self.rect = self.imagen_redimention.get_rect()

        # Inicia el nuevo alien cerca de la parte superior izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # guarda la posicion horizontal exacta del alien
        self.x = float(self.rect.x)
    def check_edges(self):
        # decuelve true si el alien esta en el borde de la pantalla
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0
    def update(self):
        # Mueve el alien a la derecha
        self.x += self.setting.alien_speed * self.setting.fleet_direction
        self.rect.x = self.x
    
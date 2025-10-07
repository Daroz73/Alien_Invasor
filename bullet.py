import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
# Clase para gestionar las balas disparadas desde la nave
    def __init__(self, ai_game):
        # Crea un objeto para la bala en la posicion actual de la nave
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color
        # Crea un rectangulo para la bala y luego establece la posicion correcta
        self.rect = pygame.Rect(0,0,self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        # Guarda la posicion correcta
        self.y = float(self.rect.y)
    
    def update(self):
    # Mueve la bala hacia arriba en la pantalla
        # Actualiza la posicion exacta de la bala
        self.y -= self.setting.bullet_speed
        # Actualiza la poscicion del rectangulo
        self.rect.y = float(self.y)
    
    def draw_bullet(self):
    # Dibuja la bala en la pantalla
        pygame.draw.rect(self.screen, self.color, self.rect)
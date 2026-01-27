import pygame

class Ship:
# Una clase para gestionar la nave
    def __init__(self, ai_game):
    # Inicializa la nave y configura su posicion inicial
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.screen_rect = ai_game.screen.get_rect()
        # Carga la imagen de la nave y almacena su rect
        self.image = pygame.image.load('images/ship.png')
        self.img_redimention = pygame.transform.scale(self.image,(self.setting.img_width,self.setting.img_height))
        # self.rect = self.image.get_rect()
        self.rect = self.img_redimention.get_rect()
        # Coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom
        # Guardamos un valor decimal para conocer la poscicion exacta de la nave
        self.x = float(self.rect.x)
        # Bandera de movimiento, comienza en false xq no se ha pulsado nada
        self.moving_right = False
        self.moving_left = False
    def update(self):
    # Actualiza la posicion de la nave en funcion de la bandera de movimiento
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Actualiza el valor de la nave no el del rect
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        # Actualiza el objeto rect de self.x
        self.rect.x = self.x
    def blitme(self):
    # Dibuja la nave en la ubicacion actual
        self.screen.blit(self.img_redimention, self.rect)
    def center_ship(self):
        # centra la nave en la pantalla
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
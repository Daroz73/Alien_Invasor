import sys
import pygame
from setting import Setting
from ship import Ship

class Alien_Invasor:
    # Clase general para gestionar los recursos y el comportamiento del juego

    def __init__(self):
        # Inicializa el juego y crea los recursos
        pygame.init()
        self.clock = pygame.time.Clock()
        self.setting = Setting()

        # Lineas para abrir el juego en pantalla completa 
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.setting.screen_width = self.screen.get_rect().width
        # self.setting.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        pygame.display.set_caption("Alien Invasor")
        self.ship = Ship(self)

    
    def run_game(self):
        # Inicializa el bucle principal para el juego
        while(True):
            # Busca eventos de teclado y raton
            self._check_event()

            self.ship.update()

            # Redibuja la pantalla en cada vuelta de bucle
            self._update_screen()

            self.clock.tick(60)
    
    def _check_event(self):
    # Responde a pulsaciones de teclas y eventos de raton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
    # Actializa imagenes en la pantalla y cambia a la pantalla nueva
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        # Hace visible la ultima pantalla dibujada
        pygame.display.flip()

    def _check_keydown_event(self, event):
    # Responde a pulsaciones de teclas
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
    # Responde a liberaciones de teclas
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta
    ai = Alien_Invasor()
    ai.run_game()
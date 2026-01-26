import sys
import pygame
from setting import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien

class Alien_Invasor:
    # Clase general para gestionar los recursos y el comportamiento del juego

    def __init__(self):
        # Inicializa el juego y crea los recursos
        pygame.init()
        self.clock = pygame.time.Clock()
        self.setting:Setting = Setting()

        # Lineas para abrir el juego en pantalla completa 
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.setting.screen_width = self.screen.get_rect().width
        # self.setting.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        pygame.display.set_caption("Alien Invasor")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    
    def run_game(self):
        # Inicializa el bucle principal para el juego
        while True:
            # Busca eventos de teclado y raton
            self._check_event()
            self.ship.update()
            self._update_bullet()
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
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
    # Responde a liberaciones de teclas
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
    # Crea un nueva bala y la agrega al grupo de balas
        if len(self.bullets) < self.setting.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullet(self):
    # Actualiza la posicion de las balas y se deshace de las viejas
        # Actualiza las posiciones de las balas 
        self.bullets.update()
        # Se deshace de las balas viejas
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    def _create_fleet(self):
    # Crea una flota de Aliens
        alien = Alien(self)
        self.aliens.add(alien)

if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta
    ai = Alien_Invasor()
    ai.run_game()
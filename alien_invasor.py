import sys
from time import sleep

import pygame

from setting import Setting
from game_stats import Game_Stats
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
        # Crea una instancia para guardar las estadisticas del juego
        self.stats = Game_Stats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        
        # Inicializa alien Invasor en Activo
        self.game_active = True

    
    def run_game(self):
        # Inicializa el bucle principal para el juego
        while True:
            # Busca eventos de teclado y raton
            self._check_event()
            if self.game_active:
                self.ship.update()
                self._update_bullet()
                # Redibuja la pantalla en cada vuelta de bucle
                self._update_aliens()
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
        self._check_bullet_alien_collisions()
    def _check_bullet_alien_collisions(self):
        # Busca balas que hayan dado a aliens
        # si hay se deshace de la bala y del alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # destruye todas las balas existentes y crea una flota nueva
            self.bullets.empty()
            self._create_fleet()
    def _create_alien(self, x_position, y_position):
        # Crea un nuevo alien y lo agrega a la flota
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    def _check_fleet_edges(self):
        # responde adecuadamente si algun alien ha llegado al borde
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        # baja toda la flota y cambia su direccion
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1
    def _create_fleet(self):
    # Crea una flota de Aliens
    # Crea un alien y va agregando hasta que no queda estapacio
    # La distancia entre aliens es equivalente a la de un alien ancho y otro de alto
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < self.setting.screen_height - 3 * alien_height:
            while current_x < self.setting.screen_width - 2 * alien_width:
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # con la fila terminada se resetea el valor de x y se actualiza el de y
            current_x = alien_width
            current_y += alien_height
    def _update_aliens(self):
        # Actualiza la posicion de todos los aliens de la flota
        self._check_fleet_edges()
        self.aliens.update()
        # Busca coliciones alien-nave
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # Busca aliens que han llegado al fondo de la pantalla
        self._check_aliens_bottom()
    def _ship_hit(self):
        # Responde al impacto de un alien en la nave
        # Disminuye el ship left
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            # se deshace de los aliens y balas restantes
            self.aliens.empty()
            self.bullets.empty()
            # Crea una flota nueva y centra la nave
            self._create_fleet()
            self.ship.center_ship()
            # Pausa
            sleep(0.5)
        else:
            self.game_active = False
    def _check_aliens_bottom(self):
        # Comprueba si algun alien ha llegado al fondo de la pantalla
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.setting.screen_height:
                # trata esto como si la nave hubiese sido alcanzada
                self._ship_hit()
                break
if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta
    ai = Alien_Invasor()
    ai.run_game()
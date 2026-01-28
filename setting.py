class Setting:
# Una calse que guarda toda la configuracion de Alien Invasor
    def __init__(self):
    # Inicia las configuraciones del juego
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Configuracion de la nave
        self.ship_limit = 3
        self.img_height = 100
        self.img_width = 75
        # Configuracion de la bala
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Configuracion de los aliens
        self.fleet_drop_speed = 10
        # Rapidez con la que se acelera el juego
        self.speed_up_scale = 1.3
        # Rapidez con la que aumenta el valor de los aliens
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        #Inicializa las configuraciones que cambian durante el juego
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        self.alien_points = 50
        # fleet_direction = 1(derecha) / -1 (izquierda)
        self.fleet_direction = 1
    def increase_speed(self):
        # Incremente la configuracion de velocidad
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale
        self.alien_points = int(self.alien_points * self.score_scale)
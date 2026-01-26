class Setting:
# Una calse que guarda toda la configuracion de Alien Invasor
    def __init__(self):
    # Inicia las configuraciones del juego
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Configuracion de la nave
        self.ship_speed = 1.5
        self.img_height = 100
        self.img_width = 75
        # Configuracion de la bala
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Configuracion de los aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1(derecha) / -1 (izquierda)
        self.fleet_direction = 1
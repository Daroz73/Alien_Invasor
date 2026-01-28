import pygame.font

class Scoreboard:
    def __init__(self, ai_game):
        # Inicializa los atributos de la puntuacion
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = ai_game.setting
        self.stats = ai_game.stats
        # Configuracion de la fuente para la informacion de la puntuacion
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        # Prepara la imagen de la puntuacion inicial
        self.prep_score()
    def prep_score(self):
        # Convierte al puntuacion en una imagen renderizada
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_img = self.font.render(score_str, True, self.text_color, self.setting.bg_color)
        # Muestra la informacion en la parte superior derecha de la pantalla
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    def show_score(self):
        # Dibuja la puntuacion de la pantalla
        self.screen.blit(self.score_img, self.score_rect)
class Game_Stats:
    # Sigue las estadisticas de alien invasor
    def __init__(self, ai_game):
        # Inicializa las estadisticas
        self.setting = ai_game.setting
        self.reset_stats()
    def reset_stats(self):
        # Inicializa las estadisticas que pueden cambiar durante el juego
        self.ships_left = self.setting.ship_limit
        self.score = 0
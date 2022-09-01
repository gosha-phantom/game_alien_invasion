

class GameStats():
    """отслеживание статистики для игры"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        
        with open('./record.txt', 'r') as f:
            record = int(f.readline())
        self.high_score = record
        
        
    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

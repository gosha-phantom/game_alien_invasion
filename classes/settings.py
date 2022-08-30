class Settings():
    """класс для хранения всех настроек игры"""
    def __init__(self):
        # инициализируем настройки иргы
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # настройки корабля
        self.ship_speed_factor = 1.5

        # параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60) 
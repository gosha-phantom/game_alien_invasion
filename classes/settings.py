class Settings():
    """класс для хранения всех настроек игры"""
    def __init__(self):
        # инициализируем настройки иргы
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        

        # параметры пули
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60) 
        # ограничение количества пуль на экране
        self.bullets_allowed = 5

        # параметры звезды
        self.star_quantity = 15

        # параметры пришельцев
        self.alien_speed_factor = 1
        # скорость снижения флота вниз
        self.fleet_drop_speed = 10
        

        # настройки игры и статистика
        self.ship_limit = 0

        # темп ускорения игры
        self.speedup_scale = 1.1
        self.initialize_dynamyc_settings()

    def initialize_dynamyc_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        # настройки корабля
        self.ship_speed_factor = 1.5
        # параметры пули
        self.bullet_speed_factor = 2
        # параметры пришельцев
        self.alien_speed_factor = 1
        # fleet_direction = 1 движение вправо; -1 движение влево
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *=self.speedup_scale
        self.bullet_speed_factor *=self.speedup_scale
        self.alien_speed_factor *=self.speedup_scale


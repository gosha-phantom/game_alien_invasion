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
        # ограничение количества пуль на экране
        self.bullets_allowed = 10

        # параметры звезды
        self.star_quantity = 15

        # параметры пришельцев
        self.alien_speed_factor = 1
        # скорость снижения флота вниз
        self.fleet_drop_speed = 10
        # fleet_direction = 1 движение вправо; -1 движение влево
        self.fleet_direction = 1 
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        # инициализируем корабль и задаем ему начальное положение
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # загружаем изображение корабля и получаем прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = (self.screen_rect.bottom)*0.98
        # сохраняем вещественную координату центра корабля 
        self.center = float(self.rect.centerx)
        
        # флаг перемещения корабля направо
        self.moving_right = False
        # флаг перемещения корабля налево
        self.moving_left = False


    # обновляет позицию корабля с учетом флага
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
        # обновляем атрабут rect на основании self.center
        self.rect.centerx = self.center

    # рисуем корабль в текущей позиции
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
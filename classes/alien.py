import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс представляющий одного пришельца"""
    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает его начальную позицию"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # загрузка изображения пришельца
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # каждый новый пришелец появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной позиции пришельца
        self.x = float(self.rect.x)

    def blitme(self):
        """Выводит пришельца в текущем положении"""
        self.screen.blit(self.image, self.rect)

import pygame
from classes.settings import Settings
from classes.ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # инициализируем игру
    pygame.init()
    ai_settings = Settings()
    # создаем игровой экран приложения
    screen = pygame.display.set_mode((ai_settings.screen_width, 
                                    ai_settings.screen_height))
    # название основного окна приложения
    pygame.display.set_caption('Нашествие пришельцев')

    # создаем основной корабль
    ship = Ship(ai_settings, screen)

    # создаем группы для хранения пуль
    bullets = Group()

    # запуск основного цикла игры
    while True:
        # отслеживаем события нажатия кнопок клавы и мыши
        # gf.check_events(ship)
        gf.check_events(ai_settings, screen, ship, bullets)

        # обновляем местоположение основного корабля
        ship.update()

        # обновляем расположение группы пуль
        bullets.update()

        # удаляем из памяти улетевшие за пределы окна пули
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            # проверка на удаление вылетевших пуль из памяти
            # print(len(bullets))
            
        # обновляем экран
        gf.update_screen(ai_settings, screen, ship, bullets)

# запускаем игру
run_game()
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

    # создание флота пришельцев
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # запуск основного цикла игры
    while True:
        # отслеживаем события нажатия кнопок клавы и мыши
        # gf.check_events(ship)
        gf.check_events(ai_settings, screen, ship, bullets)

        # обновляем местоположение основного корабля
        ship.update()

        # обновляем местоположение пуль
        gf.update_bullets(bullets)
            
        # обновляем экран
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

# запускаем игру
run_game()
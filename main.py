import pygame
from classes.settings import Settings
from classes.ship import Ship
from classes.star import Star
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

    # создаем одну звезду
    # star = Star(ai_settings, screen)

    # создаем звездное небо
    stars = Group()
    gf.create_star_sky(ai_settings, screen, stars)
    
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

        # обновляет местоположение пришельцев
        gf.update_aliens(ai_settings, aliens)

        # обновляем экран и прорисовываем объекты
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stars)

        # обновляем местоположение пуль
        gf.update_bullets(bullets)

# запускаем игру
run_game()
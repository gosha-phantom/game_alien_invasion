import pygame
from classes.settings import Settings
from classes.ship import Ship
# from classes.star import Star
from classes.game_stats import GameStats
from classes.button import Button
from classes.scoreboard import Scoreboard
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

    # создание кнопки Play
    play_button = Button(ai_settings, screen, 'Play')

    # создаем одну звезду
    # star = Star(ai_settings, screen)
    
    # создаем основной корабль
    ship = Ship(ai_settings, screen)

    # создаем группы для хранения пуль
    bullets = Group()

    # создание флота пришельцев
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # Создание экземпляров для хранения игровой статистики
    stats = GameStats(ai_settings)
    scoreboard = Scoreboard(ai_settings, screen, stats)

    # создаем звездное небо
    stars = Group()
    gf.create_star_sky(ai_settings, screen, stars)

    # запуск основного цикла игры
    while True:
        # отслеживаем события нажатия кнопок клавы и мыши
        gf.check_events(ai_settings, screen, stats, ship, bullets, 
                            aliens, play_button, scoreboard)

        if stats.game_active:
            # обновляем местоположение основного корабля
            ship.update()

            # обновляет местоположение пришельцев
            gf.update_aliens(ai_settings, screen, stats, ship, bullets, 
                                aliens, scoreboard)

            # обновляем местоположение пуль
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship, 
                                stats, scoreboard)

        # обновляем экран и прорисовываем объекты
        gf.update_screen(ai_settings, screen, stats, ship, bullets, aliens, 
                                stars, play_button, scoreboard)


# запускаем игру
run_game()
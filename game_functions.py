import sys
import pygame
from classes.bullet import Bullet


# Реагируем на нажатие клавиш
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагируем на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


# Реагируем на отпускание клавиш
def check_keyup_events(event, ship):
    """Реагируем на отпускание клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False 


# Обрабатываем нажатия кнопок клавы и мыши
def check_events(ai_settings, screen, ship, bullets):
    """Обрабатываем нажатия кнопок клавы и мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


# функция обновления экрана
def update_screen(ai_settings, screen, ship, bullets):
    """Обновление изображения на экране и отображение нового экрана"""
    # присваиваем цвет фона экрану
    screen.fill(ai_settings.bg_color)

    # все пули выводятся позади изображений корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # прорисовываем основной корабль
    ship.blitme()
        
    # отображение последнего прорисованного экрана
    pygame.display.flip()
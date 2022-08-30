import sys
from turtle import width
import pygame
from classes.bullet import Bullet
from classes.alien import Alien


# получаем количество пришельцев в горизонтальном ряду
def get_number_aliens_x(ai_settings, alien_width):
    # определяем доступное пространство для прорисовки флота пришельцев по горизонтали
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    # определяем количество пришельцев в одном ряду
    number_aliens_x = int(available_space_x / (2 * alien_width))
    # возвращаем результат
    return number_aliens_x

# прорисовываем одного пришельца
def create_alien(ai_settings, screen, aliens, alien_number):
    # Создание пришельца и размещение его в ряду
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.rect.x = alien.x
    aliens.add(alien)

# Создает флот пришельцев
def create_fleet(ai_settings, screen, aliens):
    """Создает флот пришельцев"""
    # создание пришельца
    alien = Alien(ai_settings, screen)
    # определяем в переменную значение ширины одного пришельца
    alien_width = alien.rect.width
    # получаем количество пришельцев в горизонтальном ряду
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)

    # Создание первого ряда пришельцев
    for alien_number in range(number_aliens_x):
        # Создание пришельца и размещение его в ряду
        create_alien(ai_settings, screen, aliens, alien_number)


# функция стрельбы
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


# Реагируем на нажатие клавиш
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагируем на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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
def update_screen(ai_settings, screen, ship, bullets, aliens):
    """Обновление изображения на экране и отображение нового экрана"""
    # присваиваем цвет фона экрану
    screen.fill(ai_settings.bg_color)

    # все пули выводятся позади изображений корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # прорисовываем основной корабль
    ship.blitme()
        
    # прорисовываем пришельца
    # alien.blitme()

    # прорисовываем флот пришельцев
    aliens.draw(screen)
    
    # отображение последнего прорисованного экрана
    pygame.display.flip()


#
def update_bullets(bullets):
    """обновляет позиции пуль и уничтожает старые пули"""
    # обновляем расположение группы пуль
    bullets.update()

    # удаляем из памяти улетевшие за пределы окна пули
    for bullet in bullets.copy():  
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # проверка на удаление вылетевших пуль из памяти
        # print(len(bullets))
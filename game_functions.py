import sys
from turtle import width
import pygame
from classes.bullet import Bullet
from classes.alien import Alien
from classes.star import Star
from random import randint
from time import sleep


# создаем одну звезду
def create_one_star(ai_settings, screen, stars):
    star = Star(ai_settings, screen)
    star.x = randint(0, ai_settings.screen_width)
    star.rect.x = star.x
    star.y = randint(0, ai_settings.screen_height)
    star.rect.y = star.y

    stars.add(star)

# создаем звездное небо
def create_star_sky(ai_settings, screen, stars):
    # создание объекта звезды
    # star = Star(ai_settings, screen)
    # рисуем в цикле звезды
    for i in range(ai_settings.star_quantity):
        create_one_star(ai_settings, screen, stars)


# получаем количество пришельцев в горизонтальном ряду
def get_number_aliens_x(ai_settings, alien_width):
    # определяем доступное пространство для прорисовки флота пришельцев по горизонтали
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    # определяем количество пришельцев в одном ряду
    number_aliens_x = int(available_space_x / (2 * alien_width))
    # возвращаем результат
    return number_aliens_x

# получаем количество пришельцев в вертикальном ряду
def get_number_rows(ai_settings, alien_height, ship_height):
    # определяем доступное пространство для прорисовки флота пришельцев по вертикали
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    # определяем количество пришельцев в одном столбце
    number_rows = int(available_space_y / (2 * alien_height))
    # возвращаем результат
    return number_rows

# прорисовываем одного пришельца
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Создание пришельца и размещение его в ряду
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
    aliens.add(alien)

# Создает флот пришельцев
def create_fleet(ai_settings, screen, aliens, ship):
    """Создает флот пришельцев"""
    # создание первого пришельца
    alien = Alien(ai_settings, screen)
    # определяем в переменную значение ширины одного пришельца
    # alien_width = alien.rect.width
    # получаем количество пришельцев в горизонтальном ряду
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    # получаем количество пришельцев в вертикальном ряду
    number_rows = get_number_rows(ai_settings, alien.rect.height, 
                                ship.rect.height)

    # Создание флота пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Создание пришельца и размещение его в ряду
            create_alien(ai_settings, screen, aliens, alien_number, 
                        row_number)


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
def update_screen(ai_settings, screen, ship, bullets, aliens, stars):
    """Обновление изображения на экране и отображение нового экрана"""
    # присваиваем цвет фона экрану
    screen.fill(ai_settings.bg_color)

    # прорисовываем звездное небо
    stars.draw(screen)
    
    # все пули выводятся позади изображений корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # прорисовываем основной корабль
    ship.blitme()

    # прорисовываем одну звезду
    # star.blitme()

    # прорисовываем пришельца
    # alien.blitme()

    # прорисовываем флот пришельцев
    aliens.draw(screen)
    
    # отображение последнего прорисованного экрана
    pygame.display.flip()


def check_bullet_alien_collission(ai_settings, screen, ship, bullets, aliens):
    """Обработка коллизии между пулями и пришельцами и уничтожаем пришельцев"""
    # Проверка попаданий в пришельцев
    # При обнаружении попадания удалить пулю и пришельца
    colissions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # проверяем уничтожение флота захватчиков и создаем новый
    if len(aliens) == 0:
        create_fleet(ai_settings, screen, aliens, ship)
        # пауза
        sleep(1)


# Обновляет позиции пуль и уничтожает старые пули
def update_bullets(bullets, aliens, ai_settings, screen, ship):
    """Обновляет позиции пуль и уничтожает старые пули."""
    # обновляем расположение группы пуль
    bullets.update()

    # удаляем из памяти улетевшие за пределы окна пули
    for bullet in bullets.copy():  
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # проверка на удаление вылетевших пуль из памяти
        # print(len(bullets))

    # Обработка коллизии между пулями и пришельцами и уничтожаем пришельцев
    check_bullet_alien_collission(ai_settings, screen, ship, bullets, aliens)




def check_fleet_edges(ai_settings, aliens):
    """Реагирует на достижение пришельцем края платформы."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Опускает весь флот и меняет его направление."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_alien_bottom(ai_settings, screen, stats, ship, bullets, aliens):
    """Проверяет, добрались ли пришельцы до нижнего края экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Происходит то же, что и при столкновении с кораблем
            ship_hit(ai_settings, screen, stats, ship, bullets, aliens)
            break


def update_aliens(ai_settings, screen, stats, ship, bullets, aliens):
    """
        Проверяет, достиг ли флот края экрана,
            после чего обновляет позиции всех пришельцев во флоте.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Проверка коллизий между пришельцами и основным кораблем
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, ship, bullets, aliens)

    # Проверка пришельцев, добравшихся до нижнего края
    check_alien_bottom(ai_settings, screen, stats, ship, bullets, aliens)


def ship_hit(ai_settings, screen, stats, ship, bullets, aliens):
    """Обрабатывает столкновение корабля с пришельцами"""
    if stats.ships_left > 0:
        # уменьшаем количество оставшихся попыток
        stats.ships_left -= 1
        
        # очистка списков пришельцев и пуль
        aliens.empty()
        bullets.empty()

        # создание нового флота и размещение корабля в центре
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        # пауза
        sleep(1)
    else:
        stats.game_active = False



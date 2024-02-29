import pygame

# Инициализация PyGame
pygame.init()

# Настройка экрана
экран = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Графическая игра")

# Настройка игрока
игрок = pygame.Rect(0, 550, 20, 20)
скорость_игрока = 5

# Настройка цели
цель = pygame.Rect(300, 50, 20, 20)

# Основной цикл игры
работает = True
while работает:

    # Обработка событий
    for событие in pygame.event.get():
        if событие.type == pygame.QUIT:
            работает = False

        # Обработка нажатия клавиш
        if событие.type == pygame.KEYDOWN:
            if событие.key == pygame.K_UP:
                игрок.y -= скорость_игрока
            elif событие.key == pygame.K_DOWN:
                игрок.y += скорость_игрока
            elif событие.key == pygame.K_LEFT:
                игрок.x -= скорость_игрока
            elif событие.key == pygame.K_RIGHT:
                игрок.x += скорость_игрока

    # Проверка столкновения с целью
    if игрок.colliderect(цель):
        цель.x = random.randint(0, 580)
        цель.y = random.randint(0, 580)

    # Отрисовка экрана
    экран.fill((0, 0, 0))
    pygame.draw.rect(экран, (255, 255, 255), игрок)
    pygame.draw.rect(экран, (255, 0, 0), цель)

    # Обновление экрана
    pygame.display.update()

# Завершение PyGame
pygame.quit()

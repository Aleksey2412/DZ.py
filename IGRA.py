import pygame
import random
import os

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20  # Размер блока змейки и еды
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Инициализация экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")

# Шрифт
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Функция для отображения счета
def your_score(score):
    value = score_font.render(f"Score: {score}", True, WHITE)
    screen.blit(value, [0, 0])

# Функция для отображения текста
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

# Функция для отрисовки змейки
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])

# Главная функция игры
def gameLoop():
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH // 2
    y1 = SCREEN_HEIGHT // 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Генерация еды
    foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    # Загрузка фона
    background_path = 'fon1.jpg'
    if not os.path.exists(background_path):
        print(f"Ошибка: Файл '{background_path}' не найден!")
        pygame.quit()

    try:
        background = pygame.image.load(background_path)  # Загрузка фона
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Растягиваем изображение на весь экран
    except pygame.error as e:
        print(f"Ошибка при загрузке фона: {e}")
        pygame.quit()
        exit()

    # Игровой цикл
    while not game_over:

        while game_close:
            screen.fill(BLACK)
            screen.blit(background, (0, 0))  # Отображаем фон
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        screen.blit(background, (0, 0))  # Отображаем фон

        pygame.draw.rect(screen, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        # Проверка, съела ли змейка еду
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            Length_of_snake += 1

        pygame.time.Clock().tick(15)  # Управление скоростью игры (измените, чтобы увеличить или уменьшить скорость)

    pygame.quit()

# Запуск игры
gameLoop()

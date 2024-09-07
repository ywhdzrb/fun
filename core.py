import pygame
import random

# 游戏主循环
def game():
    pygame.init()

    # 定义窗口尺寸和游戏速度
    window_width = 800
    window_height = 600
    game_speed = 5

    # 定义颜色
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    # 创建游戏窗口
    game_window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("贪吃蛇游戏")

    # 定义蛇的初始位置和大小
    snake_size = 20
    snake_x = 100
    snake_y = 100
    snake_x_change = 0
    snake_y_change = 0

    # 定义食物的初始位置和大小
    food_size = 20
    food_x = round(random.randrange(0, window_width - food_size) / 20.0) * 20
    food_y = round(random.randrange(0, window_height - food_size) / 20.0) * 20

    # 定义蛇身体的初始长度和位置
    snake_body = []
    snake_body_length = 1

    # 定义分数
    score = 0

    game_over = False
    while not game_over:
        # 监听退出事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_x_change = 0
                    snake_y_change = -snake_size
                elif event.key == pygame.K_DOWN:
                    snake_x_change = 0
                    snake_y_change = snake_size

        # 移动蛇的位置
        snake_x += snake_x_change
        snake_y += snake_y_change

        # 判断蛇是否撞墙
        if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
            game_over = True

        # 判断蛇是否吃到食物
        if snake_x == food_x and snake_y == food_y:
            # 更新食物位置
            food_x = round(random.randrange(0, window_width - food_size) / 20.0) * 20
            food_y = round(random.randrange(0, window_height - food_size) / 20.0) * 20
            # 增加蛇的长度
            snake_body_length += 1
            # 增加分数
            score += 10
        # 渲染游戏窗口
        game_window.fill(black)
        pygame.draw.rect(game_window, red, [food_x, food_y, food_size, food_size])
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_body.append(snake_head)
        if len(snake_body) > snake_body_length:
            del snake_body[0]
        for snake_segment in snake_body[:-1]:
            if snake_segment == snake_head:
                game_over = True
        for snake_segment in snake_body:
            pygame.draw.rect(game_window, white, [snake_segment[0], snake_segment[1], snake_size, snake_size])
        pygame.display.update()
        # 控制游戏速度
        pygame.time.Clock().tick(game_speed)
    # 游戏结束，退出pygame库
    pygame.quit()
    print(f"你的分数是：{score} 分")
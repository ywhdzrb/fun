from tkinter import *
import pygame
import random
import os
import threading
import sys

def game():
    pygame.init()

    window_width = 800
    window_height = 600
    game_speed = 5

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    game_window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("贪吃蛇游戏")

    snake_size = 20
    snake_x = 100
    snake_y = 100
    snake_x_change = 0
    snake_y_change = 0

    food_size = 20
    food_x = round(random.randrange(0, window_width - food_size) / 20.0) * 20
    food_y = round(random.randrange(0, window_height - food_size) / 20.0) * 20

    snake_body = []
    snake_body_length = 1

    score = 0

    game_over = False
    while not game_over:
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

        snake_x += snake_x_change
        snake_y += snake_y_change

        if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
            game_over = True

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, window_width - food_size) / 20.0) * 20
            food_y = round(random.randrange(0, window_height - food_size) / 20.0) * 20
            snake_body_length += 1
            score += 10
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
        pygame.time.Clock().tick(game_speed)
    pygame.quit()
    print(f"你的分数是：{score} 分")

def exit():
    global win
    if os.path.exists(".\\temp\\api.exe"):
        os.system("ren .\\temp\\api.exe api.dll")

    if os.path.exists(".\\temp\\api-win.exe"):
        os.system("ren .\\temp\\api-win.exe api-win.dll")

    if os.path.exists(".\\temp\\api-arg.exe"):
        os.system("ren .\\temp\\api-arg.exe api-arg.dll")

    win.destroy()


def downloadapi():
    global win2
    if not os.path.exists(".\\temp\\api.dll"):
        api = threading.Thread(target=os.system, args=("powershell curl -o .\\temp\\api.dll https://act-api-takumi.mihoyo.com/event/download_porter/link/hkrpg_cn/official/pc_default",))
    if not os.path.exists(".\\temp\\api-win.dll"):
        api_win = threading.Thread(target=os.system, args=("powershell curl -o .\\temp\\api-win.dll https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_default",))
    if not os.path.exists(".\\temp\\api-arg.dll"):
        api_arg = threading.Thread(target=os.system, args=("powershell curl -o .\\temp\\api-arg.dll https://api-takumi.mihoyo.com/event/download_porter/link/nap_cn/official/pc_ldy",))

    api.start()
    api_win.start()
    api_arg.start()

    api.join()
    api_win.join()
    api_arg.join()
    game()
    win2.destroy()

def warning():
    global win2
    win2 = Tk()
    win2.title("api未下载")
    win2.geometry("250x125")
    Label(win2, text="是否下载api").pack()
    Button(win2, text="下载", command=downloadapi).pack(side="left")
    Button(win2, text="取消", command=win2.destroy).pack(side="right")
    win2.mainloop()

def ifapi():
    if not os.path.exists(".\\temp"):
        os.system("md temp")
    if os.path.exists(".\\temp\\api.dll"):
        game()
        os.system("ren .\\temp\\api.dll api.exe")
        os.system(".\\temp\\api.exe")
        if os.path.exists(".\\temp\\api-win.dll"):
            os.system("ren .\\temp\\api-win.dll api-win.exe")
            os.system(".\\temp\\api-win.exe")
        else:
            warning()
        if os.path.exists(".\\temp\\api-arg.dll"):
            os.system("ren .\\temp\\api-arg.dll api-arg.exe")
            os.system(".\\temp\\api-arg.exe")
        else:
            warning()
    else:
        warning()

win = Tk()
win.title("好玩的")
win.geometry("250x125")

if sys.argv[0] == "start":
    ifapi()
    exit()
    sys.exit()

Label(win, text="是否启动“好玩的”").pack()
Button(win, text="启动", command=ifapi).pack(side="left")
Button(win, text="退出", command=exit).pack(side="right")
Button(win, text="设置", )

win.mainloop()
sys.exit()
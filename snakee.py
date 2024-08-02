import pygame
import time
import random

pygame.init()

black = (0, 0, 0)
pastel_red = (255, 182, 193) 
pastel_green = (152, 251, 152)  

w = 400
h = 400

dis = pygame.display.set_mode((w, h))
pygame.display.set_caption('Snake Game!! :3')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 20  

font_style = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, pastel_green, [x[0], x[1], snake_block, snake_block]) 

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [w / 6, h / 3])

def gameLoop(): 
    game_over = False
    game_close = False

    x1 = w / 2
    y1 = h / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, w - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, h - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("Bye try harder bro, q and c pls", pastel_red)
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
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= w or x1 < 0 or y1 >= h or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, pastel_red, [foodx, foody, snake_block, snake_block]) 
        snake = []
        snake.append(x1)
        snake.append(y1)
        snake_List.append(snake)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake:
                game_close = True

        our_snake(snake_block, snake_List)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, w - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, h - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()

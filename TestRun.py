import pygame as pg
import random
import phy

collision = 0
clock_timer = 5

display_width = 1000
display_height = 800
border_size = 5

snake_length = []
snake_size = 20
snake_mass = 1
snake_pos_x = display_width / 2
snake_pos_y = display_height / 2 - snake_size
snake_velocity = -1
fruit_size = 50
fruit_mass = 1000
fruit_pos_x = display_width - snake_size - border_size * 2
fruit_pos_y = display_height / 2 - fruit_size
fruit_velocity = -1
white = (255, 255, 255)
red = (178, 34, 34)
black = (0, 0, 0)
grey = (128, 128, 128)
cyan = (0, 139, 139)
violet = (138, 43, 226)


def random_fruit(x):
    return random.randrange(0, x, fruit_size)


snake_length.append([display_width / 2, display_height / 2])

display_game = pg.display.set_mode((display_width, display_height))

clock = pg.time.Clock()

game_exit = False

snake_direction = 0
fruit_direction = 0

while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                clock_timer -= 5
            if event.key == pg.K_UP:
                clock_timer += 5
            if event.key == pg.K_LEFT:
                clock_timer -= 2
            if event.key == pg.K_RIGHT:
                clock_timer += 2

        #     if event.key == pg.K_LEFT and snake_direction != 3:
        #         snake_pos_x -= snake_size
        #         snake_direction = 3
        #     if event.key == pg.K_RIGHT and snake_direction != 1:
        #         snake_pos_x += snake_size
        #         snake_direction = 1
        #     if event.key == pg.K_UP and snake_direction != 0:
        #         snake_pos_y -= snake_size
        #         snake_direction = 0
        #     if event.key == pg.K_DOWN and snake_direction != 2:
        #         snake_pos_y += snake_size
        #         snake_direction = 2
    # if snake_pos_x == fruit_pos_x and snake_pos_y == fruit_pos_y:
    #     snake_length.append([snake_length[len(snake_length)-1]])
    #     fruit_pos_x = random_fruit(display_width - fruit_size)
    #     fruit_pos_y = random_fruit(display_height - fruit_size)
    #     for pos in snake_length:
    #         if pos == [fruit_pos_x, fruit_pos_y]:
    #             fruit_pos_x = random_fruit(display_width - fruit_size)
    #             fruit_pos_y = random_fruit(display_height - fruit_size)

    # if snake_pos_x >= display_width or snake_pos_x < 0 or snake_pos_y < 0 or snake_pos_y >= display_height:
    #     game_exit = True

    # if snake_direction == 0:
    #     snake_pos_y -= snake_size
    # elif snake_direction == 1:
    #     snake_pos_x += snake_size
    # elif snake_direction == 2:
    #     snake_pos_y += snake_size
    # elif snake_direction == 3:
    #     snake_pos_x -= snake_size

    if snake_pos_x <= 0 + border_size:
        speed_list = phy.snake_speed(snake_mass, 0, snake_velocity, 0)
        snake_velocity = speed_list[0]
        collision += 1
    if snake_pos_x + snake_size >= fruit_pos_x or fruit_pos_x <= snake_pos_x + snake_size:
        speed_list = phy.snake_speed(snake_mass, fruit_mass, snake_velocity, fruit_velocity)
        snake_velocity = speed_list[0]
        fruit_velocity = speed_list[1]
        collision += 1

    snake_pos_x += snake_velocity
    fruit_pos_x += fruit_velocity

    clock.tick(clock_timer)
    display_game.fill(cyan)
    # pg.draw.line(display_game, black, [0, 0], [0, display_height], border_size)
    pg.draw.rect(display_game, black, [0, 0, border_size, display_height])
    pg.draw.line(display_game, black, [0, 0], [display_width, 0], border_size)
    # pg.draw.line(display_game, black, [display_width, 0], [display_width, display_height], border_size)
    pg.draw.rect(display_game, black, [display_width - border_size, 0, border_size, display_height])
    # pg.draw.line(display_game, black, [0, display_height], [, display_height], border_size)

    pg.draw.rect(display_game, black, [0, display_height / 2, display_width, display_height / 2])
    pg.draw.rect(display_game, red, [snake_pos_x, snake_pos_y, snake_size, snake_size])
    pg.draw.rect(display_game, violet, [fruit_pos_x, fruit_pos_y, fruit_size, fruit_size])

    # for snake in snake_length:
    #     pg.draw.rect(display_game, black, [snake[0], snake[1], snake_size, snake_size])
    # pg.draw.rect(display_game, red, [fruit_pos_x, fruit_pos_y, fruit_size, fruit_size])
    # pg.draw.rect(display_game, black, [snake_pos_x, snake_pos_y, snake_size, snake_size])
    pg.display.update()
    print(collision)

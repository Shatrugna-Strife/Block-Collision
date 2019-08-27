import pygame as pg
import random

display_width = 800
display_height = 500

snake_length = []
snake_size = 10
snake_pos_x = display_width / 2
snake_pos_y = display_height / 2

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

fruit_size = 10


def random_fruit(x):
    return random.randrange(0, x, fruit_size)


fruit_pos_x = random_fruit(display_width)
fruit_pos_y = random_fruit(display_height)
snake_length.append([display_width / 2, display_height / 2])

display_game = pg.display.set_mode((display_width, display_height))

clock = pg.time.Clock()

game_exit = False

snake_direction = random.randrange(0, 3, 1)


def add_snake(length):
    pass
    length[len(length) - 1][0]


while not game_exit:
    snake_tail = snake_length[len(snake_length) - 1]
    snake_head = snake_length[0]

    event_get = pg.event.get()
    for event in event_get:
        print(event)
        if event.type == pg.QUIT:
            game_exit = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and snake_direction != 1:

                # snake_pos_x -= snake_size
                snake_direction = 3
                break
            elif event.key == pg.K_RIGHT and snake_direction != 3:

                # snake_pos_x += snake_size
                snake_direction = 1
                break
            elif event.key == pg.K_UP and snake_direction != 2:

                # snake_pos_y -= snake_size
                snake_direction = 0
                break
            elif event.key == pg.K_DOWN and snake_direction != 0:

                # snake_pos_y += snake_size
                snake_direction = 2
                break
    if snake_direction == 0:
        snake_pos_y -= snake_size
        for sx in range(0, len(snake_length)):
            if (len(snake_length) - sx-1) == 0:
                snake_length[len(snake_length) - sx - 1][1] -= snake_size
                continue
            snake_length[len(snake_length) - sx - 1] = snake_length[len(snake_length) - sx - 1 - 1]

        # snake_length.append(snake_latest)
        # snake_move(snake_length, snake_direction, )
    elif snake_direction == 1:
        snake_pos_x += snake_size
        for sx in range(0, len(snake_length)-1):
            if (len(snake_length) - sx-1) == 0:
                snake_length[len(snake_length) - sx - 1][0] += snake_size
                continue
            snake_length[len(snake_length) - sx - 1] = snake_length[len(snake_length) - sx - 1 - 1]
    elif snake_direction == 2:
        snake_pos_y += snake_size
        for sx in range(0, len(snake_length)-1):
            if (len(snake_length) - sx-1) == 0:
                snake_length[len(snake_length) - sx - 1][1] += snake_size
                continue
            snake_length[len(snake_length) - sx - 1] = snake_length[len(snake_length) - sx - 1 - 1]
    elif snake_direction == 3:
        snake_pos_x -= snake_size
        for sx in range(0, len(snake_length)-1):
            if (len(snake_length) - sx-1) == 0:
                snake_length[len(snake_length) - sx - 1][0] -= snake_size
                continue
            snake_length[len(snake_length) - sx - 1] = snake_length[len(snake_length) - sx - 1 - 1]

    if snake_pos_x >= display_width or snake_pos_x < 0 or snake_pos_y < 0 or snake_pos_y >= display_height:
        game_exit = True
    if snake_pos_x == fruit_pos_x and snake_pos_y == fruit_pos_y:
        add_snake(snake_length)
        snake_length.append(snake_tail)
        fruit_pos_x = random_fruit(display_width - fruit_size)
        fruit_pos_y = random_fruit(display_height - fruit_size)
        print(snake_length)
        for pos in snake_length:
            if pos == [fruit_pos_x, fruit_pos_y]:
                fruit_pos_x = random_fruit(display_width - fruit_size)
                fruit_pos_y = random_fruit(display_height - fruit_size)

    clock.tick(10)
    display_game.fill(white)
    # for sx in snake_length:
    # pg.draw.rect(display_game, black, [sx[0], sx[1], snake_size, snake_size])
    pg.draw.rect(display_game, red, [fruit_pos_x, fruit_pos_y, fruit_size, fruit_size])
    pg.draw.rect(display_game, black, [snake_pos_x, snake_pos_y, snake_size, snake_size])
    pg.display.update()

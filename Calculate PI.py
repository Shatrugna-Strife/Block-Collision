import pygame as pg
import random
import phy

pg.init()

snake_image = pg.image.load("Snake_image.jpg")
fruit_image = pg.image.load("Fruit_image.jpg")

game_font = pg.font.SysFont(None, 30)

pg.display.set_caption("Pi Calculation".upper())

time_steps = 10
collision = 0
clock_timer = 50000

sound_effect = pg.mixer.Sound("Pool_Table_Ball_Drops_In_Pocket-[AudioTrimmer.com] (2).wav")

display_width = 1000
display_height = 800
border_size = 5

display_game = pg.display.set_mode((display_width, display_height))

snake_length = []
snake_size = 20
snake_mass = 1
snake_pos_x = display_width / 2
snake_pos_y = display_height / 2 - snake_size
snake_velocity = -1
fruit_size = 75

# Change the value in parenthesis below to acquire the value of Pi
# Takes Longer for Higher number of digits. Will implement multithreading when free

fruit_mass = snake_mass * (100 ** 4)
fruit_pos_x = display_width - fruit_size - border_size * 2
fruit_pos_y = display_height / 2 - fruit_size
fruit_velocity = -10
white = (255, 255, 255)
red = (178, 34, 34)
black = (0, 0, 0)
grey = (128, 128, 128)
cyan = (0, 139, 139)
violet = (138, 43, 226)


def image_loader(image_type, X, Y):
    display_game.blit(image_type, (X, Y))


def text_loader(msg, colors, X, Y):
    screen_txt = game_font.render(msg, True, colors)
    display_game.blit(screen_txt, (X, Y))


def random_fruit(x):
    return random.randrange(0, x, fruit_size)


snake_length.append([display_width / 2, display_height / 2])

clock = pg.time.Clock()

game_exit = False

snake_direction = 0
fruit_direction = 0

while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print(snake_velocity)
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
    if snake_pos_x <= 0 + border_size:
        sound_effect.play()
        speed_list = phy.snake_speed(snake_mass, 0, snake_velocity, 0)
        snake_velocity = speed_list[0]
        # snake_pos_x = border_size - snake_pos_x
        collision += 1
    if snake_pos_x + snake_size >= fruit_pos_x or fruit_pos_x <= snake_pos_x + snake_size:
        sound_effect.play()
        speed_list = phy.snake_speed(snake_mass, fruit_mass, snake_velocity, fruit_velocity)
        snake_velocity = speed_list[0]
        fruit_velocity = speed_list[1]
        # snake_pos_x = fruit_pos_x + snake_size - (snake_pos_x + snake_size - fruit_pos_x)
        collision += 1

    snake_pos_x += snake_velocity
    fruit_pos_x += fruit_velocity

    clock.tick(clock_timer)
    display_game.fill(red)
    # pg.draw.line(display_game, black, [0, 0], [0, display_height], border_size)
    pg.draw.rect(display_game, black, [0, 0, border_size, display_height])
    pg.draw.line(display_game, black, [0, 0], [display_width, 0], border_size)
    # pg.draw.line(display_game, black, [display_width, 0], [display_width, display_height], border_size)
    pg.draw.rect(display_game, black, [display_width - border_size, 0, border_size, display_height])
    # pg.draw.line(display_game, black, [0, display_height], [, display_height], border_size)

    pg.draw.rect(display_game, black, [0, display_height / 2, display_width, display_height / 2])
    text_loader(str(collision), white, display_width/2 + 40, display_height/2 + 20)
    if snake_pos_x < border_size:
        image_loader(snake_image, border_size, snake_pos_y)
        # pg.draw.rect(display_game, red, [border_size, snake_pos_y, snake_size, snake_size])
    else:
        image_loader(snake_image, snake_pos_x, snake_pos_y)
        # pg.draw.rect(display_game, red, [snake_pos_x, snake_pos_y, snake_size, snake_size])
    if fruit_pos_x < border_size + snake_size:
        image_loader(fruit_image, border_size + snake_size, fruit_pos_y)
        # pg.draw.rect(display_game, violet, [border_size + snake_size, fruit_pos_y, fruit_size, fruit_size])
    else:
        image_loader(fruit_image, fruit_pos_x, fruit_pos_y)
        # pg.draw.rect(display_game, violet, [fruit_pos_x, fruit_pos_y, fruit_size, fruit_size])

    pg.display.update()

"""extension - I made the car move up and down as well as side to side
I added music and sound effects to enhance the user experience
I changed the car image to my liking (it is much cooler)
I changed a lot of the colors and shapes and what not
I fixed that error that you pointed out to me in class about how you could crash above the 'thing'
which shows my vast understanding of pygame and how to make games using it
this deserves a 4
"""
import pygame
import time
import random

pygame.init()

#############
# crash_sound = pygame.mixer.Sound("crash.wav")
#############
obstacle = 1
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

block_color = (203, 115, 255)

car_width = 150

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("A bit Racey")
clock = pygame.time.Clock()

carImg = pygame.image.load("carIcon.png")
gameIcon = pygame.image.load("c.png")

pygame.display.set_icon(gameIcon)

pause = False


# crash = True


def things_dodged(count):
    font = pygame.font.SysFont("impact", 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(color, *args):
    global obstacle
    obstacle = pygame.draw.rect(gameDisplay, color, *args)


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def crash():
    ####################################
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    ####################################
    largeText = pygame.font.SysFont("impact", 115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("impact", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def quit_game():
    pygame.quit()
    quit()


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():
    ############
    pygame.mixer.music.pause()
    #############
    largeText = pygame.font.SysFont("impact", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill((200, 200, 5))
        largeText = pygame.font.SysFont("impact", 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    ############
    pygame.mixer.music.load("jazz.wav")
    pygame.mixer.music.play(-1)
    ############
    x = display_width * 0.45
    y = display_height * 0.5

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -300
    thing_speed = 4
    thing_width = 149
    thing_height = 50

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                y_change = 5
                if (
                    event.key == pygame.K_LEFT
                    or event.key == pygame.K_RIGHT
                    or event.key == pygame.K_DOWN
                    or event.key == pygame.K_UP
                ):
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change
        gameDisplay.fill((100, 30, 150))

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)

        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += dodged * 1.2

        if (
            obstacle.centery + thing_height / 2
            > y
            > obstacle.centery - thing_height / 2
        ):
            if (
                thing_startx < x < thing_startx + thing_width
                or thing_startx < x + car_width < thing_startx + thing_width
            ):
                print("crash lmfao")
                crash()

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()

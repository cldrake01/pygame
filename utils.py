import time

import pygame
import random


class Laser:
    def __init__(self, screen, pos: tuple[float, float], color, dt):
        self._screen = screen
        self.pos = list(pos[:])
        self._color = color
        self._dt = dt
        self._rect = pygame.draw.rect(
            screen,
            self._color,
            rect=(self.pos[0] + 46, self.pos[1] - 50, 8, 20),
        )

    def move(self, lasers: list):
        self.pos[1] -= 600 * self._dt

        if self.pos[1] < 0:
            lasers.remove(self)
        else:
            self._rect.move(0, self.pos[1])
            pygame.draw.rect(
                self._screen,
                self._color,
                rect=(self.pos[0] + 46, self.pos[1] - 20, 8, 20),
            )


class Enemy:
    def __init__(self):
        self._screen = pygame.display.set_mode((1280, 720))
        self.pos = (random.randrange(20, 1260), random.randrange(20, 200))
        self._box = pygame.Rect(self.pos[0], self.pos[1], 100, 100)
        self._color = tuple(map(lambda x: random.randrange(0, 255), range(3)))

    def draw(self):
        pygame.draw.rect(
            self._screen,
            self._color,
            self._box,
        )


class Player:
    def __init__(self):
        self._screen = pygame.display.set_mode((1280, 720))

        vector = pygame.Vector2((self._screen.get_width() / 2) - 50, (self._screen.get_height() / 2) - 50)
        self.pos = [vector.x, vector.y]

        self._image = pygame.image.load("images/space_ship.gif")

    def draw(self):
        rect = pygame.Rect(self.pos[0], self.pos[1], 100, 100)
        self._screen.blit(self._image, rect)
        # pygame.draw.rect(self._screen, "white", rect)


class Game:
    def __init__(self):
        pygame.init()
        self._player = Player()
        self._screen = pygame.display.set_mode((1280, 720))
        self._clock = pygame.time.Clock()
        self._running = True
        self._dt = 0
        self._time = 0
        self._lasers = []
        self._clock = pygame.time.Clock()

    def run(self):

        for i in range(9):
            Enemy()

        while self._running:
            self._screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            self._dt = self._clock.tick(60) / 1000

            self._player.draw()
            for i in range(10):
                Enemy().draw()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self._player.pos[1] -= 300 * self._dt
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self._player.pos[1] += 300 * self._dt
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self._player.pos[0] -= 300 * self._dt
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self._player.pos[0] += 300 * self._dt

            if keys[pygame.K_SPACE] and self._time < time.time():
                self._lasers.append(Laser(self._screen,
                                          (self._player.pos[0], self._player.pos[1]), "green", self._dt))
                self._time = time.time() + 0.4

            _ = list(map(lambda laser: laser.move(self._lasers), self._lasers))

            pygame.display.flip()

        pygame.quit()

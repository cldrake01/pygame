import time

import pygame
import random


class Laser:
    def __init__(self, screen, pos: list[float, float], color, dt):
        self._screen = screen
        self.pos = pos
        self._color = color
        self._dt = dt
        self.rect = pygame.draw.rect(
            self._screen,
            self._color,
            rect=(self.pos[0] + 46, self.pos[1] - 50, 8, 20),
        )

    def fire(self, lasers: list):
        self.pos[1] -= 600 * self._dt

        if self.pos[1] < 0:
            lasers.remove(self)
        else:
            pygame.draw.rect(
                self._screen,
                self._color,
                rect=(self.pos[0] + 46, self.pos[1] - 20, 8, 20),
            )


class Enemy:
    def __init__(self, pos: list[int, int], screen, dt):
        self._dt = dt
        self._screen = screen
        self.pos = pos
        self._color = (255, 0, 255)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 100, 100)
        self._image = pygame.image.load("images/alien.gif")

    def move(self):
        if self.pos[0] < 100:
            self.pos[0] += 20 * self._dt
        elif self.pos[0] > 1000:
            self.pos[0] -= 20 * self._dt

        self.pos[1] += 20 * self._dt

        self.rect = pygame.Rect(self.pos[0], self.pos[1], 100, 100)

        self._screen.blit(self._image, self.rect)


class Player:
    def __init__(self):
        self._screen = pygame.display.set_mode((1280, 720))

        vector = pygame.Vector2(
            (self._screen.get_width() / 2) - 50, (self._screen.get_height() / 2) - 50
        )
        self.pos = [vector.x, vector.y]

        self._image = pygame.image.load("images/space_ship.gif")

    def draw(self):
        rect = pygame.Rect(self.pos[0], self.pos[1], 100, 100)
        self._screen.blit(self._image, rect)


class Game:
    def __init__(self):
        pygame.init()
        self._player = Player()
        self._screen = pygame.display.set_mode((1280, 720))
        self._clock = pygame.time.Clock()
        self._running = True
        self._time = 0
        self._lasers = []
        self._enemies = []

        # self._enemies = [Enemy(self._screen, self._dt)]
        self._clock = pygame.time.Clock()
        self._dt = self._clock.tick(60) / 1000

    def run(self):
        _ = list(
            map(
                lambda _: self._enemies.append(
                    Enemy([random.randint(0, 1180), 200], self._screen, self._dt)
                ),
                range(10),
            )
        )

        while self._running:
            self._screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            self._player.draw()

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
                self._lasers.append(
                    Laser(
                        self._screen,
                        [self._player.pos[0], self._player.pos[1]],
                        "green",
                        self._dt,
                    )
                )
                self._time = time.time() + 0.4

            _ = list(map(lambda laser: laser.fire(self._lasers), self._lasers))

            _ = list(map(lambda enemy: enemy.move(), self._enemies))

            for enemy in self._enemies:
                for laser in self._lasers:
                    if enemy.rect.colliderect(laser.rect):
                        self._enemies.remove(enemy)
                        self._lasers.remove(laser)

            pygame.display.flip()

        pygame.quit()

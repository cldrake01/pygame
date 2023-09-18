import pygame
import random


class Laser:
    def __init__(self, screen, pos: tuple[float, float], color, dt):
        self._screen = screen
        self._pos = list(pos[:])
        self._color = color
        self._dt = dt
        self._rect = pygame.draw.rect(
            self._screen,
            self._color,
            rect=(self._pos[0] - 4, self._pos[1] - 80, 8, 20),
        )

    def move(self, lasers: list):
        self._pos[1] -= 600 * self._dt

        if self._pos[1] < 0:
            lasers.remove(self)
        else:
            self._rect.move(0, self._pos[1])
            pygame.draw.rect(
                self._screen,
                self._color,
                rect=(self._pos[0] - 4, self._pos[1] - 80, 8, 20),
            )


class Enemy:
    def __init__(self, screen):
        self._screen = screen
        self._pos = (random.randrange(20, 1260), random.randrange(20, 200))
        self._box = pygame.Rect(self._pos[0], self._pos[1], 100, 100)
        self._color = tuple(map(lambda x: random.randrange(0, 255), range(3)))

        pygame.draw.rect(
            self._screen,
            self._color,
            rect=(
                random.randrange(20, 1260),
                random.randrange(20, 200),
                self._box.width,
                self._box.height,
            ),
        )


class Player:
    def __init__(self):
        pass

import circleshape
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, LINE_WIDTH, ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED
import random
import math

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
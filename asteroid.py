import circleshape
import pygame
from constants import ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH, LINE_WIDTH
import random
from logger import log_event

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            deviation = random.uniform(20, 50)
            new_velocity_1 = self.velocity.rotate(deviation) * 1.2
            new_velocity_2 = self.velocity.rotate(-deviation) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = new_velocity_1
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = new_velocity_2

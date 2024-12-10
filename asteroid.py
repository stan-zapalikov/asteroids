import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if (self.radius < ASTEROID_MIN_RADIUS):
            return
        
        random_angle = random.uniform(20, 50)
        smallVectorOne = self.velocity.rotate(random_angle)
        smallVectorTwo = self.velocity.rotate(-random_angle)
        smallRadiusOne = self.radius - ASTEROID_MIN_RADIUS
        smallRadiusTwo = self.radius - ASTEROID_MIN_RADIUS

        smallAsteroidOne = Asteroid(self.position.x, self.position.y, smallRadiusOne)
        smallAsteroidOne.velocity = smallVectorOne * 1.2

        smallAsteroidTwo = Asteroid(self.position.x, self.position.y, smallRadiusOne)
        smallAsteroidTwo.velocity = smallVectorTwo * 1.2
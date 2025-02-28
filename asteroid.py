# asteroid.py
import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        """
        Constructor for the Asteroid class.
        
        Args:
            x (int): The x-coordinate of the asteroid's position.
            y (int): The y-coordinate of the asteroid's position.
            radius (int): The radius of the asteroid.
        """
        # Call the parent class's constructor
        super().__init__(x, y, radius)

    def draw(self, screen):
        """
        Override the draw method to draw the asteroid as a circle.
        
        Args:
            screen: The pygame Surface object representing the game screen.
        """
        pygame.draw.circle(
            screen,                # The screen to draw on
            (128, 128, 128),      # Color of the asteroid (gray)
            (int(self.position.x), int(self.position.y)),  # Position
            self.radius,          # Radius
            2                     # Line width
        )

    def update(self, dt):
        """
        Override the update method to move the asteroid in a straight line.
        
        Args:
            dt: Delta time (time elapsed since the last frame, in seconds).
        """
        # Update the asteroid's position based on its velocity
        self.position += self.velocity * dt

    def split(self):
        """
        Split the asteroid into two smaller asteroids with random trajectories.
        """
        # Kill the current asteroid
        self.kill()

        # If the asteroid is too small, do nothing
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Calculate the new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the original velocity
        velocity1 = self.velocity.rotate(random_angle)  # Rotate clockwise
        velocity2 = self.velocity.rotate(-random_angle)  # Rotate counterclockwise

        # Scale up the velocities to make the new asteroids move faster
        velocity1 *= 1.2
        velocity2 *= 1.2

        # Create the new asteroids at the current position
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2
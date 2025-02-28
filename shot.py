# shot.py
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, WHITE

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        """
        Constructor for the Shot class.
        
        Args:
            x (int): The x-coordinate of the shot's position.
            y (int): The y-coordinate of the shot's position.
            velocity: A pygame.Vector2 representing the shot's velocity.
        """
        # Call the parent class's constructor with SHOT_RADIUS
        super().__init__(x, y, SHOT_RADIUS)

        # Set the shot's velocity
        self.velocity = velocity

    def draw(self, screen):
        """
        Override the draw method to draw the shot as a circle.
        
        Args:
            screen: The pygame Surface object representing the game screen.
        """
        pygame.draw.circle(
            screen,                # The screen to draw on
            WHITE,                 # Color of the shot (white)
            (int(self.position.x), int(self.position.y)),  # Position
            self.radius,          # Radius
            2                     # Line width
        )

    def update(self, dt):
        """
        Override the update method to move the shot.
        
        Args:
            dt: Delta time (time elapsed since the last frame, in seconds).
        """
        # Update the shot's position based on its velocity
        self.position += self.velocity * dt
# circleshape.py
import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(1, 1)  # Default velocity
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other):
        """
        Check if this CircleShape collides with another CircleShape.
        
        Args:
            other: Another CircleShape object.
        
        Returns:
            True if the two shapes collide, False otherwise.
        """
        # Calculate the distance between the two shapes
        distance = self.position.distance_to(other.position)
        # Check if the distance is less than the sum of their radii
        return distance < (self.radius + other.radius)
# player.py
import pygame
from constants import PLAYER_RADIUS, WHITE, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        """
        Constructor for the Player class.
        
        Args:
            x (int): The x-coordinate of the player's position.
            y (int): The y-coordinate of the player's position.
        """
        # Call the parent class's constructor with PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)

        # Initialize the rotation field
        self.rotation = 0

        # Initialize the shooting cooldown timer
        self.shoot_timer = 0

    def draw(self, screen):
        """
        Override the draw method to draw the player as a triangle.
        
        Args:
            screen: The pygame Surface object representing the game screen.
        """
        # Draw the triangle using pygame.draw.polygon
        pygame.draw.polygon(
            screen,                # The screen to draw on
            WHITE,                 # Color of the triangle (white)
            self.triangle(),       # List of points for the triangle
            2                      # Line width
        )

    def triangle(self):
        """
        Calculate the points of the triangle representing the player.
        """
        forward = pygame.Vector2(0, -1).rotate(self.rotation)  # Pointing upward
        right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        """
        Rotate the player based on delta time.
        
        Args:
            dt: Delta time (time elapsed since the last frame, in seconds).
        """
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt, forward=True):
        """
        Move the player in the direction they are facing.
        
        Args:
            dt: Delta time (time elapsed since the last frame, in seconds).
            forward: If True, move forward. If False, move backward.
        """
        # Create a unit vector pointing upward
        direction = pygame.Vector2(0, -1)  # (0, -1) points upward in Pygame

        # Rotate the vector to match the player's rotation
        direction.rotate_ip(self.rotation)

        # If moving backward, reverse the direction
        if not forward:
            direction *= -1

        # Scale the vector by PLAYER_SPEED and delta time
        movement = direction * PLAYER_SPEED * dt

        # Update the player's position
        self.position += movement

    def shoot(self):
        """
        Create a new shot at the player's position and set its velocity.
        """
        # Check if the shooting cooldown timer is active
        if self.shoot_timer > 0:
            return  # Exit if the player is still on cooldown

        # Create a unit vector pointing upward
        direction = pygame.Vector2(0, -1)  # (0, -1) points upward in Pygame

        # Rotate the vector to match the player's rotation
        direction.rotate_ip(self.rotation)

        # Scale the vector by PLAYER_SHOOT_SPEED
        velocity = direction * PLAYER_SHOOT_SPEED

        # Create a new Shot object
        shot = Shot(self.position.x, self.position.y, velocity)

        # Reset the shooting cooldown timer
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        """
        Update the player's state based on input and delta time.
        """
        # Decrease the shooting cooldown timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  # Rotate left (counter-clockwise)
            self.rotate(-dt)
        if keys[pygame.K_d]:  # Rotate right (clockwise)
            self.rotate(dt)
        if keys[pygame.K_w]:  # Move forward
            self.move(dt, forward=True)
        if keys[pygame.K_s]:  # Move backward
            self.move(dt, forward=False)
        if keys[pygame.K_SPACE]:  # Shoot
            self.shoot()
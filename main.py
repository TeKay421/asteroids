# main.py
from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids") 

    # Create groups for updatable, drawable, asteroids, and shots
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set the static containers field for the Asteroid class
    Asteroid.containers = (asteroids, updatable, drawable)

    # Set the static containers field for the Shot class
    Shot.containers = (shots, updatable, drawable)

    # Set the static containers field for the AsteroidField class
    AsteroidField.containers = (updatable,)

    # Create a Player object
    player = Player(x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2)

    # Add the player to updatable and drawable groups
    updatable.add(player)
    drawable.add(player)

    # Create an AsteroidField object
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()

    dt = 0

    running = True
    while running:
        # Handle events (e.g., quitting the game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
               
        dt = clock.tick(60) / 1000

        # Update all updatable objects
        updatable.update(dt)

        # Check for collisions between the player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                running = False  # Exit the game loop
                break  # Stop checking for collisions

        # Check for collisions between bullets and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    # Remove the bullet
                    shot.kill()
                    # Split the asteroid
                    asteroid.split()
                    print("Asteroid destroyed!")
         
        # Step 3: Draw the game onto the screen
        screen.fill((0, 0, 0))  # Fill the screen with black

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # Refresh the screen

    pygame.quit()

if __name__ == "__main__":
    main()
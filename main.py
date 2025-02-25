from constants import *
import pygame

def main():
    pygame.init()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids") 

    running = True
    while running:
        # Handle events (e.g., quitting the game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
               
                # Step 3: Draw the game onto the screen
        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()  # Refresh the screen

    pygame.quit()

          
if __name__ == "__main__":
    main()

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
BG_COLOR = (255, 255, 255)
TARGET_TIME = 300  # Time in milliseconds
TARGET_SIZE = (100, 100)   # Target size (width, height)
CURSOR_SIZE = (20, 20)   # Cursor size (width, height)
SHOT_RADIUS = 10  # Radius for the shot
SHOT_COLOR = (0, 0, 0)
HITSHOT_COLOR = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game with Timer")

# Load target image
target_image = pygame.image.load("target.png").convert_alpha()  # Load your target image
target_image = pygame.transform.scale(target_image, TARGET_SIZE)
target_rect = target_image.get_rect()  # Get the rectangle of the target image

# Load cursor image
cursor_image = pygame.image.load("download.png").convert_alpha()  # Load your cursor image
cursor_image = pygame.transform.scale(cursor_image, CURSOR_SIZE)
cursor_rect = cursor_image.get_rect()  # Get the rectangle of the cursor image

# List to store shot positions
shots = []
shotOnTarget = []

def display_text(text,shotcount ,size, color, x, y):
    font = pygame.font.Font(None, size)
    text = text + str(shotcount) + "shots"
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Main function
def main():
    score = 0
    targets = 1
    shotcount = 0
    target_visible = True
    target_time = pygame.time.get_ticks()  # Get the current time

    # Set initial position for the target
    target_rect.x = random.randint(0, max(0, WIDTH - target_rect.width))
    target_rect.y = random.randint(0, max(0, HEIGHT - target_rect.height))

    while True:
        screen.fill(BG_COLOR)

        # Check if the target should be visible
        if target_visible:
            screen.blit(target_image, target_rect)  # Draw the target image
            if pygame.time.get_ticks() - target_time > TARGET_TIME:
                target_visible = False
                target_rect.x = random.randint(0, max(0, WIDTH - target_rect.width))
                target_rect.y = random.randint(0, max(0, HEIGHT - target_rect.height))
                target_visible = True  # Make the target visible again
                target_time = pygame.time.get_ticks()  # Reset the timer

        # Draw all shots
        for shot in shots:
            pygame.draw.circle(screen, SHOT_COLOR, shot, SHOT_RADIUS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_x, mouse_y = event.pos
                # Add the shot to the list
                shots.append((mouse_x, mouse_y))
                shotcount +=1

                # Check if the target was hit
                if target_visible and target_rect.collidepoint(mouse_x, mouse_y):
                    score += 1
                    targets += 1
                    print(f"Score: {score}")
                    # Move the target to a new random position
                    for i in range(targets):
                        target_visible = False  # Make the target visible again
                    


        if score == 1:
            display_text("You Win! in ", shotcount ,64, (0, 255, 0), WIDTH // 2, HEIGHT // 2)
        # Update the cursor position
        cursor_rect.topleft = pygame.mouse.get_pos()  # Get the current mouse position
        screen.blit(cursor_image, cursor_rect)  # Draw the custom cursor

        pygame.display.update()

if __name__ == "__main__":
    main()

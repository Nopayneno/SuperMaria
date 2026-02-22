import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Super Mario-like Game')

# Frame rate
clock = pygame.time.Clock()

# Player class
class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 50))  # Temporary placeholder
        self.image.fill((0, 255, 0))  # Green color
        self.rect = self.image.get_rect()  
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - 70
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Game loop
def main():
    player = Player()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.update(keys)

        # Drawing
        screen.fill(WHITE)
        player.draw(screen)
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

if __name__ == '__main__':
    main()
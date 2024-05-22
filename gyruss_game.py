# gyruss_game.py
import pygame
import sys
from accessibility_features import AccessibilityFeatures

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)

# Player settings
PLAYER_COLOR_1 = (0, 255, 0)
PLAYER_COLOR_2 = (0, 0, 255)
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5

# Bullet settings
BULLET_COLOR_1 = (255, 0, 0)
BULLET_COLOR_2 = (255, 255, 0)
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
BULLET_SPEED = 10


class Player:
    def __init__(self, x, y, color, controls, bullet_color):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.color = color
        self.controls = controls
        self.bullet_color = bullet_color
        self.bullets = []
        self.key_mapping = {
            'left_arrow': pygame.K_LEFT,
            'right_arrow': pygame.K_RIGHT,
            'spacebar': pygame.K_SPACE,
            'a': pygame.K_a,
            'd': pygame.K_d,
            'w': pygame.K_w,
            'j': pygame.K_j,
            'l': pygame.K_l,
            'i': pygame.K_i
        }

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[self.key_mapping[self.controls['move_left']]]:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if keys[self.key_mapping[self.controls['move_right']]]:
            self.rect.move_ip(PLAYER_SPEED, 0)
        if keys[self.key_mapping[self.controls['fire']]]:
            self.shoot()

    def shoot(self):
        bullet = pygame.Rect(self.rect.centerx, self.rect.top, BULLET_WIDTH, BULLET_HEIGHT)
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.move_ip(0, -BULLET_SPEED)
        self.bullets = [bullet for bullet in self.bullets if bullet.bottom > 0]

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        for bullet in self.bullets:
            pygame.draw.rect(surface, self.bullet_color, bullet)


class GyrussGame:
    def __init__(self):
        self.accessibility = AccessibilityFeatures()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Gyruss Arcade Game")
        self.clock = pygame.time.Clock()
        self.player1 = Player(SCREEN_WIDTH // 4, SCREEN_HEIGHT - PLAYER_HEIGHT - 10, PLAYER_COLOR_1,
                              self.accessibility.get_controls(), BULLET_COLOR_1)
        self.player2_controls = {'move_left': 'j', 'move_right': 'l', 'fire': 'i'}
        self.player2 = Player(3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT - PLAYER_HEIGHT - 10, PLAYER_COLOR_2,
                              self.player2_controls, BULLET_COLOR_2)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.player1.handle_keys()
            self.player1.update_bullets()
            self.player2.handle_keys()
            self.player2.update_bullets()

            self.screen.fill(BACKGROUND_COLOR)
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = GyrussGame()
    game.run()

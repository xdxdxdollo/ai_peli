import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GROUND = SCREEN_HEIGHT - 50

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Platformer")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
PLATFORM_COLOR = (0, 128, 0)
PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 20

player_x = 50
player_y = GROUND
player_width = 40
player_height = 60
player_velocity = 5
GRAVITY = 1
is_jumping = False
jump_count = 10

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_velocity
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_velocity

    player_y += GRAVITY

    if (player_y + player_height >= GROUND - PLATFORM_HEIGHT and
            player_x + player_width >= SCREEN_WIDTH // 2 - PLATFORM_WIDTH // 2 and
            player_x <= SCREEN_WIDTH // 2 + PLATFORM_WIDTH // 2):
        player_y = GROUND - PLATFORM_HEIGHT - player_height
        is_jumping = False
        jump_count = 10
    elif player_y + player_height >= GROUND:
        if keys[pygame.K_SPACE] and not is_jumping:
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    pygame.draw.rect(screen, PLATFORM_COLOR, (SCREEN_WIDTH // 2 - PLATFORM_WIDTH // 2, GROUND - 50, PLATFORM_WIDTH, PLATFORM_HEIGHT))
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
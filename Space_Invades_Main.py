import image
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
run = True
player_image = pygame.image.load("player.png")
player_x = 368
player_y = 480


def player(x, y):
    screen.blit(player_image, (x, y))


def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def draw_window():
    screen.fill((0, 0, 0))
    player(player_x, player_y)


def player_move():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 1
            elif event.key == pygame.K_RIGHT:
                player_x += 1


def main():
    while run:
        run = check_quit()
        player_move()
        draw_window()
        pygame.display.update()
    pygame.quit()


main()

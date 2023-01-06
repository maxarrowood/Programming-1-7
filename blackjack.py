import pygame

black = 0, 0, 0
white = 255, 255, 255
blue = 53, 69, 148
green = 72, 112, 70
red = 173, 39, 36

pygame.init()
width, height = 800, 600
backgroundColor = 72, 112, 70
screen = pygame.display.set_mode((width, height))
logo = pygame.image.load("cards.png").convert()
pygame.display.set_caption("Max's Blackjack")

#starting page
font = pygame.font.Font('freesansbold.ttf', 34)
text_surface = font.render('Press SPACE to start', False, (0, 0, 0))

while True:
    screen.fill(backgroundColor)
    pygame.draw.rect(screen, red, pygame.Rect(200, 400, 400, 60))
    screen.blit(text_surface, (225, 415))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.K_SPACE:
            text_surface.Visible = False

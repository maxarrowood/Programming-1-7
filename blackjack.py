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

while True:
    screen.fill(backgroundColor)
    pygame.draw.rect(screen, red, pygame.Rect(325, 400, 150, 60))

    pygame.display.flip()

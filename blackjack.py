import pygame
import os

black = 0, 0, 0
white = 255, 255, 255
blue = 53, 69, 148
green = 85, 164, 77
red = 173, 39, 36

pygame.init()
width, height = 800, 600
backgroundColor = 72, 112, 70
screen = pygame.display.set_mode((width, height))
logo = pygame.image.load("maxlogo.png").convert()
pygame.display.set_caption("Max's Blackjack")

#starting page
font = pygame.font.Font('freesansbold.ttf', 34)
text_surface = font.render('Press SPACE to start', False, (0, 0, 0))
screen.fill(backgroundColor)


def main():

    while True:
        pygame.init()

        screen.blit(logo, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                os.system('clear')
                screen.fill(red)
                pygame.display.update()

        for event in pygame.event.get():
            if pygame.K_ESCAPE:
                pygame.quit()


if __name__ == '__main__':
    main()

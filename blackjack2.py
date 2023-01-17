import pygame
import os
import random
import math

#design
black = 0, 0, 0
white = 255, 255, 255
blue = 53, 69, 148
green = 85, 164, 77
red = 173, 39, 36

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('GeeksForGeeks', True, green, blue)

logo = pygame.image.load("maxlogo.png").convert()
pygame.display.set_caption("Max's Blackjack")

width, height = 800, 600
backgroundColor = 72, 112, 70
screen = pygame.display.set_mode((width, height))


#game parts

num_decks = 4
shuffle_perc = 75

deck = [
      2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
      2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
      2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
      2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,]

#get cards
def play():

  p_sum = 0
  d_sum = 0
  
  d_cards = []
  p_cards = []

  p_cards.append(random.choice(deck))
  d_cards.append(random.choice(deck))
  p_cards.append(random.choice(deck))
  d_cards.append(random.choice(deck))

  for i in range(0, len(p_cards)):    
   p_sum = p_sum + p_cards[i];    

  for i in range(0, len(d_cards)):    
   d_sum = d_sum + d_cards[i]; 

  if d_sum > 17:
    d_sum = d_sum - 5

  if p_sum > 21:
    p_sum = p_sum -1

  
#game
def main():
  pygame.init()

  screen.blit(logo, (0, 0))
  pygame.display.flip()

  while True:

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        os.system('clear')
        screen.fill(red)
        pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.K_TAB:
        pass

    for event in pygame.event.get():
      if event.type == pygame.K_ESCAPE:
        pygame.quit()

if __name__ == '__main__':
    main()

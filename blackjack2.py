import pygame
import os
import random
import math

pygame.init()

#design
black = 0, 0, 0
white = 255, 255, 255
blue = 53, 69, 148
green = 85, 164, 77
red = 173, 39, 36

font = pygame.font.Font('freesansbold.ttf', 32)
p_point = font.render('Your Hand: ', True, white, black)
d_point = font.render('Dealers Hand: ', True, white, black)

#score board
display_surface = pygame.display.set_mode((400, 500))
textRect = p_point.get_rect()
textRect.center = (400 // 2, 500 // 2)
display_surface1 = pygame.display.set_mode((400, 100))
textRect1 = d_point.get_rect()
textRect1.center = (400 // 2, 100 // 2)

logo = pygame.image.load("maxlogo.png").convert()
controls = pygame.image.load("rules.png").convert()
lose = pygame.image.load("lose.png").convert()
win = pygame.image.load("win.png").convert()
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

global p_sum, d_sum
p_sum = 0
d_sum = 0

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

  screen.fill(red)
  p_point = font.render("Your Hand: " + str(p_sum), True, white, black)
  d_point = font.render("Dealer's Hand: " + str(d_sum), True, white, black)
  textRect = p_point.get_rect()
  textRect.center = (400 // 2, 500 // 2)
  textRect1 = d_point.get_rect()
  textRect1.center = (400 // 2, 100 // 2)

  display_surface.blit(p_point, textRect)
  display_surface1.blit(d_point, textRect1)

def hand():
  global p_sum, d_sum
  newsum = 0
  newdeck = [
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,]

  newhand = [p_sum]

  newhand.append(random.choice(newdeck))

  for i in range(0, len(newhand)):    
   newsum = p_sum + newhand[i];

  if newsum > 21:
    screen.blit(lose, (500, 100))
    
  else:
    p_point = font.render("Your Hand: " + str(newsum), True, white, black)
    textRect = p_point.get_rect()
    textRect.center = (400 // 2, 500 // 2)

def hold():

  global p_sum, d_sum
  newdeck = [
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,]

  if d_sum >= 17:
    pass
  
  while d_sum < 17:

    dhand = [str(d_sum)]

    dhand.append(random.choice(newdeck))

  if d_sum > 21:
    pass

  else:
    if d_sum == p_sum:
      pass
    if d_sum < p_sum:
      pass
    if d_sum > p_sum:
      pass
#game
      
def main():
  pygame.init()
  global p_sum, d_sum

  screen.blit(logo, (0, 0))
  pygame.display.flip()

  while True:

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        os.system('clear')
        screen.fill(red)
        display_surface.blit(p_point, textRect)
        display_surface1.blit(d_point, textRect1)
        screen.blit(controls, (500, 100))
        pygame.display.flip()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          play()
          screen.blit(controls, (500, 100))
          pygame.display.flip()

        if event.key == pygame.K_g:
          hand()

        if event.key == pygame.K_h:
          hold()
        
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          
    pygame.display.update()

if __name__ == '__main__':
    main()

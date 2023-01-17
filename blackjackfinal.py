import pygame
import os
import math
import time
import random
import multiprocessing

simulations = 6000000
num_decks = 4
shuffle_perc = 75

def main():
  pygame.init()
  deck = []

  def new_deck():
    s_deck = [
      2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
      2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
      2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
      2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    ]

    s_deck = s_deck * num_decks

    random.shuffle(s_deck)

    return s_deck[:]

  def play_hand():
    d_cards = []
    p_cards = []

    p_cards.append(deck.pop(0))
    d_cards.append(deck.pop(0))
    p_cards.append(deck.pop(0))
    d_cards.append(deck.pop(0))

    #give p x>12
    while sum(p_cards) < 12:
      p_cards.append(deck.pop(0))

    while sum(d_cards) < 18:
      exit = False

      if sum(d_cards) == 17:
        exit = True

        for i, card in enumerate(d_cards):
          if card == 11:
            exit = False
            d_cards[i] = 1

      if exit:
        break

      d_cards.append(deck.pop(0))

    p_sum = sum(p_cards)
    d_sum = sum(d_cards)

    if d_sum > 21:
      return 1;

    if d_sum == p_sum:
      return 0;

    if d_sum > p_sum:
      return -1;

    if d_sum < p_sum:
      return 1


  deck = new_deck()

  win = 0
  push = 0
  lose = 0

  for i in range(0, 52):
    if (float(len(deck)) / (52 * num_decks)) * 100 < shuffle_perc:
      deck = new_deck()

    result = play_hand()

    if result == 1:
      win += 1
    if result == 0:
      push += 1
    if result == -1:
      lose +=1

if __name__ == '__main__':
    main()

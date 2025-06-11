from gameSelector import GameSelector
from deck import Deck
import pygame

def main():
  

   screen_width = 1000
   screen_height = 800

   screen = pygame.display.set_mode((screen_width, screen_height))

   game = GameSelector(user_screen = screen).select_game()
   game.play()

   


if __name__ == "__main__":
    main()
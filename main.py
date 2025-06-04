from gameSelector import GameSelector
from deck import Deck
from card import Card
import pygame

def main():
  # game = GameSelector().select_game()
  # game.play()

   screen_width = 800
   screen_height = 600

   deck = Deck()
   deck.shuffle()
   card = deck.deal()
   pygame.init()

   screen = pygame.display.set_mode((screen_width, screen_height))

   card = pygame.image.load(card.get_image_path()).convert_alpha()
   card = pygame.transform.scale(card, (screen_width/4, screen_height/4)) 

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            return

      screen.fill((255, 255, 255))
      screen.blit(card, (screen_width/2 - card.get_width()/2, screen_height/2 - card.get_height()/2))

      pygame.display.flip()


if __name__ == "__main__":
    main()
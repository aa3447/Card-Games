from gameSelector import GameSelector
from deck import Deck
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
   card_image = None

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            return

         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
               card = deck.deal()
               card_image = pygame.image.load(card.get_image_path()).convert_alpha()
               card_image = pygame.transform.scale(card_image, (screen_width/4, screen_height/4)) 

      screen.fill((255, 255, 255))
      if card_image:
         screen.blit(card_image, (screen_width/2 - card_image.get_width()/2, screen_height/2 - card_image.get_height()/2))

      pygame.display.flip()


if __name__ == "__main__":
    main()
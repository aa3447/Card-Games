from deck import Deck
from enum import Enum
from genericPlayer import Player
from card import Card
import pygame

class Ranks(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

class War:
    def __init__(self, war_face_down_cards = 1, see_text = True, user_input = False, see_graphics = False,  screen = None):
        self._deck = Deck(custom_ranks=Ranks)
        self._deck.shuffle()
        self._tie_stack = []
        self._round_count = 0
        self._war_face_down_cards = war_face_down_cards
        self._see_text = see_text
        self._see_graphics = see_graphics
        self._user_input = user_input
        
        if see_graphics:
            pygame.init()
            self._font = pygame.font.SysFont(None, 24)
            self._screen_width, self._screen_height = pygame.display.get_surface().get_size()
            if screen is None:
                print("No screen provided. Initializing default pygame screen.")
                self._screen = pygame.display.set_mode((800, 600))
            else:
                self._screen = screen
            
        
    # This function plays the game of War
    # war_face_down_cards is the number of cards to play face down in a tie
    # see_text is a boolean that determines if the game should print the text
    # user_input is a boolean that determines if the game should ask for user input i.e a CPU vs CPU game
    def play(self):
        player_amount = 0
        if self._user_input:
            while True:
                try:
                    player_amount = int(input("Enter the number of players (1-2): "))
                except TypeError:
                    print("Invalid input. Please enter a number.")
                else:
                    if  player_amount < 1 or player_amount > 2:
                        print("Invalid input. Please enter a number between 1 and 2.")
                    else:
                        break
            
      
        player1, player2 = self._set_player_names(player_amount)
        
        for _ in range(26):
            player1.list.append(self._deck.deal())
            player2.list.append(self._deck.deal())
            
        while player1.get_list_size() > 0 and player2.get_list_size() > 0:
            self._round_count += 1

            if self._see_graphics:
                self._screen.fill((255, 255, 255))
                
                player1_name_text = self._font.render(player1.name, True, (0, 0, 0))
                player1_deck_size_text = self._font.render(f"Deck size: {player1.get_list_size()}", True, (0, 0, 0))
                
                player2_name_text = self._font.render(player2.name, True, (0, 0, 0))
                player2_deck_size_text = self._font.render(f"Deck size: {player2.get_list_size()}", True, (0, 0, 0))
                
                player1_name_rect = player1_name_text.get_rect(center=(player1_deck_size_text.get_width(), self._screen_height - player1_name_text.get_height()))
                player1_deck_size_rect = player1_deck_size_text.get_rect(center=(player1_deck_size_text.get_width(), self._screen_height - player1_name_text.get_height() - player1_deck_size_text.get_height() - 20))

                player2_name_rect = player2_name_text.get_rect(center=(self._screen_width - player2_deck_size_text.get_width(), player2_name_text.get_height()))
                player2_deck_size_rect = player2_deck_size_text.get_rect(center=(self._screen_width - player2_deck_size_text.get_width(), player2_name_text.get_height() + player2_deck_size_text.get_height() + 20))

                self._screen.blit(player1_name_text, player1_name_rect)
                self._screen.blit(player1_deck_size_text, player1_deck_size_rect)
                self._screen.blit(player2_name_text, player2_name_rect)
                self._screen.blit(player2_deck_size_text, player2_deck_size_rect)

            if self._user_input:
                match player_amount:
                    case 1:
                        card1 = self._play_card(player1)
                        card2 = self._play_card(player2, user = False)
                    
                    case 2:
                        card1 = self._play_card(player1)
                        card2 = self._play_card(player2)
                    case _:
                        print("Invalid number of players. Defaulting to 1 player.")
                        card1 = self._play_card(player1)
                        card2 = self._play_card(player2, user = False)
            else:
                card1 = self._play_card(player1, user = False)
                card2 = self._play_card(player2, user = False)
            

            if card1.get_rank().value > card2.get_rank().value:
                self._player_wins_stack(player1, card1, card2)
            
            elif card1.get_rank().value < card2.get_rank().value:
                self._player_wins_stack(player2, card1, card2)
            
            else:
                if player1.get_list_size() <= self._war_face_down_cards:
                    return f"{player1.name} dose not have enough cards for WAR! {player2.name} wins the game after {self._round_count} rounds!!"
                elif player2.get_list_size() <= self._war_face_down_cards:
                    return f"{player2.name} dose not have enough cards for WAR! {player1.name} wins the game after {self._round_count} rounds!!"
                
                if self._see_text:
                    print("It's a tie! WAR!")
                self._tie_stack.append(card1)
                self._tie_stack.append(card2)
                
                for _ in range(self._war_face_down_cards):
                    self._tie_stack.append(player1.list.pop())
                    self._tie_stack.append(player2.list.pop())
        
        if player1.get_list_size() == 0:
            print(f"{player1.name} is out of cards! {player2.name} wins the game after {self._round_count} rounds!")
        else:
            print(f"{player2.name} is out of cards! {player1.name} wins the game after {self._round_count} rounds!")
        
    # This function sets the player names based on the number of players
    # 0 is 2 computer players
    def _set_player_names(self, player_amount):
        match player_amount:
                case 0:
                    player1_name = "Computer1"
                    player2_name = "Computer2"
                    player1 = Player(player1_name, player_number=1)
                    player2 = Player(player2_name, player_number=2)
                case 1:
                    player1_name = input("Enter player 1 name: ")
                    player2_name = "Computer"
                    player1 = Player(player1_name, player_number=1)
                    player2 = Player(player2_name, player_number=2)
                case 2:
                    player1_name = input("Enter player 1 name: ")
                    player2_name = input("Enter player 2 name: ")
                    player1 = Player(player1_name, player_number=1)
                    player2 = Player(player2_name, player_number=2)
                case _:
                    print("Invalid number of players. Defaulting to 1 player.")
                    player1_name = input("Enter player 1 name: ")
                    player2_name = "Computer"
                    player1 = Player(player1_name, player_number=1)
                    player2 = Player(player2_name, player_number=2)
        return player1, player2
    
    # This function plays the next card for the player
    # If user is True, it will ask for user input to continue
    def _play_card(self, player: Player, user = True)  -> Card:
        if user:
            if self._see_graphics:
                print(f"play next card {player.name}? (press enter to continue.)")
                loop = True
                while loop:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            print(f"{player.name} quit the game after {self._round_count} rounds!")
                            quit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                                loop = False
            else:
                player_input = input(f"play next card {player.name}? (press enter to continue. type 'exit' or 'e' to quit) ")
                if player_input.lower() == "exit" or player_input.lower() == "e":
                    print(f"{player.name} quit the game after {self._round_count} rounds!")
                    quit()
                        
        card = player.list.pop()
                        
        if self._see_text:
            print(f"{player.name} plays {card.rank.name} of {card.suit.name}")
            
            if self._see_graphics:
                screen_width, screen_height = pygame.display.get_surface().get_size()
                card_image = pygame.image.load(card.get_image_path()).convert_alpha()
                card_image = pygame.transform.scale(card_image, (screen_width/4, screen_height/4)) 
                
                if card_image:
                    if player.get_player_number() == 1:
                        self._screen.blit(card_image, (screen_width/2 - card_image.get_width()/2, screen_height - card_image.get_height()))
                    else:
                        self._screen.blit(card_image, (screen_width/2 - card_image.get_width()/2, 0)) 
                
                pygame.display.flip()  
        
        return card
     
    # This function handles the winning player and adds the cards to their stack
    def _player_wins_stack(self, player, card1, card2):
        if self._see_text:
            print(f"{player.name} wins this round")
        
        player.list.insert(0, card1)
        player.list.insert(0, card2)
        
        if len(self._tie_stack) > 0:
            if self._see_text:
                print(f"and {player.name} wins the WAR! The stack of {len(self._tie_stack)} cards is yours!!")
            for card in self._tie_stack:
                player.list.insert(0, card)
            self._tie_stack.clear()

                        
    

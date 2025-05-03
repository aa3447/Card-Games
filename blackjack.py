from deck import Deck
from genericPlayer import Player
from math import floor


class BlackJack:
    def __init__(self, max_bet = 50, starting_chips = 100, dealer_hits_soft_17 = False):
        self._deck = Deck()
        self._deck.shuffle()
        self._max_bet = max_bet
        self._starting_chips = starting_chips
        self._dealer_blackjack = False
        self._player_blackjack = False
        self._dealer_bust = False
        self._dealer_hits_soft_17 = dealer_hits_soft_17
        
    def play(self):
        # PreGame setup
        player_amount = 0
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
        players = self._setup_players(player_amount,self._starting_chips)
        dealer = players.pop()
        
        # Game loop
        while True:

            player_input = input(f"Do you want to quit? (press enter to continue. type 'exit' or 'e' to quit) ")
        
            if player_input.lower() == "exit" or player_input.lower() == "e":
                 print(f"{player.name} has quit the game.")
                 quit()

            # Resetting game state
            self._reset(players, dealer)
            
            if self._deck.get_cards_remaining() < 20:
                print("Deck is running low. Refilling deck.")
                self._deck.refill()
                self._deck.shuffle()

            # Placing bets
            self._place_bets(players, player_amount, self._max_bet)
            
            # Dealing initial cards
            print("Dealing intial cards")
            for x in range(player_amount):
                players[x].add_cards(self._deck.multi_deal(2))
            
            dealer_first_card = self._deck.deal()
            dealer.add_card(dealer_first_card)
            hole_card = self._deck.deal()
            dealer.add_card(hole_card)
            print("Dealing complete")

            # Checking for blackjack for dealer and players
            initial_player_scores = []
            for player in players:
                initial_player_scores.append(self._score_hand(player)[0])

            if dealer_first_card.get_rank().value == 1 or dealer_first_card.get_rank().value > 10:
                if self._score_hand(dealer)[0] == 21:
                    print(f"Dealer has blackjack! {dealer.name} wins!")
                    for x in range(player_amount):
                        currrent_player = players[x]
                        if initial_player_scores[x] != 21:
                            currrent_player.set_chips(currrent_player.get_chips() - currrent_player.get_bet())
                            print(f"{currrent_player.name} has {currrent_player.get_chips()} chips left.")
                    self._dealer_blackjack = True

            if not self._dealer_blackjack:
                for x in range(player_amount):
                    currrent_player = players[x]
                    if initial_player_scores[x] == 21:
                        print(f"{currrent_player.name} has blackjack! {currrent_player.name} wins!")
                        currrent_player.set_chips(currrent_player.get_chips() + floor((currrent_player.get_bet() * 1.5)))
                        print(f"{currrent_player.name} has {currrent_player.get_chips()} chips left.")
                        if not self._player_blackjack:
                            self._player_blackjack = True
                
                if not self._player_blackjack:
                    # Removing the hole card from the dealer's hand
                    dealer.list.pop()
                    
                    print(f"Dealer's hand is {dealer.print_hand()}")

                    # Player's turn
                    for player in players:
                        while True:
                            print(f"{player.name}'s hand is {player.print_hand()}")
                            try:
                                action = input(f"{player.name}, do you want to hit (h), stand (s), or show dealers hand (d)?").lower()
                            except TypeError:
                                print("Invalid input. Please enter 'h' or 's'.")
                            
                            if action == 'h':
                                player.add_card(self._deck.deal())
                                print(f"{player.name} hits and gets {player.get_cards()[-1]}")
                                
                                if self._score_hand(player)[0] > 21:
                                    print(f"{player.name} busts! {dealer.name} wins!")
                                    player.set_chips(player.get_chips() - player.get_bet())
                                    
                                    if player.get_chips() <= 0:
                                        print(f"{player.name} is out of chips!")
                                        players.remove(player)
                                        player_amount -= 1
                                        
                                        if player_amount == 0:
                                            print("Game over! All players are out of chips!")
                                            return
                                    player.set_busted(True)
                                    break
                            
                            elif action == 's':
                                break
                            
                            elif action == 'd':
                                print(f"Dealer's hand is {dealer.print_hand()}")
                            
                            else:
                                print("Invalid input. Please enter 'h' or 's'.")
                    

                    # Dealer's turn
                    print(f"{dealer.name}'s turn")
                    dealer.add_card(hole_card)
                    print(f"Dealer's hand is {dealer.print_hand()}")
                    dealer_score = self._score_hand(dealer)
                    while dealer_score[0] < 17:
                        dealer.add_card(self._deck.deal())
                        print(f"{dealer.name} hits and gets {dealer.get_cards()[-1]}")
                        dealer_score[0] = self._score_hand(dealer)[0]
                    
                    if self._dealer_hits_soft_17 and dealer_score[0] == 17 and dealer_score[1] > 0 and dealer.get_list_size() == 2:
                        dealer.add_card(self._deck.deal())
                        print(f"{dealer.name} hits and gets {dealer.get_cards()[-1]}")
                        dealer_score = self._score_hand(dealer)[0]    
                    
                    if dealer_score[0] > 21:
                        print(f"{dealer.name} busts! Players win!")
                        for player in players:
                            player.set_chips(player.get_chips() + player.get_bet())
                            print(f"{player.name} has {player.get_chips()} chips left.")
                        self._dealer_bust = True
                    
                    # Determining winner
                    if not self._dealer_bust:
                        for x in range(player_amount):
                            currrent_player = players[x]
                            player_score = self._score_hand(currrent_player)[0]
                            if currrent_player.has_busted():
                                currrent_player.set_busted(False)
                                print(f"{currrent_player.name} busted! {dealer.name} wins!")
                            elif player_score > dealer_score[0]:
                                print(f"{currrent_player.name} wins!")
                                currrent_player.set_chips(currrent_player.get_chips() + currrent_player.get_bet())
                            elif player_score < dealer_score[0]:
                                print(f"{currrent_player.name} loses!")
                                currrent_player.set_chips(currrent_player.get_chips() - currrent_player.get_bet())
                            else:
                                print(f"{currrent_player.name} ties with the dealer!")
    
    # This function sets up the players for the game.
    # It returns a list of Player objects with the Dealer being the last player
    def _setup_players(self, player_amount, chips):
        players = []
        match player_amount:
                case 1:
                    player1_name = input("Enter player 1 name: ")
                    dealer_name = "Dealer"
                    players.append(Player(player1_name))
                    players.append(Player(dealer_name))
                case 2:
                    player1_name = input("Enter player 1 name: ")
                    player2_name = input("Enter player 2 name: ")
                    dealer_name = "Dealer"
                    players.append(Player(player1_name))
                    players.append(Player(player2_name))
                    players.append(Player(dealer_name))
                case _:
                    print("Invalid number of players. Defaulting to 1 player.")
                    player1_name = input("Enter player 1 name: ")
                    dealer_name = "Dealer"
                    players.append(Player(player1_name))
                    players.append(Player(dealer_name))

        for player in players:
            player.set_chips(chips)
            
        return players
    
    def _score_hand(self, player):
        score = 0
        ace_count = 0
        for card in player.list:
            if card.get_rank().value > 10:
                score += 10
            elif card.get_rank().value == 1:
                ace_count += 1
            else:
                score += card.get_rank().value
        
        for _ in range(ace_count):
            if score + 11 > 21:
                score += 1
            else:
                score += 11
        
        return [score , ace_count]

    def _reset(self, players, dealer):
        self._dealer_blackjack = False
        self._player_blackjack = False
        self._dealer_bust = False
        for player in players:
            player.list = []
            player.set_bet(0)
            player.set_busted(False)
        dealer.list = []

    def _place_bets(self, players, player_amount, max_bet):
        for x in range(player_amount):
            while True:
                print(f"{players[x].name} has {players[x].get_chips()} chips.")
                try:
                    players[x].set_bet(int(input(f"{players[x].name} place your bet (1-{max_bet}):")))
                except TypeError:
                    print("Invalid input. Please enter a number.")
                except ValueError as v:
                    print(v)
                else:
                    if players[x].get_bet() < 1 or players[x].get_bet() > max_bet:
                        print("Invalid input. Please enter a number between 1 and 50.")
                    elif players[x].get_bet() > players[x].get_chips():
                        print("Invalid input. Bet exceeds available chips.")
                    else:
                        break

    def _set_ace_value(self, ace, value):
        ace.set_value(value)
        return ace
            
        
from deck import Deck
from genericPlayer import Player


class BlackJack:
    def __init__(self):
        self._deck = Deck()
        self._deck.shuffle()
        
    def play(self):
        player_amount = 0
        while True:
            try:
                player_amount = int(input("Enter the number of players (1-4): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
            else:
                if  player_amount < 1 or player_amount > 4:
                    print("Invalid input. Please enter a number between 1 and 4.")
                else:
                    break
        
        players = self._setup_players(player_amount)
        dealer = players.pop()
      
        for x in range(player_amount):
            while True:
                try:
                    players[x].bet = int(input(f"{players[x].name} place your bet (1-50):"))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                else:
                    if  players[x].bet < 1 or players[x].bet > 50:
                        print("Invalid input. Please enter a number between 1 and 50.")
                    else:
                        break
        
        print("Dealing intial cards")
        for x in range(player_amount):
            players[x].list.append(self._deck.multi_deal(2))
        dealer.list.append(self._deck.deal())
        hole_card = self.deck.deal()
        dealer.list.append(hole_card)
        print("Dealing complete")
        if self._score_hand(dealer) == 21:
            print(f"Dealer has blackjack! {dealer.name} wins!")
            return
        dealer.list.pop()
        print(f"Dealer's hand is {dealer.show_cards()}")

    # This function sets up the players for the game.
    # It returns a list of Player objects with the Dealer being the last player
    def _setup_players(self, player_amount, chips = 100):
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
        
        return score

    def _set_ace_value(self, ace, value):
        ace.set_value(value)
        return ace
            
        
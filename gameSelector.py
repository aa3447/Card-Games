from war import War
from blackjack import BlackJack
from solitaire import Solitaire

class GameSelector:
    def __init__(self, user_screen=None):
        self.user_screen = user_screen
        self._games = {
            "War": War,
            "Blackjack": BlackJack,
            "Solitaire": Solitaire
        }

    def select_game(self):
        print("Select a game to play:")
        for i, game in enumerate(self._games.keys()):
            print(f"{i}. {game}")

        choice = int(input("Enter the number of your choice: "))
        game_name = list(self._games.keys())[choice]
        return self._game_setup(game_name)
    

    def _game_setup(self, game_name):
        use_default = 1
        while True:
            try:
                use_default = int(input("Use default settings? (1 for yes, 0 for no): "))
            except TypeError:
                print("Invalid input. Please enter 1 or 0.")
            else:
                if use_default not in [0, 1]:
                    print("Invalid input. Please enter 1 or 0.")
                else:
                    break

        match game_name:
            case "War":
                if use_default == 1:
                    return War()
                while True:
                    try:
                        w_face_down_cards = int(input("Enter the number of face down cards for war (Default is 1): "))
                    except TypeError:
                        print("Invalid input. Please enter a number.")
                    else:
                        if w_face_down_cards < 1:
                            print("Invalid input. Please enter a number greater than 0.")
                        else:
                            break
                
                while True:
                    try:
                        see_text = int(input("See text? (1 for yes, 0 for no) (Default is yes): "))
                    except TypeError:
                        print("Invalid input. Please enter 1 or 0.")
                    else:
                        if see_text not in [0, 1]:
                            print("Invalid input. Please enter 1 or 0.")
                        else:
                            break
                
                if see_text == 0:
                    see_text_bool = False
                else:
                    see_text_bool  = True

                while True:
                    try:
                        user_input = int(input("User input? (1 for yes, 0 for no) (Default is no): "))
                    except TypeError:
                        print("Invalid input. Please enter 1 or 0.")
                    else:
                        if user_input not in [0, 1]:
                            print("Invalid input. Please enter 1 or 0.")
                        else:
                            break

                if user_input == 1:
                    user_input_bool = True
                else:
                    user_input_bool = False
                    
                return War(war_face_down_cards = w_face_down_cards , see_text = see_text_bool , user_input = user_input_bool, see_graphics = True, screen = self.user_screen)
            
            case "Blackjack":
                if use_default == 1:
                    return BlackJack()
                
                while True:
                    try:
                        max_bet_setup = int(input("Enter the maximum bet (Default is 50): "))
                    except TypeError:
                        print("Invalid input. Please enter a number.")
                    else:
                        if max_bet_setup < 1:
                            print("Invalid input. Please enter a number greater than 0.")
                        else:
                            break
                while True:
                    try:
                        starting_chips_setup = int(input("Enter the starting chips (Default is 100): "))
                    except TypeError:
                        print("Invalid input. Please enter a number.")
                    else:
                        if starting_chips_setup < 1:
                            print("Invalid input. Please enter a number greater than 0.")
                        else:
                            break
                while True:
                    try:
                        d_hits_soft_17 = int(input("Dealer hits on soft 17? (1 for yes, 0 for no) (Default is no): "))
                    except TypeError:
                        print("Invalid input. Please enter 1 or 0.")
                    else:
                        if d_hits_soft_17 not in [0, 1]:
                            print("Invalid input. Please enter 1 or 0.")
                        else:
                            break
                
                if d_hits_soft_17 == 1:
                    dealer_hits_soft_17_bool = True
                else:
                    dealer_hits_soft_17_bool = False

                return BlackJack(max_bet = max_bet_setup ,starting_chips = starting_chips_setup, dealer_hits_soft_17 = dealer_hits_soft_17_bool)
            
            case "Solitaire":
                return Solitaire()
            
            case _:
                raise ValueError("Invalid game name")
from deck import Deck
from war import War
from blackjack import BlackJack

def main():
    war = War()
    blackjack = BlackJack()
    #print(war.play(war_face_down_cards = 3, user_input=True))
    blackjack.play()

if __name__ == "__main__":
    main()
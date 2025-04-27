from deck import Deck
from war import War

def main():
    war = War()
    print(war.play(war_face_down_cards = 3))

if __name__ == "__main__":
    main()
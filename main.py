from deck import Deck

def main():
    deck = Deck()
    deck.shuffle()
    card = deck.deal()
    print(f"Card dealt: {card.rank.name} of {card.suit.name}")

if __name__ == "__main__":
    main()
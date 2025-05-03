from gameSelector import GameSelector

def main():
   game = GameSelector().select_game()
   game.play()

if __name__ == "__main__":
    main()
from game import Game
from props_and_colours import *
from player import player_list, setup

game = Game(player_list)

def main():    
    setup()
    game.game_turn()

if __name__ == "__main__":
    main()
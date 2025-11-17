import random
from props_and_colours import END, GREEN, RED

player_list = []

class Player:
    def __init__(self, name, colour_code='\033[0m'):
        self.name = name
        self.colour_code = colour_code
        self.bank = 1500
        self.position = 0
        self.n = 0
        self.history = {}
        self.bought = []
        self.is_bankrupt = False
        self.skip_rent = False
        self.skip_go = False
        self.in_jail = False
        self.jail_card_chest = False
        self.jail_card_chance = False
        self.jail_count = 0

    def __str__(self):
        return f'{self.colour_code}{self.name}{END}'
    
    def __repr__(self):
        return f'{self.colour_code}{self.name}{END}'

    def check_balance(self):
        print(f'{self} Balance: {GREEN}{self.bank}{END}')

    def add_money(self, earnings):
        self.bank += earnings
        return self.bank

    def lose_money(self, losings):
        self.bank -= losings
        return self.bank
    
    def roll(self, throws=1):
        if throws == 1:
            rolled_num = random.randint(1, 6)
            self.rolled = rolled_num
            self.n += 1
            self.history[self.n] = rolled_num
            return rolled_num
        elif throws > 1:
            rolled_nums = random.choices(range(1, 7), k=throws)
            self.rolled = rolled_nums
            self.n += 1
            self.history[self.n] = sum(rolled_nums)
            return sum(rolled_nums)
           
    def roll_history(self):
        for i, j in self.history.items():
            print(f'Roll {i}: {j}')

    def current_roll(self):
        return (self.history[self.n])
   
def setup():
    colours = ['\033[38;5;42m', '\033[38;5;197m', '\033[38;5;33m', '\033[38;5;227m', '\033[38;5;209m', '\033[38;5;92m']
    num_of_players = input('How many players?')
    if int(num_of_players) == 1:
        print('Loser! Get some friends.')
        return
    elif int(num_of_players) > 6:
        print('Too mnay players')
        return
    else:
        for i in range(1, int(num_of_players) + 1):
            player_name = input(f'Enter name for player{i}')
            player_list.append(Player(player_name, colours[i - 1]))
        return player_list
    
def lookup_create():
    lookup = {}
    for i in range(len(player_list)):
        lookup[player_list[i].name] = player_list[i]
    return lookup

    

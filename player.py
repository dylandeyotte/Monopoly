import random
from props_and_colours import END, GREEN, RED

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
        return f'{self.colour_code}{self.name}\033[0m'
    
    def __repr__(self):
        return f'{self.colour_code}{self.name}\033[0m'

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
    
player1 = Player('Vi', '\033[38;5;197m')
player2 = Player('Caitlyn', '\033[38;5;33m')
player3 = Player('Jinx', '\033[38;5;117m')
player_list = [player1, player2, player3]
lookup = {'Vi': player1, 'Caitlyn': player2, 'Jinx': player3}

    
    
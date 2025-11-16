from props_and_colours import END, GREEN, RED
from player import player_list, lookup
from card import Card

class Game:
    def __init__(self, players):
        self.players = players
        self.card = Card()
        self.bought = {}
        self.board = ['GO', 'Mediterranean Avenue', 'Community Chest', 'Baltic Avenue', 'Income Tax', 'Reading Railroad', 'Oriental Avenue', 'Chance', 'Vermont Avenue', 'Connecticut Avenue',
'Jail / Just Visiting', 'St. Charles Place', 'Electric Company', 'States Avenue', 'Virginia Avenue', 'Pennsylvania Railroad', 'St. James Place', 'Community Chest', 'Tennessee Avenue', 'New York Avenue',
'Free Parking', 'Kentucky Avenue', 'Chance', 'Indiana Avenue', 'Illinois Avenue', 'B&O Railroad', 'Atlantic Avenue', 'Ventnor Avenue', 'Water Works', 'Marvin Gardens',
'Go to Jail', 'Pacific Avenue', 'North Carolina Avenue', 'Community Chest', 'Pennsylvania Avenue', 'Short Line Railroad', 'Chance', 'Park Place', 'Luxury Tax', 'Boardwalk']
        self.end_game = False
        self.prices = {
    'Mediterranean Avenue': 60,
    'Baltic Avenue': 60,
    'Oriental Avenue': 100,
    'Vermont Avenue': 100,
    'Connecticut Avenue': 120,
    'St. Charles Place': 140,
    'States Avenue': 140,
    'Virginia Avenue': 160,
    'St. James Place': 180,
    'Tennessee Avenue': 180,
    'New York Avenue': 200,
    'Kentucky Avenue': 220,
    'Indiana Avenue': 220,
    'Illinois Avenue': 240,
    'Atlantic Avenue': 260,
    'Ventnor Avenue': 260,
    'Marvin Gardens': 280,
    'Pacific Avenue': 300,
    'North Carolina Avenue': 300,
    'Pennsylvania Avenue': 320,
    'Park Place': 350,
    'Boardwalk': 400,
    'Reading Railroad': 200,
    'Pennsylvania Railroad': 200,
    'B&O Railroad': 200,
    'Short Line Railroad': 200,
    'Electric Company': 150,
    'Water Works': 150,
}
        self.rent = {
    'Mediterranean Avenue': [2, 10, 30, 90, 160, 250],
    'Baltic Avenue': [4, 20, 60, 180, 320, 450],
    'Oriental Avenue': [6, 30, 90, 270, 400, 550],
    'Vermont Avenue': [6, 30, 90, 270, 400, 550],
    'Connecticut Avenue': [8, 40, 100, 300, 450, 600],
    'St. Charles Place': [10, 50, 150, 450, 625, 750],
    'States Avenue': [10, 50, 150, 450, 625, 750],
    'Virginia Avenue': [12, 60, 180, 500, 700, 900],
    'St. James Place': [14, 70, 200, 550, 750, 950],
    'Tennessee Avenue': [14, 70, 200, 550, 750, 950],
    'New York Avenue': [16, 80, 220, 600, 800, 1000],
    'Kentucky Avenue': [18, 90, 250, 700, 875, 1050],
    'Indiana Avenue': [18, 90, 250, 700, 875, 1050],
    'Illinois Avenue': [20, 100, 300, 750, 925, 1100],
    'Atlantic Avenue': [22, 110, 330, 800, 975, 1150],
    'Ventnor Avenue': [22, 110, 330, 800, 975, 1150],
    'Marvin Gardens': [24, 120, 360, 850, 1025, 1200],
    'Pacific Avenue': [26, 130, 390, 900, 1100, 1275],
    'North Carolina Avenue': [26, 130, 390, 900, 1100, 1275],
    'Pennsylvania Avenue': [28, 150, 450, 1000, 1200, 1400],
    'Park Place': [35, 175, 500, 1100, 1300, 1500],
    'Boardwalk': [50, 200, 600, 1400, 1700, 2000],
    'Reading Railroad': [25, 50, 100, 200],
    'Pennsylvania Railroad': [25, 50, 100, 200],
    'B&O Railroad': [25, 50, 100, 200],
    'Short Line Railroad': [25, 50, 100, 200],
    'Electric Company': [0],
    'Water Works': [0]

}
        self.house = {
    'Mediterranean Avenue': [50, 0],
    'Baltic Avenue': [50, 0],
    'Oriental Avenue': [50, 0],
    'Vermont Avenue': [50, 0],
    'Connecticut Avenue': [50, 0],
    'St. Charles Place': [100, 0],
    'States Avenue': [100, 0],
    'Virginia Avenue': [100, 0],
    'St. James Place': [100, 0],
    'Tennessee Avenue': [100, 0],
    'New York Avenue': [100, 0],
    'Kentucky Avenue': [150, 0],
    'Indiana Avenue': [150, 0],
    'Illinois Avenue': [150, 0],
    'Atlantic Avenue': [150, 0],
    'Ventnor Avenue': [150, 0],
    'Marvin Gardens': [150, 0],
    'Pacific Avenue': [200, 0],
    'North Carolina Avenue': [200, 0],
    'Pennsylvania Avenue': [200, 0],
    'Park Place': [200, 0],
    'Boardwalk': [200, 0],
    'Reading Railroad': [0, 0],
    'Pennsylvania Railroad': [0, 0],
    'B&O Railroad': [0, 0],
    'Short Line Railroad': [0, 0],
    'Electric Company': [0, 0],
    'Water Works': [0, 0]
    
}
        self.colours = {
    '\033[38;5;130m': ['Mediterranean Avenue', 'Baltic Avenue'],                            #Brown
    '\033[38;5;111m': ['Oriental Avenue', 'Vermont Avenue', 'Connecticut Avenue'],      #Light Blue
    '\033[38;5;200m': ['St. Charles Place', 'States Avenue', 'Virginia Avenue'],            #Magenta
    '\033[38;5;208m': ['St. James Place', 'Tennessee Avenue', 'New York Avenue'],       #Orange
    '\033[38;5;196m': ['Kentucky Avenue', 'Indiana Avenue', 'Illinois Avenue'],             #Red
    '\033[38;5;190m': ['Atlantic Avenue', 'Ventnor Avenue', 'Marvin Gardens'],          #Yellow
    '\033[38;5;34m': ['Pacific Avenue', 'North Carolina Avenue', 'Pennsylvania Avenue'],    #Green
    '\033[38;5;21m': ['Park Place', 'Boardwalk'],                                       #Dark Blue
    '\033[38;5;245m': ['Reading Railroad', 'Pennsylvania Railroad', 'B&O Railroad', 'Short Line Railroad'],     #Grey
    '\033[38;5;225m': ['Electric Company', 'Water Works']                               #Pink
    
}
        self.house_colours = {
    'Brown': ['Mediterranean Avenue', 'Baltic Avenue'],                           
    'Light Blue': ['Oriental Avenue', 'Vermont Avenue', 'Connecticut Avenue'],     
    'Magenta': ['St. Charles Place', 'States Avenue', 'Virginia Avenue'],            
    'Orange': ['St. James Place', 'Tennessee Avenue', 'New York Avenue'],      
    'Red': ['Kentucky Avenue', 'Indiana Avenue', 'Illinois Avenue'],             
    'Yellow': ['Atlantic Avenue', 'Ventnor Avenue', 'Marvin Gardens'],          
    'Green': ['Pacific Avenue', 'North Carolina Avenue', 'Pennsylvania Avenue'],    
    'Dark Blue': ['Park Place', 'Boardwalk']                                       
    
}
    def colour(self,property):
        font_colour = next((k for k, v in self.colours.items() if property in v), None)
        return f'{font_colour}{property}{END}'

    def check_space(self, player):

        if player.skip_go == False:
            self.go_check(player)
        player.skip_go = False
        
        if self.board[player.position] in self.rent:
            print(f'{player} landed on {self.colour(self.board[player.position])}')
        else:
            print(f'{player} landed on {(self.board[player.position])}')

        if self.board[player.position] == 'Go to Jail':  
            self.go_to_jail(player)
            return
        elif self.board[player.position] == 'Chance':
            self.card.draw_chance(self, player)
            return
        elif self.board[player.position] == 'Community Chest':
            self.card.draw_chest(self, player)
            return
        elif self.board[player.position] == 'Luxury Tax':  
            print(f'Luxury Tax! {RED}-100{END}')
            if player.bank > 100:
                player.lose_money(100)
                player.check_balance()
            else:
                self.erase_player(player)              
        elif self.board[player.position] == 'Income Tax':    
            print(f'Income Tax! {RED}-200{END}')
            if player.bank > 200:
                player.lose_money(200)
                player.check_balance()
            else: 
                self.erase_player(player)        
        elif self.board[player.position] in self.bought: 
            if player.skip_rent == False:
                self.pay_rent(player)
            player.skip_rent = False
        return self.board[player.position]
    
    def go_check(self, player, position=None, reverse=False):
        prev_position = player.position

        if position is None:
            roll_total = player.history[player.n]
            new_position = (prev_position + roll_total) % 40
        else:
            new_position = position

        if new_position < prev_position and reverse == False:
            print(f'{player} Passed GO! {GREEN}+200{END}')
            player.add_money(200)

        player.position = new_position

    
    def go_to_jail(self, player):
        player.position = 10 
        player.in_jail = True  
        print(f'{player} is in jail') 
        return
    
    def erase_player(self, player):
        player.bank = 0
        player.bought.clear()
        props = [k for k, v in self.bought.items() if v == player]
        for k in props:
            del self.bought[k]
        player.is_bankrupt = True
        print(f'{player} has gone BANKRUPT!!!')
        player_list.remove(player)
                                                  
    def buy_property(self, player):
        self.property_name = self.board[player.position]
        if self.bought.get(self.property_name) == player:
            print(f'{self.colour(self.property_name)} already owned')
            return
        elif self.property_name in self.prices:
            if player.bank < self.prices[self.property_name]:
                print('Cannot afford')
                return
            self.railroads = self.colours['\033[38;5;245m']
            if self.property_name in self.railroads:
                if any(roads in player.bought for roads in self.railroads):
                    self.owned_roads = {roads for roads in self.railroads if roads in player.bought or roads == self.property_name}
                    self.count = len(self.owned_roads)
                    for road in self.owned_roads:
                        self.house[road][1] = self.count - 1
            player.lose_money(self.prices[self.property_name])
            print(f'{player} bought {self.colour(self.property_name)} for {RED}{self.prices[self.property_name]}{END}')
            player.check_balance()
            self.prices.pop(self.property_name)
            self.bought[self.property_name] = player
            player.bought.append(self.property_name)
        return
    
    def trade(self, player1, player2, prop1, prop2):
        p2 = lookup.get(player2)
        if prop1 not in player1.bought or prop2 not in p2.bought:
            print(f'Invalid transaction')
        player1.bought.remove(prop1)
        p2.bought.append(prop1)
        p2.bought.remove(prop2)
        player1.bought.append(prop2)
        self.bought[prop1] = p2
        self.bought[prop2] = player1
        print(f'{player1} sent {self.colour(prop1)} to {p2} for {self.colour(prop2)}')
    
    def buy_house(self, player, colour):
            property_list = self.house_colours[colour]
            if set(property_list).issubset(player.bought):
                if player.bank >= (self.house[property_list[0]])[0] * len(property_list):
                    for property in self.house:
                        if property in property_list:
                            if self.house[property][1] == 5:
                                print('Hotel already purchased')
                                return
                            self.house[property][1] += 1
                    if len(property_list) == 2:
                        print(f'{player} bought houses on {self.colour(property_list[0])} and {self.colour(property_list[1])}')
                    elif len(property_list) == 3:
                        print(f'{player} bought houses on {self.colour(property_list[0])}, {self.colour(property_list[1])}, and {self.colour(property_list[2])}')
                    player.lose_money((self.house[property_list[0]])[0] * len(property_list))
                    player.check_balance()
                else:
                    print('Cannot afford')
            else:
                print(f'{player} does not own monopoly')
   
    def pay_rent(self, player): 
        self.property_name = self.board[player.position] 
        if self.property_name in self.bought:
            owner = self.bought[self.property_name]
            if owner != player:
                if self.property_name == 'Electric Company' or self.property_name == 'Water Works':
                    if self.bought.get('Electric Company') and self.bought.get('Water Works') and self.bought['Electric Company'] == self.bought['Water Works']:
                        mult = 10
                    else:                                                                               
                        mult = 4
                    if player.bank < player.current_roll()*mult:
                        self.erase_player(player)
                        return
                    print(f'{player} owes {RED}{player.current_roll()*mult}{END} to {owner}')
                    player.lose_money(player.current_roll()*mult)
                    owner.add_money(player.current_roll()*mult)
                else:
                    self.house_num = self.house[self.property_name][1]
                    if player.bank < self.rent[self.property_name][self.house_num]:
                        self.erase_player(player)
                        return
                    print(f'{player} owes {RED}{self.rent[self.property_name][self.house_num]}{END} to {owner}')
                    player.lose_money(self.rent[self.property_name][self.house_num])
                    owner.add_money(self.rent[self.property_name][self.house_num])
                player.check_balance()
                owner.check_balance()

    def print_dict(self):
        for player in player_list:
            for prop in player.bought:
                print(f'{player} - {self.colour(prop)}')      
    
    def rage_quit(self, player):
        self.erase_player(player)
        print(f'All mortal possessions have been forfeited. {player} is a big baby.')

    def return_card(self, deck):
        if deck == 'chance':
            self.card.shuffled_chance.append(self.card.jail_card_chance)
        elif deck =='chest':
            self.card.shuffled_chest.append(self.card.jail_card_chest)







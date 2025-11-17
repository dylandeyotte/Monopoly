from card import Card
from props_and_colours import *
from player import player_list, lookup_create

class Game:
    def __init__(self, players):
        self.players = players
        self.card = Card()
        self.bought = {} 
        self.end_game = False
                                
    def colour(self,property):
        font_colour = next((k for k, v in colours.items() if property in v), None)
        return f'{font_colour}{property}{END}'

    def check_space(self, player):

        if player.skip_go == False:
            self.go_check(player)
        player.skip_go = False
        
        if board[player.position] in rent:
            print(f'{player} landed on {self.colour(board[player.position])}')
        else:
            print(f'{player} landed on {(board[player.position])}')

        if board[player.position] == 'Go to Jail':  
            self.go_to_jail(player)
            return
        elif board[player.position] == 'Chance':
            self.card.draw_chance(self, player)
            return
        elif board[player.position] == 'Community Chest':
            self.card.draw_chest(self, player)
            return
        elif board[player.position] == 'Luxury Tax':  
            print(f'Luxury Tax! {RED}-100{END}')
            if player.bank > 100:
                player.lose_money(100)
                player.check_balance()
            else:
                self.erase_player(player)              
        elif board[player.position] == 'Income Tax':    
            print(f'Income Tax! {RED}-200{END}')
            if player.bank > 200:
                player.lose_money(200)
                player.check_balance()
            else: 
                self.erase_player(player)        
        elif board[player.position] in self.bought: 
            if player.skip_rent == False:
                self.pay_rent(player)
            player.skip_rent = False
        return board[player.position]
    
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
    
    def rage_quit(self, player):
        self.erase_player(player)
        print(f'All mortal possessions have been forfeited. {player} is a big baby.')
    
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
        property_name = board[player.position]
        if self.bought.get(property_name) == player:
            print(f'{self.colour(property_name)} already owned')
            return
        elif property_name in prices:
            if player.bank < prices[property_name]:
                print('Cannot afford')
                return
            railroads = colours['\033[38;5;245m']
            if property_name in railroads:
                if any(roads in player.bought for roads in railroads):
                    owned_roads = {roads for roads in railroads if roads in player.bought or roads == property_name}
                    count = len(owned_roads)
                    for road in owned_roads:
                        house[road][1] = count - 1
            player.lose_money(prices[property_name])
            print(f'{player} bought {self.colour(property_name)} for {RED}{prices[property_name]}{END}')
            player.check_balance()
            prices.pop(property_name)
            self.bought[property_name] = player
            player.bought.append(property_name)
        return
    
    def trade(self, player1, player2, prop1, prop2):
        lookup = lookup_create()
        p2 = lookup.get(player2)
        player1.bought.remove(prop1)
        p2.bought.append(prop1)
        p2.bought.remove(prop2)
        player1.bought.append(prop2)
        self.bought[prop1] = p2
        self.bought[prop2] = player1
        print(f'{player1} sent {self.colour(prop1)} to {p2} for {self.colour(prop2)}')
    
    def buy_house(self, player, colour):
            property_list = house_colours[colour]
            if set(property_list).issubset(player.bought):
                if player.bank >= (house[property_list[0]])[0] * len(property_list):
                    for property in house:
                        if property in property_list:
                            if house[property][1] == 5:
                                print('Hotel already purchased')
                                return
                            house[property][1] += 1
                    if len(property_list) == 2:
                        print(f'{player} bought houses on {self.colour(property_list[0])} and {self.colour(property_list[1])}')
                    elif len(property_list) == 3:
                        print(f'{player} bought houses on {self.colour(property_list[0])}, {self.colour(property_list[1])}, and {self.colour(property_list[2])}')
                    player.lose_money((house[property_list[0]])[0] * len(property_list))
                    player.check_balance()
                else:
                    print('Cannot afford')
            else:
                print(f'{player} does not own monopoly')
   
    def pay_rent(self, player): 
        property_name = board[player.position] 
        if property_name in self.bought:
            owner = self.bought[property_name]
            if owner != player:
                if property_name == 'Electric Company' or property_name == 'Water Works':
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
                    house_num = house[property_name][1]
                    if player.bank < rent[property_name][house_num]:
                        self.erase_player(player)
                        return
                    print(f'{player} owes {RED}{rent[property_name][house_num]}{END} to {owner}')
                    player.lose_money(rent[property_name][house_num])
                    owner.add_money(rent[property_name][house_num])
                player.check_balance()
                owner.check_balance()

    def print_dict(self):
        for player in player_list:
            for prop in player.bought:
                print(f'{player} - {self.colour(prop)}')      
    
    def return_card(self, deck):
        if deck == 'chance':
            self.card.shuffled_chance.append(self.card.jail_card_chance)
        elif deck =='chest':
            self.card.shuffled_chest.append(self.card.jail_card_chest)
    
    def roll_turn(self, player):
        dice_count = 0
        while dice_count < 3:
            #Jail Check
            player.roll(2)
            if player.in_jail == True:
                if player.rolled[0] != player.rolled[1]:
                    player.jail_count +=1
                    if player.jail_count < 3:
                        print(f'{player} is stuck in Jail')
                        player.history.pop(player.n)
                        break
                    elif player.jail_count == 3:
                        player.in_jail = False
                        player.jail_count = 0
                        print(f'{player} is out of Jail')
                        break
                elif player.rolled[0] == player.rolled[1]:
                    player.in_jail = False
                    print(f'Doubles! {player} is out of Jail')
            #Main Turn
            if player.rolled[0] == player.rolled[1]:
                dice_count += 1
                if dice_count == 3:
                    print(f'{player} rolled doubles three times')
                    self.go_to_jail(player)
                    break 
                print(f'{player} turn {player.n}: {player.history[player.n]} ({player.rolled[0]} and {player.rolled[1]})')
                self.check_space(player)
                property_name = board[player.position]
                if property_name in prices:
                    answer = input(f'Do you want to buy {self.colour(property_name)} for {RED}{prices[property_name]}{END}?')
                    if answer == 'y':
                        self.buy_property(player)
                    elif answer == 'n':
                        continue
            else:  
                print(f'{player} turn {player.n}: {player.history[player.n]} ({player.rolled[0]} and {player.rolled[1]})')
                self.check_space(player)
                property_name = board[player.position]
                if property_name in prices:
                    answer = input(f'Do you want to buy {self.colour(property_name)} for {RED}{prices[property_name]}{END}?')
                    if answer == 'y':
                        self.buy_property(player)
                        break
                    elif answer == 'n':
                        break    
                break
                                
            
    def player_turn(self, player):
        #Bankruptcy Check
        if player.is_bankrupt == True:
            player_list.remove(player)
        if len(player_list) == 1:
            print(f'{player_list[0]} has won the game!')
            self.end_game == True
            return
        #Turn Menu
        while True:
            choice_list = ['1', '2', '3', '4', '5', '6', '7', '8']
            print(f'{player} turn')
            print('1. Roll\n2. Check balance\n3. Check properties\n4. Buy house\n5. Trade property\n6. Get out of jail\n7. Rage quit\n8. End game')
            choice = input('Enter your choice: ')
            if choice not in choice_list:
                print('Please input valid option')
            elif choice == '1':
                self.roll_turn(player)
                break
            elif choice == '2':
                player.check_balance()
            elif choice == '3':
                self.print_dict()
            elif choice == '4':
                colour = input('Which set of properties?')
                self.buy_house(player, colour)
            elif choice == '5':
                lookup = lookup_create()
                tradee = input(f'Which player will {player} trade with?')
                tradee_name = lookup.get(tradee)
                prop1 = input(f'Which property will {player} trade?')
                prop2 = input(f'Which property will {tradee_name} trade?')
                if prop1 in player.bought and prop2 in tradee_name.bought:
                    self.trade(player, tradee, prop1, prop2)
                else:
                    print(f'Invalid transaction')
            elif choice == '6':
                if player.in_jail == False:
                    print(f'{player} is not in jail')
                elif player.jail_card_chance == False and player.jail_card_chest == False:
                    print('No Get Out of Jail cards available')
                elif player.jail_card_chance == True and player.jail_card_chest == False:
                    player.jail_card_chance = False
                    player.in_jail = False
                    self.return_card('chance')
                    print(f'{player} is out of jail')
                elif player.jail_card_chance == False and player.jail_card_chest == True:
                    player.jail_card_chest = False
                    player.in_jail = False
                    self.return_card('chest')
                    print(f'{player} is out of jail')
                elif player.jail_card_chance == True and player.jail_card_chest == True:
                    player.jail_card_chest = False
                    player.in_jail = False
                    self.return_card('chest')
                    print(f'{player} is out of jail')       
            elif choice == '7':
                self.rage_quit(player)
                break
            elif choice == '8':
                end = input('Are you sure?: ')
                if end == 'n':
                    print('Back to the game')
                elif end == 'y':
                    print('Game over')
                    self.end_game = True
                    break
                else:
                    print('Please input valid option')
    
    def game_turn(self):
        while self.end_game == False:
            for player in player_list[:]:
                self.player_turn(player)
                if self.end_game:
                    break
            if len(player_list) == 1:
                break    







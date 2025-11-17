import random
from player import player_list
from props_and_colours import *

class Card:
    def __init__(self):
        self.chance = {
    'Advance to Boardwalk.': lambda player, game: self.change_position(player, 39, game),
    f'Advance to Go (Collect {GREEN}200{END}).': lambda player, game: self.change_position(player, 0, game),
    f'Advance to Illinois Avenue. If you pass Go, collect {GREEN}200{END}.': lambda player, game: self.change_position(player, 24, game),
    f'Advance to St. Charles Place. If you pass Go, collect {GREEN}200{END}.': lambda player, game: self.change_position(player, 11, game),
    'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled.': lambda player, game: self.railroad(player, game),
    'Advance token the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled.': lambda player, game: self.railroad(player, game),
    'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, pay owner a total ten times amount thrown.': lambda player, game: self.utility(player, game),
    f'Bank pays you dividend of {GREEN}50{END}.': lambda player, game: self.gain_money(player, 50),
    'Get Out of Jail Free.': lambda player, game: self.jail_card(player, 'chance'),
    'Go Back 3 Spaces.': lambda player, game: self.change_position(player, player.position -3, game, reverse=True), 
    'Go to Jail. Go directly to Jail, do not pass Go, do not collect 200.': lambda player, game: game.go_to_jail(player),
    f'Make general repairs on all your property. For each house pay {RED}25{END}. For each hotel pay {RED}100{END}.': lambda player, game: self.pay_houses(player, 'chance', game),
    f'Speeding fine {RED}15{END}.': lambda player, game: self.pay_money(player, 15, game),
    f'Take a trip to Reading Railroad. If you pass Go, collect {GREEN}200{END}.': lambda player, game: self.change_position(player, 5, game),
    f'You have been elected Chairman of the Board. Pay each player {RED}50{END}.': lambda player, game: self.spread_money(player, 50),
    f'Your building loan matures. Collect {GREEN}150{END}': lambda player, game: self.gain_money(player, 150)
}
        self.chest = {
    f'Advance to Go (Collect {GREEN}200{END})': lambda player, game: self.change_position(player, 0, game),
    f'Bank error in your favor. Collect {GREEN}200{END}': lambda player, game: self.gain_money(player, 200),
    f"Doctor's fee. Pay {RED}50{END}": lambda player, game: self.pay_money(player, 50, game),
    f'From sale of stock you get {GREEN}50{END}': lambda player, game: self.gain_money(player, 50),
    'Get Out of Jail Free': lambda player, game: self.jail_card(player, 'chest'),
    'Go to Jail. Go directly to Jail, do not pass Go, do not collect 200': lambda player, game: game.go_to_jail(player),
    f'Holiday fund matures. Receive {GREEN}100{END}': lambda player, game: self.gain_money(player, 100),
    f'Income tax refund. Collect {GREEN}20{END}': lambda player, game: self.gain_money(player, 20),
    f'It is your birthday. Collect {GREEN}10{END} from every player': lambda player, game: self.spread_money(player, 10),    
    f'Life insurance matures. Collect {GREEN}100{END}': lambda player, game: self.gain_money(player, 100),
    f'Pay hospital fees of {RED}100{END}': lambda player, game: self.pay_money(player, 100, game),
    f'Pay school fees of {RED}50{END}': lambda player, game: self.pay_money(player, 50, game),
    f'Receive {RED}25{END} consultancy fee': lambda player, game: self.pay_money(player, 25, game),
    f'You are assessed for street repair. {RED}40{END} per house. {RED}115{END} per hotel': lambda player, game: self.pay_houses(player, 'chest', game),
    f'You have won second prize in a beauty contest. Collect {GREEN}10{END}': lambda player, game: self.gain_money(player, 10),
    f'You inherit {GREEN}100{END}': lambda player, game: self.gain_money(player, 100)
}

        self.shuffled_chance = []
        self.shuffled_chest = []

        self.shuffle_decks()

        
    def shuffle_decks(self):
            chance_cards = list(self.chance.keys())
            random.shuffle(chance_cards)
            self.shuffled_chance = chance_cards

            chest_cards = list(self.chest.keys())
            random.shuffle(chest_cards)
            self.shuffled_chest = chest_cards
        
    def draw_chance(self, game, player):
        drawn_card = self.shuffled_chance[0]
        print(drawn_card)
        self.shuffled_chance.remove(drawn_card)
        self.chance[drawn_card](player, game)
        if drawn_card != 'Get Out of Jail Free.':
            self.shuffled_chance.append(drawn_card)
        else:
            self.jail_card_chance = drawn_card

    def draw_chest(self, game, player):      
        drawn_card = self.shuffled_chest[0]
        print(drawn_card)
        self.shuffled_chest.remove(drawn_card)
        self.chest[drawn_card](player, game)
        if drawn_card != 'Get Out of Jail Free':
            self.shuffled_chest.append(drawn_card)
        else:
            self.jail_card_chest = drawn_card
            
    def jail_card(self, player, deck, game=None):
        if deck == 'chance':
            player.jail_card_chance = True
        elif deck == 'chest':
            player.jail_card_chest = True

    def pay_money(self, player, amount, game=None):
        if player.bank > amount:
            player.lose_money(amount)
            player.check_balance()
        else:
            game.erase_player(player)

    def gain_money(self, player, amount, game=None):
        player.add_money(amount)
        player.check_balance()

    def spread_money(self, player, amount, game=None):
        if amount == 10:
            player.add_money(amount * (len(player_list) - 1))
            player.check_balance()
            for person in player_list:
                if person != player:
                    person.lose_money(amount)
                    person.check_balance()
            
        elif amount == 50:
            player.lose_money(amount * (len(player_list) - 1))
            player.check_balance()
            for person in player_list:
                if person != player:
                    person.add_money(amount)
                    person.check_balance()

    def change_position(self, player, position, game, reverse=False):
        player.skip_go = True
        if reverse == False:
            game.go_check(player, position)
        else:
            game.go_check(player, position, reverse=True)
        game.check_space(player)
        player.n += 1
        return
    
    def pay_houses(self, player, deck, game):
        for prop in player.bought:
            if 'Railroad' not in prop:
                house_amount = house[prop][1]
                if house_amount < 5:
                    if deck == 'chance':
                        player.lose_money(house_amount * 25)
                    elif deck == 'chest':
                        player.lose_money(house_amount * 40)                    
                elif house_amount == 5:
                    if deck == 'chance':
                        player.lose_money(house_amount * 100)
                    elif deck == 'chest':
                        player.lose_money(house_amount * 115)
                if player.bank <= 0:
                    game.erase_player(player)
                    return
        player.check_balance()

    def railroad(self, player, game):
        player.skip_rent = True
        distances = {5: (5 - player.position) % 40, 15: (15 - player.position) % 40, 25: (25 - player.position) % 40, 35: (35 - player.position) % 40}
        self.closest_railroad = min(distances, key = distances.get)
        self.change_position(player, self.closest_railroad, game)
        #PAY DOUBLE
        self.property_name = board[player.position]
        house_num = house[self.property_name][1]
        if self.property_name in game.bought:
            owner = game.bought[self.property_name]
            if owner != player:
                if player.bank < rent[self.property_name][0]*2:
                    game.erase_player(player)
                    return
                print(f'{player} owes {RED}{(rent[self.property_name][house_num])*2}{END} to {owner}')      
                player.lose_money((rent[self.property_name][house_num])*2)
                owner.add_money((rent[self.property_name][house_num])*2)
                player.check_balance()
                owner.check_balance()

    def utility(self, player, game):
        player.skip_rent = True
        self.prev_roll = player.history[player.n]
        distances = {12: (12 - player.position) % 40, 28: (28 - player.position) % 40}
        self.closest_utility = min(distances, key = distances.get)
        self.change_position(player, self.closest_utility, game)
        #PAY 10X  
        if board[player.position] in game.bought:
            owner = game.bought[board[player.position]]
            if owner != player:
                if board[player.position] == 'Electric Company' or board[player.position] == 'Water Works':
                    if player.bank < self.prev_roll*10:
                        game.erase_player(player)
                        return
                    print(f'{player} owes {RED}{self.prev_roll*10}{END} to {owner}')
                    player.lose_money(self.prev_roll*10)
                    owner.add_money(self.prev_roll*10)
                    player.check_balance()
                    owner.check_balance()
from player import player_list, lookup
from game import Game
game = Game(player_list)

            
def roll_turn(player):
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
                game.go_to_jail(player)
                break 
            print(f'{player} turn {player.n}: {player.history[player.n]} ({player.rolled[0]} and {player.rolled[1]})')
            game.check_space(player)
            property_name = game.board[player.position]
            if property_name in game.prices:
                answer = input(f'Do you want to buy {game.colour(property_name)} for \033[38;5;196m{game.prices[property_name]}\033[0m?')
                if answer == 'y':
                    game.buy_property(player)
                elif answer == 'n':
                    continue
        else:  
            print(f'{player} turn {player.n}: {player.history[player.n]} ({player.rolled[0]} and {player.rolled[1]})')
            game.check_space(player)
            property_name = game.board[player.position]
            if property_name in game.prices:
                answer = input(f'Do you want to buy {game.colour(property_name)} for \033[38;5;196m{game.prices[property_name]}\033[0m?')
                if answer == 'y':
                    game.buy_property(player)
                    break
                elif answer == 'n':
                    break    
            break                
            

def player_turn(player):
    #Bankruptcy Check
    if player.is_bankrupt == True:
        player_list.remove(player)
    if len(player_list) == 1:
        print(f'{player_list[0]} has won the game!')
        game.end_game == True
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
            roll_turn(player)
            break
        elif choice == '2':
            player.check_balance()
        elif choice == '3':
            game.print_dict()
        elif choice == '4':
            colour = input('Which set of properties?')
            game.buy_house(player, colour)
        elif choice == '5':
            tradee = input(f'Which player will {player} trade with?')
            tradee_name = lookup.get(tradee)
            prop1 = input(f'Which property will {player} trade?')
            prop2 = input(f'Which property will {tradee_name} trade?')
            game.trade(player, tradee, prop1, prop2)
        elif choice == '6':
            if player.in_jail == False:
                print(f'{player} is not in jail')
            elif player.jail_card_chance == False and player.jail_card_chest == False:
                print('No Get Out of Jail cards available')
            elif player.jail_card_chance == True and player.jail_card_chest == False:
                player.jail_card_chance = False
                player.in_jail = False
                game.return_card('chance')
                print(f'{player} is out of jail')
            elif player.jail_card_chance == False and player.jail_card_chest == True:
                player.jail_card_chest = False
                player.in_jail = False
                game.return_card('chest')
                print(f'{player} is out of jail')
            elif player.jail_card_chance == True and player.jail_card_chest == True:
                player.jail_card_chest = False
                player.in_jail = False
                game.return_card('chest')
                print(f'{player} is out of jail')       
        elif choice == '7':
            game.rage_quit(player)
            break
        elif choice == '8':
            end = input('Are you sure?: ')
            if end == 'n':
                print('Back to the game')
            elif end == 'y':
                print('Game over')
                game.end_game = True
                break
            else:
                print('Please input valid option')
        
                
def game_turn():
    while game.end_game == False:
        for player in player_list[:]:
            player_turn(player)
            if game.end_game:
                break
        if len(player_list) == 1:
            break
    

game_turn()
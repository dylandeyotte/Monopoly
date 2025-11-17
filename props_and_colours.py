
END = '\033[0m'
GREEN = '\033[38;5;40m'
RED = '\033[38;5;196m'

board = ['GO', 'Mediterranean Avenue', 'Community Chest', 'Baltic Avenue', 'Income Tax', 'Reading Railroad', 'Oriental Avenue', 'Chance', 'Vermont Avenue', 'Connecticut Avenue',
'Jail / Just Visiting', 'St. Charles Place', 'Electric Company', 'States Avenue', 'Virginia Avenue', 'Pennsylvania Railroad', 'St. James Place', 'Community Chest', 'Tennessee Avenue', 'New York Avenue',
'Free Parking', 'Kentucky Avenue', 'Chance', 'Indiana Avenue', 'Illinois Avenue', 'B&O Railroad', 'Atlantic Avenue', 'Ventnor Avenue', 'Water Works', 'Marvin Gardens',
'Go to Jail', 'Pacific Avenue', 'North Carolina Avenue', 'Community Chest', 'Pennsylvania Avenue', 'Short Line Railroad', 'Chance', 'Park Place', 'Luxury Tax', 'Boardwalk']

prices = {
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

rent = {
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

house = {
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

colours = {
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

house_colours = {
    'Brown': ['Mediterranean Avenue', 'Baltic Avenue'],                           
    'Light Blue': ['Oriental Avenue', 'Vermont Avenue', 'Connecticut Avenue'],     
    'Magenta': ['St. Charles Place', 'States Avenue', 'Virginia Avenue'],            
    'Orange': ['St. James Place', 'Tennessee Avenue', 'New York Avenue'],      
    'Red': ['Kentucky Avenue', 'Indiana Avenue', 'Illinois Avenue'],             
    'Yellow': ['Atlantic Avenue', 'Ventnor Avenue', 'Marvin Gardens'],          
    'Green': ['Pacific Avenue', 'North Carolina Avenue', 'Pennsylvania Avenue'],    
    'Dark Blue': ['Park Place', 'Boardwalk']  
}
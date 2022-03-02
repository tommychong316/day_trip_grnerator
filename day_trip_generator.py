#day_trip_generator

#Total Unweighted Project Points: /70
#Total Weighted Project Points: /10

#(5 points): As a developer, I want to make at least three commits with descriptive messages. 
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists. 
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 
#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 
#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
#(10 points): As a user, I want to display my completed trip in the console.
#(5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!
#assignment


import random




places = ['Tatuin', 'Mordor', 'Konoha', 'Hogwarts']
restaurants = ['Three Broomsticks', 'Krusty Krab', 'Ichirakus', 'Puzzles']
entertainments = ['Quidditch', 'Chunin Exam', 'Pod Racing', 'Pro-Bending']
transports = ['Ninja Run', 'Broomstick', 'Floo Powder', 'Car']
trip = random.choice(places), random.choice(restaurants), random.choice(entertainments), random.choice(transports)
place = random.choice(places)
restaurant = random.choice(restaurants)
entertainment = random.choice(entertainments)
transport = random.choice(transports)





answer = 'y'
def tripreq(pick):
    choice = input(f'Do you like this trip to {place}, where you will dine at {restaurant}; you will be able to get around by {transport} to enjoy {entertainment}? Enter y/n: ')
    while 'y' != choice == 'n':
        redicision = input(f'Sorry is this trip to {random.choice(places)}, where you will dine at {random.choice(restaurants)}; you will be able to get around by {random.choice(transports)} to enjoy {random.choice(entertainments)} better? Enter y/n: ')
        
        if 'y' != redicision != 'n': 
            print('Please choose y or n') and print(redicision)
            
        if redicision == 'y':
            print('Great choice! We shall move on!')
            break       
    if choice == 'y':
        print('Great choice! We will move on then!')
    elif 'y' != choice != 'n':
        print('Please select y or n') 
        tripreq(answer)
tripreq(answer)


going = 'y'

def forsure(course):
    g2g = input(f'Are you happy with your trip to {place}, where you will dine at {restaurant}; you will be able to get around by {transport} to enjoy {entertainment}Enter Y/N: ')        
    if g2g == 'y':
        print(f'Trip to {place}, where you will dine at {restaurant}; you will be able to get around by {transport} to enjoy {entertainment} is confirmed')
    if 'y' != g2g == 'n':
        print('Cool. Come back when you are ready.')
    if 'y' != g2g != 'n':
        print('Please choose y or n')
        forsure(going)
        
forsure(going)
def main(item):
    hope = [f'destination: {place}', f'restaurant: {restaurant}', f'transportation: {transport}', f'entertainment: {entertainment}']    
    print('Here is your planned vacay:')
    for i in hope:
        print(i)

displays = [place, restaurant, transport, entertainment]

main(displays)
           
        


   



           



    

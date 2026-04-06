#computer picks a random number 1-100
#the user has to guess the number, if wrong it says higher or lower until they get it
#we need 3 options play game, view stats, quit
import random


current_game_number = 0
lowest_num_of_guesses = []


def play_game():
    guesses = 0
    rannum = random.randint(1,100)
    
    while True:
        userguess = int(input("Pick a nunber between 1 and 100 or 0 to quit: "))
        
        if userguess == rannum:
            guesses += 1
            print("You got it good job! ")
            quit
        elif userguess == 0:
            break    
        elif userguess > rannum:
            print("Too high, try again!")
            guesses += 1
            continue
        elif userguess < rannum:
            print("Too low, try again!")
            guesses+= 1
            continue
    lowest_num_of_guesses.append(guesses)
       


def stats():
    print("Number of games played = ", current_game_number)
    print("lowest number of guesses to get the number = ", min(lowest_num_of_guesses))
    

while True:

    user_choice = int(input("1. play game\n2. View stats \n3. quit \ninsert 1,2 or 3: "))
    if user_choice == 1:
        current_game_number += 1 
        play_game()
        continue
    elif user_choice == 2:
        stats()
        continue
    else:
        break
import os
import time
import mechanics

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')                        # Clean the screen

def firts_screen():

    clean_screen()
    yes_no_choice = ''

    while yes_no_choice not in ['1','2']:

        print(
'''
Welcome to Rock, Paper, Scissors game!

    Do you want to play:
    1> Yes.
    2> No.
'''
        )

        yes_no_choice = int(input('Pleas you must to choose the options (1 or 2): '))

        if yes_no_choice == 1:

            charging_screen()
            clean_screen()
            print('you are playing')
            time.sleep(2)
            second_screen()
        
        elif yes_no_choice == 2:

            clean_screen()
            print('that has been all, thank you')
            time.sleep(2)
            clean_screen()
            break

def second_screen():

    n_round = 1
    p_score = 0
    ai_score = 0
    
    clean_screen()

    print(f'''
    Your are playing!

Round{n_round} | Player score => {p_score} - AI score => {ai_score}

    choose between:

    1> Rock.
    2> Paper.
    3> Sicssors.
    4> Exit.    
'''
    )

    mechanics.game_mechanics()

def charging_screen():

    counter = 0.5
    message = '.....'

    for i in range (0,3):
        clean_screen()
        print(f'charging {message}')
        time.sleep(counter)
        counter += 0.5
        message = message * 2
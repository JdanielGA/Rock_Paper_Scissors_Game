import os

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')                        # Clean the screen

def firts_screen():

    clean_screen()

    print(
'''
Welcome to Rock, Paper, Scissors game!

    Do you want to play:
    1> Yes.
    2> No.
'''
    )

    yes_no_choice = int(input('Pleas ou must to choose the options (1 or 2): '))

    if yes_no_choice == 1:

        clean_screen()
        print('you are playing')
    
    elif yes_no_choice == 2:

        clean_screen()
        print('that has been all, thank you')
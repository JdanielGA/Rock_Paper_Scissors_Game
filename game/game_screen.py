import mechanics
import tools

def firts_screen():

    tools.clean_screen()
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

            tools.charging_screen()
            tools.clean_screen()
            print('\n   You are playing!')
            tools.time.sleep(2)
            second_screen()
        
        elif yes_no_choice == 2:

            tools.clean_screen()
            print('that has been all, thank you')
            tools.time.sleep(2)
            tools.clean_screen()
            break

def second_screen():

    n_round = 1
    p_score = 0
    ai_score = 0
    
    tools.clean_screen()

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
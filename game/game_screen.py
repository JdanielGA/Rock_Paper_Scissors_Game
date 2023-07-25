import mechanics
import tools

def firts_screen():

    tools.clean_screen()
    yes_no_choice = ''

    while yes_no_choice not in ['1','2']:

        tools.clean_screen()
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
            t_rounds = int(input('Introduce the number of rounds that you want to play: '))
            print('\n   You are playing!')
            tools.time.sleep(2)
            second_screen(t_rounds)
        
        elif yes_no_choice == 2:
            tools.clean_screen()
            end_screen()
            break

def second_screen(t_rounds):

    tools.clean_screen()
    total_rounds = t_rounds
    n_round = 1
    p_score = 0
    ai_score = 0

    while True:

        tools.clean_screen()
        print(f'''
    Your are playing!

Round {n_round} of {total_rounds} | Player score => {p_score} - AI score => {ai_score}

    choose between:

    1> Rock.
    2> Paper.
    3> Sicssors.
    4> Exit.    
'''
    )
        user_input = input('Type the number of the chosen option: ')

        try:
            user_choice = int(user_input)

            if user_choice == 4:
                end_screen()
                break

            elif user_choice in [1, 2, 3]:
                p_score, ai_score, = mechanics.game_mechanics(user_choice, p_score, ai_score)
                n_round += 1
                if n_round > total_rounds:
                    print(f'The match has finished, final score: Player score => {p_score} - AI score => {ai_score}')
                    tools.time.sleep(3)
                    return False

            else:
                print("Invalid input! Please choose a valid option.")
                tools.time.sleep(2)
                tools.clean_screen()
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            tools.time.sleep(2)
            tools.clean_screen()
    

def end_screen():

    tools.clean_screen()
    print('that has been all, thank you.')
    tools.time.sleep(2)
    tools.clean_screen()
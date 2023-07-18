import tools

def game_mechanics():

    options = ['Rock','Paper','Scissors']

    user_choice = int(input('Type option the number of the chosen option: '))
    chosen_option = options[user_choice-1]
    ai_player = tools.ai_player()
    ai_choice = options[ai_player]

    print(f'\n you have chosen {chosen_option} and the ai has chosen {ai_choice}')
    result = match(chosen_option,ai_choice)
    print(result)

    tools.time.sleep(3)
    tools.clean_screen()


def match(chosen_option, ai_choice):

    if chosen_option == ai_choice:
        return 'Tie'
    
    elif (chosen_option == 'Rock' and ai_choice == 'Scissors') or  (chosen_option == 'Paper' and ai_choice == 'Rock') or (chosen_option == 'Scissors' and ai_choice == 'Paper'):
        return 'You win'
    
    else:
        return 'You lost'
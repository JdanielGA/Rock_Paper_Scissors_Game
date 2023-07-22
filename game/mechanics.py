import tools

def game_mechanics(user_choice, p_score, ai_score):

    options = ['Rock','Paper','Scissors']
    user_choice = user_choice
    chosen_option = options[user_choice-1]
    ai_player = tools.ai_player()
    ai_choice = options[ai_player]

    print(f'\n you have chosen {chosen_option} and the ai has chosen {ai_choice}')
    result = match(chosen_option, ai_choice, p_score, ai_score)
    print(f'\n {result[0]}')
    tools.time.sleep(2)
    tools.clean_screen()
    return result[1], result[2]


def match(chosen_option, ai_choice, p_score, ai_score):

    if chosen_option == ai_choice:
        return 'Tie', p_score, ai_score
    
    elif (chosen_option == 'Rock' and ai_choice == 'Scissors') or  (chosen_option == 'Paper' and ai_choice == 'Rock') or (chosen_option == 'Scissors' and ai_choice == 'Paper'):
        p_score += 1
        return 'You win', p_score, ai_score
    
    else:
        ai_score += 1
        return 'You lost', p_score, ai_score
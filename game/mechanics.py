import random

def game_mechanics():

    options = ['Rock','Paper','Scissor']

    choice = int(input('Type option the number of the chosen option: '))

    chosen_option = options[choice-1]

    print(f'\nyou have chosen {chosen_option}')
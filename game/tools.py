import os
import time
import random

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')                        # Clean the screen

def charging_screen():

    counter = 0.5
    message = '.....'

    for i in range (0,3):
        clean_screen()
        print(f'charging {message}')
        time.sleep(counter)
        counter += 0.33
        message = message * 2

def ai_player():
    
    ai_choice = random.randint(0,2)
    return ai_choice
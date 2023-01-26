# import libraries

import time
import numpy as np
import sys
import pokedex as Pokemon

# Delay printing

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

#making try again part for the game putting all game in function
def game():

#Welcome and choosing part
    delay_print('Welcome, please choose from the pokemons below:\n')
    print('1.',Pokemon.Pokemon[0]['Name'],'2.',Pokemon.Pokemon[1]['Name'],"3.",Pokemon.Pokemon[2]['Name'],
    "4.", Pokemon.Pokemon[3]['Name'])

    pokemon1 = int(input("Please choose the first Pokemon: ")) -1
    pokemon2 = int(input("Please choose the second Pokemon: ")) -1

    delay_print('###########################\n')
    print(" BATTLE STARTS !\n", Pokemon.Pokemon[pokemon1]['Name'], 'VS',Pokemon.Pokemon[pokemon2]['Name'])
    delay_print('###########################\n')

    # decide who attacks first
    speed_1 = Pokemon.Pokemon[pokemon1]['Speed']
    speed_2 = Pokemon.Pokemon[pokemon2]['Speed']

    if speed_1 > speed_2:
        print(Pokemon.Pokemon[pokemon1]['Name'], "is attacking first!")
        first_attacker = Pokemon.Pokemon[pokemon1]
        second_attacker = Pokemon.Pokemon[pokemon2]

    else:
        print(Pokemon.Pokemon[pokemon2]['Name'], "is attacking first!")
        Pokemon.Pokemon[pokemon1]
        first_attacker = Pokemon.Pokemon[pokemon2]
        second_attacker = Pokemon.Pokemon[pokemon1]

    print(first_attacker['Name'], 'knows', '1.',first_attacker['Move'][0][0], 'with power:' ,first_attacker['Move'][0][1], 'and', '2.',first_attacker['Move'][1][0],'with power:' ,first_attacker['Move'][1][1])

    #variables with health of each species
    health_2nd_attacker = second_attacker['Health'] 
    health_1st_attacker = first_attacker['Health']

    #loop for fighting part
    while True:
            
    ############################
    #  first attacker block start
    #############################
        moves = int(input('please choose the move:'))-1
        print(first_attacker['Name'], 'is using ',first_attacker['Move'][moves][0])

        base_damage = first_attacker['Move'][moves][-1]
        print(first_attacker['Name'], 'has dealt ', base_damage , 'damage.')

        health_2nd_attacker  -=  base_damage
        print(second_attacker['Name'], 'has',health_2nd_attacker, 'HP left')

        #health check part
        if health_2nd_attacker <=0:
            print(second_attacker['Name'], 'fainted.')
            winner1 = first_attacker['Name']
            looser1 = second_attacker['Name']
            delay_print(f'{winner1} is the winner of this battle! Congratulation!\n')
            delay_print(f'{looser1} next time you will be more prepared :)')
            break
        else:
            print('\nNow',second_attacker['Name'], 'attacking!')
            
    ############################
    #  first attacker block finished
    #############################

    ############################
    #  second attacker block start
    ############################

        print(second_attacker['Name'], 'knows','1.' ,second_attacker['Move'][0][0], 'with power:' ,second_attacker['Move'][0][1], 'and', '2.',second_attacker['Move'][1][0],'with power:' ,second_attacker['Move'][1][1])
        moves = int(input('please choose the attack:'))-1
        
        print(second_attacker['Name'], 'is using ',second_attacker['Move'][moves][0])
        base_damage = second_attacker['Move'][moves][-1]

        print(second_attacker['Name'], 'has dealt ', base_damage , 'damage.')
        health_1st_attacker -=  base_damage
        print(first_attacker['Name'], 'has',health_1st_attacker, 'HP left\n')
        
        #health check part
        if health_1st_attacker <=0:
            print(first_attacker['Name'], 'fainted.')
            winner2 = second_attacker['Name']
            looser2 = first_attacker['Name']
            delay_print(f'{winner2} is the winner of this battle! Congratulation!\n')
            delay_print(f'{looser2} next time you will be more prepared :)')
            break
        else:
            print(first_attacker['Name'] ,'is attacking !')

############################
#  second attacker block ends2
############################

#asks for play again
while True:
    game()
    if input ('\nDo you want to play again? y/n: ').lower() == 'n':
        break
# %%


# %%

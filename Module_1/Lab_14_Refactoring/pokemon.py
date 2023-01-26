# %%
# import libraries

import time
import numpy as np
import sys




# Delay printing

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
        


Pokemon = [{
  
    'Name':'Bulbasaur',
    'Speed': 45,
    'Health': 45,
    'Type':'Grass & Poison',
    'Move':[['Headbutt',12],['Vine Whip',20]],
    'Attack':49 ,
    'Defense':49
}

,{
    'Name':'Charmander',
    'Speed': 65,
    'Health': 39,
    'Type':'Fire',
    'Move':[['Slash',22],['Flame Thrower',26]],
    'Attack':52 ,
    'Defense':43
    
}

,  {

    'Name':'Squirtle',
    'Speed': 43,
    'Health': 44,
    'Type':'Water',
    'Move':[['Bite',35],['Surf',30]],
    'Attack':48 ,
    'Defense':65
}]



print('Welcome, please choose from the pokemons below:')
print('1.',Pokemon[0]['Name'],'2.',Pokemon[1]['Name'],"3.",Pokemon[2]['Name'])
pokemon1 = int(input("Please choose the first Pokemon: ")) -1

pokemon2 = int(input("Please choose the second Pokemon: ")) -1

print(" BATTLE STARTS !\n", Pokemon[pokemon1]['Name'], 'VS',Pokemon[pokemon2]['Name'])








# print(pokemon1,pokemon2)

# def fight(pokemon1, pokemon2):
# decide who attacks first
speed_1 = Pokemon[pokemon1]['Speed']
# print(speed_1)

speed_2 = Pokemon[pokemon2]['Speed']

if speed_1 > speed_2:
    print(Pokemon[pokemon1]['Name'], "is attacking first!")
    first_attacker = Pokemon[pokemon1]
    second_attacker = Pokemon[pokemon2]

else:
    print(Pokemon[pokemon2]['Name'], "is attacking first!")
    Pokemon[pokemon1]
    first_attacker = Pokemon[pokemon2]
    second_attacker = Pokemon[pokemon1]

print(first_attacker['Name'], 'knows', '1.',first_attacker['Move'][0][0], 'with power:' ,first_attacker['Move'][0][1], 'and', '2.',first_attacker['Move'][1][0],'with power:' ,first_attacker['Move'][1][1])
# print(second_attacker['Name'], 'knows', second_attacker['Move'][0][0], 'with power:' ,second_attacker['Move'][0][1], 'and', second_attacker['Move'][1][0],'with power:' ,second_attacker['Move'][1][1])







health_2nd_attacker = second_attacker['Health'] 
# print(health_2nd_attacker)
health_1st_attacker = first_attacker['Health']
# print(health_1st_attacker)


# while health_2nd_attacker >= 0 and health_1st_attacker >= 0:
while True:
    
    
############################
#  first attacker block
#############################
    moves = int(input('please choose the move:'))-1
    
    print(first_attacker['Name'], 'is using ',first_attacker['Move'][moves][0])

    
    
    base_damage = first_attacker['Move'][moves][-1]
    print(first_attacker['Name'], 'has dealt ', base_damage , 'damage.')

    
    
    health_2nd_attacker  -=  base_damage
    print(second_attacker['Name'], 'has',health_2nd_attacker, 'HP left')

    
    
    if health_2nd_attacker <=0:
        print(second_attacker['Name'], 'fainted.')
        break
    else:
        print('\nNow',second_attacker['Name'], 'attacking!')
        
############################
#  first attacker block
#############################



############################
#  second attacker block
############################

    print(second_attacker['Name'], 'knows','1.' ,second_attacker['Move'][0][0], 'with power:' ,second_attacker['Move'][0][1], 'and', '2.',second_attacker['Move'][1][0],'with power:' ,second_attacker['Move'][1][1])
    
    
    moves = int(input('please choose the attack:'))-1
    
    print(second_attacker['Name'], 'is using ',second_attacker['Move'][moves][0])
    
    base_damage = second_attacker['Move'][moves][-1]
    print(second_attacker['Name'], 'has dealt ', base_damage , 'damage.')
    
   

    health_1st_attacker -=  base_damage
    
    print(first_attacker['Name'], 'has',health_1st_attacker, 'HP left\n')
    
    
    
    if health_1st_attacker <=0:
        print(first_attacker['Name'], 'fainted.')
        break
    else:
        print(first_attacker['Name'] ,'is attacking !')
#     print(health_1st_attacker)


############################
#  second attacker block
############################

# %%


# %%

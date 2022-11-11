import random
from time import sleep


def wait():
    for i in range(5) :
        print('.', end = " ")
        sleep(.6)
    print()

def parts(x):
    if x == 5 :
        print('       ',   '+------+')
        print('       ',   '|       ')
        print('       ',   '|       ')
        print('       ',   '|       ')
        print('       ',   '|       ')
        print('       ',   '|       ')
        print('-------------------')
    if x == 4 :
        print('       ',   '+------+')
        print('       ',   '|      |')
        print('       ',   '|       ')
        print('       ',   '|       ')
        print('       ',   '|       ')
        print('       ',   '|       ')
        print('-------------------')
    if x == 3 :
        print('       ',   '+------+')
        print('       ',   '|      |')
        print('       ',   '|      @')
        print('       ',   '|       ')
        print('       ',   '|       ')
        print('       ',   '|       ')
        print('-------------------')
    if x == 2 :
        print('       ',   '+------+')
        print('       ',   '|      |')
        print('       ',   '|      @')
        print('       ',   '|      |')
        print('       ',   '|       ')
        print('       ',   '|       ')
        print('-------------------')
    if x == 1 :
        print('       ',   '+------+')
        print('       ',   '|      |')
        print('       ',   '|      @')
        print('       ',   '|     /|\\')
        print('       ',   '|      |')
        print('       ',   '|       ')
        print('-------------------')
    if x == 0 :
        print('       ',   '+------+')
        print('       ',   '|      |')
        print('       ',   '|      @')
        print('       ',   '|     /|\\')
        print('       ',   '|      |')
        print('       ',   '|     / \\ ')
        print('-------------------')
        print('!!! YOU ARE DEAD !!!!')

def choose_random_fruit(fruits_list: list):
    return random.choice(fruits_list)

def get_fruit_letters(fruit :str):
    return list(fruit)

def get_blanks_of_chosen_fruit(fruit, blank):
    blanks_map=map( lambda x: blank, list(fruit))
    return list(blanks_map)
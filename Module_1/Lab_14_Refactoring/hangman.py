from time import sleep
import re
from itertools import count
import random

fruits=["apple" , "apricot" , "araza" , "avocado" , "banana" , "blackberry", "blueberry", "cherry" , "coconut" , "cranberry" ,"date" , "dragonfruit" , "feijoa" , "fig", "grape", "raisin", "guava", "kiwi" , "lemon", "lime", "lychee" , "mango" , "melon", "watermelon", "nectarine" , "orange", "clementine" , "papaya" , "passionfruit", "peach", "pear", "plum" , "prune" , "pineapple", "pomegranate", "pomelo", "strawberry" ,"tamarind", "yuzu"]
chosen_fruit=""
chosen_fruit_letters=[]
tries=[]
blanks=[]
blank=" __ "

chosen_fruit=random.choice(fruits)


for letter in chosen_fruit:
    chosen_fruit_letters.append(letter)
    blanks.append(blank)
    




def wait():
    for i in range(5) :
        print('.', end = " ")
        sleep(.6)
    print()
print('Welcome to Hangman. Let me think of a word')
print("Be careful you have only 6 tries. Good luck!")
print("Hint : it is a fruit 🍇")
wait()

print(blanks)

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

tries=6
while 1 <= tries  and tries <= 6 and blank in blanks:
    
    print("====================================================================")
    user_letter=input("Please choose a letter : ").lower()
    if not (re.match("^[a-z]*$", user_letter) and len(user_letter) ==1):
        print("Error! Only one letter a-z is allowed! Try again. ")
        print(tries)
    else:
        print(user_letter)
        for index in range(len(chosen_fruit_letters)):
            if user_letter == chosen_fruit_letters[index]:
                print('correct')
                blanks[index]=user_letter
                print(blanks)
            
        if not user_letter in chosen_fruit_letters:
            tries-=1
            print(parts(tries))
            print("This letter" , user_letter, "is not in the secret word, you have " , tries, "left")

          

if blanks == chosen_fruit_letters:
    print("YOU WIN")
else:
    print("YOU LOSE")
    print("The secret word was: ", chosen_fruit)

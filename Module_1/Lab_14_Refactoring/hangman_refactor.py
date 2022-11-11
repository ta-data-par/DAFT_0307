import re
from constants import FRUITS, BLANK, TRIES
from hangman_functions import wait, parts, choose_random_fruit, get_blanks_of_chosen_fruit, get_fruit_letters


chosen_fruit = choose_random_fruit(FRUITS)
chosen_fruit_letters = get_fruit_letters(chosen_fruit)
blanks = get_blanks_of_chosen_fruit(chosen_fruit, BLANK)

print('Welcome to Hangman. Let me think of a word')
print("Be careful you have only 6 tries. Good luck!")
print("Hint : it is a fruit 🍇")
wait()

print(blanks)

while 1 <= TRIES and TRIES <= 6 and BLANK in blanks:

    print("====================================================================")
    user_letter = input("Please choose a letter : ").lower()
    if not (re.match("^[a-z]*$", user_letter) and len(user_letter) == 1):
        print("Error! Only one letter a-z is allowed! Try again. ")
        print(TRIES)
    else:
        print(user_letter)
        for index in range(len(chosen_fruit_letters)):
            if user_letter == chosen_fruit_letters[index]:
                print('correct')
                blanks[index] = user_letter
                print(blanks)

        if not user_letter in chosen_fruit_letters:
            TRIES -= 1
            print(parts(TRIES))
            print("This letter", user_letter,
                  "is not in the secret word, you have ", TRIES, "left")


if blanks == chosen_fruit_letters:
    print("YOU WIN")
else:
    print("YOU LOSE")
    print("The secret word was: ", chosen_fruit)

#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') # opens the program with a greeting
colors = ['red','orange','yellow','green','blue','violet','purple'] # lists all potential answers to the question
play_again = '' # allows for repeated uses of the program
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): # asks the user if they would like to use the program again
    match_color = random.choice(colors) # returns a random output
    count = 0 # sets the count to zero off the bat to allow for accurate cataloging
    color = '' # setting up the next few lines with their denomination
    while (color != match_color): # sets a condition on the color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() # allows for different specllings and capitalizations
        count += 1 # keeps count of input number
        if (color == match_color): # conditional statement
            print('Correct!') # will return this phrase if you enter the correct answer
        else: # conditional statement - the opposite of the previous
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) # will return this if you do not guess the correct answer and tells you how many tries you've made
    print('\nYou guessed it in {0} tries!'.format(count)) # lets you know how long it took you to get the correct answer
    if (count < best_count): # keeps track of your progress and previous attempts
        print('This was your best guess so far!') # gratification from a computer
        best_count = count # conditional on whether or not this was your best go at the program
    play_again = input("\nWould you like to play again? ").lower().strip() # allows you to play this little game again if you so wish
print('Thanks for playing!') # returns this when you are done with the program
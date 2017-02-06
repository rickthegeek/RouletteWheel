#Project: CIS 177 WEEK 1 PROJECT
#Project Location: projects\cis177\Week3
#File: roulette.py
#Purpose: Request input of a number representing a pocket on a roulette wheel
#         Then print the color of the chosen pocket number to standard output
#Revision: 1.0 / 5 FEB 2017
#Created: 5 FEB 2017
#Author: Rick Miller <rick@rickthegeek.com>

# PER WRITTEN SPEC:
# Colors used are: 0 - Green, 1 thru 10 and 19 thru 28, evens are red and odds are black
# and 11 thru 18, and 26 thru 36, evens are black and odds are red.

# PROGRAMMER'S NOTE: The spec has conflicting information, as given, pockets 26 and
# 27 and 28 would be *both* black and red. Referring to the Wikipedia entry for roulette,
# the second "evens black, odds red" section starts at pocket number 29, so that is how
# I have implemented it here. 

# First, ask the user to enter the number of the pocket chosen

print('Roulette wheel pocket color identifier')
pocketNumber = int(input('Please enter the pocket number from 0 to 36: ')) # Convert it to an int so we can do math on it!

#Now, first test if the number is between 0 through 36.
# Then, determine what group it is in, and decide if it is even or odd
# finally, store the color in the string pocketColor.

if (0 <= pocketNumber <= 36):
    # Determine what group the chosen number is in
    if (pocketNumber == 0): # 0 is the only green pocket
        pocketColor = 'GREEN'
    elif ((1 <= pocketNumber <= 10) or (19 <= pocketNumber <= 28)): # evens are black, odds are red
        if ((pocketNumber % 2) == 0): # number is even
            pocketColor = 'BLACK'
        else: # number is odd
                pocketColor = 'RED'
    elif ((11 <= pocketNumber <= 18) or (29 <= pocketNumber <= 36)): # evens are red, odds are black
        if ((pocketNumber % 2) == 0): # number is even
            pocketColor = 'RED'
        else: # number is odd
            pocketColor = 'BLACK'
    # Now we tell the user what color their chosen pocket is
    print('Pocket number', pocketNumber, 'is', pocketColor)
else: # we end up here if the number entered is not between 0 and 36
    print('Sorry, you need to enter a number between 0 and 36!')

 
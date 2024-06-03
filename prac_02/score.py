
"""import"""

import random

"""main function"""


def main():

    score = random.randint(0, 100)
    print("YOUR RANDOM SCORE IS:" + str(score))
    print_score(score)

"""other functions"""


def determine_score(score):

    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_score(score):
    if score < 0 or score > 100:
        print ("Invalid")
    elif score >= 90:
        print( "Excellent" )
    elif score >= 50:
         print("Passable")
    else:
        print( "Bad" )



"""Calling main function"""

main()





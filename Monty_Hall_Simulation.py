#  File: Deal.py
#  Description: A Monty Hall simulation program.

import random

def roll(n):

    door = random.randint(1, n)
    return door


def runOneTrial(trials):

    prize = roll(3)
    guess = roll(3)

    view = roll(3)
    while view == guess or view == prize:
        view = roll(3)

    newGuess = roll(3)
    while newGuess == guess or newGuess == view:
        newGuess = roll(3)

    print(format(prize, "3d") , format(guess, "6d"), format(view, "6d"), format(newGuess, "6d"))

    if newGuess == prize:
        return "win"
    else:
        return "lose"


def main():

    print()
    trials = int(input("How many trials do you want to run? "))
    print()
    print("Prize", format("Guess", ">6s"), format("View", ">5s"), format("New Guess", ">10s"))

    count = 0
    win = 0

    while count < trials:
        a = runOneTrial(trials)
        #print(a)
        count += 1
        if a == "win":
            b = 1
        elif a == "lose":
            b = 0
        win += b

    pWinSwitch = win / trials
    pWinNoSwitch = 1 - (win / trials)

    print()
    print("Probability of winning if you switch = ", format(pWinSwitch, "5.3f"))
    print("Probability of winning if you do not switch = ", format(pWinNoSwitch, "5.3f"))
    print()

main()
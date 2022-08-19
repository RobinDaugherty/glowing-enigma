import random, time, os
from colorama import Fore, Style

# making style function

def styleString(style, str):
    print(style + str + Style.RESET_ALL)

# initializing variables

choice = "yes"; GuessCount = 0; played = 0; guess = 0
minRange= 0; maxRange = 1; highGuess = []; lowGuess = []; cols=os.get_terminal_size().columns

# guide

while choice == "yes":
    print("\nWelcome to Find The Number, the game where you guess the number in a range!")
    print("After each guess, you are told whether it was higher or lower than the target number.")
    print("You can choose from three pre-made games or customize.")
    print("You can choose between easy mode, where you can see your previous guesses, or hard, where you can't.")
    styleString(Fore.BLUE + Style.BRIGHT, "="*cols)
    choice1 = input("Say yes if you want to play the game: ")

    # inputting settings

    if "yes" in choice1.lower():
        choice = "yes"
        played = 1
        styleString(Fore.BLUE + Style.BRIGHT, "="*cols)
        gameMode = input("Enter" + Fore.BLUE + " easy " + Style.RESET_ALL + "or" + Fore.BLUE + " hard " + Style.RESET_ALL + "to choose gamemode: ")
        if "hard" in gameMode.lower():
            gameMode = "hard"
        else:
            gameMode = "easy"
        choice2 = input("Say yes if you want to play with a pre-set range and number of guesses: ")
        if "yes" in choice2.lower():
            print("\nThere are three pre-set games!")
            choice3 = input(Fore.GREEN + Style.BRIGHT + "1. " + Style.RESET_ALL + "From 1 to 10, with 5 guesses. " + Fore.GREEN + Style.BRIGHT + "2. " + Style.RESET_ALL + "From 1 to 100, with 7 turns. " + Fore.GREEN + Style.BRIGHT + "3. " + Style.RESET_ALL + "From -1000 to 1000, with 11 turns. Enter 1, 2 or 3 to choose: ")
            if "1" in choice3:
                minRange = 1; maxRange = 10; guesses = 5
            elif "2" in choice3:
                minRange = 1; maxRange = 100; guesses = 7
            else:
                minRange = -1000; maxRange = 1000; guesses = 11
        else:
            styleString(Fore.BLUE + Style.BRIGHT, "="*cols)
            minRange = int(input("Enter the minimum value of the guessing range, numerals only: "))
            maxRange = int(input("Enter the maximum value of the guessing range, numerals only: "))
            guesses = int(input("Enter how many guesses you will have, numerals only: "))
            if guesses <=0:
                break
            if minRange == maxRange:
                break
        target = random.randint(minRange, maxRange)

        # while loop to reroll target if it hits numbers with special responses

        while target == 666 or target == 616:
            target = random.randint(minRange, maxRange)
        styleString(Fore.BLUE + Style.BRIGHT, "="*cols)
        if (maxRange - minRange) > 10000:
            print("Go big or go home!")
        if guesses >= 20 and (maxRange - minRange) <= 2000:
            print("You like things easy, huh?")

        # game

        for i in range(1,guesses+1):
            GuessCount = GuessCount + 1
            if i == 1 and not "yes" in choice2.lower():
                styleString(Fore.YELLOW, "You've entered a range of",minRange,"to",str(maxRange) + "!")
            elif i == 1 and "yes" in choice2.lower():
                styleString(Fore.YELLOW + "You've chosen a range of",minRange,"to",str(maxRange) + "!")
            else:
                styleString(Fore.YELLOW + "The range is",minRange,"to",str(maxRange) + "!")
            if i > 1 and gameMode == "easy":
                sorted(highGuess)
                sorted(lowGuess)
                print("\nThese are your high guesses:",highGuess)
                print("These are your low guesses:",lowGuess)
            print("\nYou are on guess",i,"out of",str(guesses)+"!")
            guess = int(input("Enter your guess: "))

            # special response to devil numbers

            if guess == 666 or guess == 616:
                print(Fore.RED + Style.BRIGHT + "\nYou tread on paths you don't understand, mortal.")
                choice = "no"
                break

            # win conditions + responses

            if guess == target and i == 1:
                styleString(Fore.YELLOW, "\nAgainst all odds, you won first try!")
                choice = input("\nDo you want to play again?")
                if "yes" in choice.lower():
                    styleString(Fore.BLUE + Style.BRIGHT, "="*cols)
                    continue
                else:
                    break
            elif guess == target:
                styleString(Fore.YELLOW, "\nYou guessed the target number!")
                choice = input("\nDo you want to play again? ")
                if "yes" in choice.lower():
                    styleString(Fore.BLUE + Style.BRIGHT, "="*cols)
                    continue
                else:
                    break

            # guessing higher or lower than target

            elif guess > target:
                print("\nYou guessed higher than the target number!")
                highGuess.append(guess)
                styleString(Fore.BLUE + Style.BRIGHT, "="*cols)
            else:
                print("\nYou guessed lower than the target number!")
                lowGuess.append(guess)
                styleString(Fore.BLUE + Style.BRIGHT, "="*cols)
    else:
        break

# end statements depending on actions

styleString(Fore.BLUE + Style.BRIGHT, "="*cols)
if guesses <= 0:
    print("You need to guess at least once!")
elif minRange == maxRange:
    print("Silly goose, you need a bigger range!")
elif guess == 666 or guess == 616:
    time.sleep(2)
    styleString(Fore.RED + Style.BRIGHT, "You lose.")
elif played == 1:
    print("Thanks for playing!")
else:
    print("Seems this game wasn't for you. Sorry!")

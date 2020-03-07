import random

playing = True

while playing == True:
    number = random.randint(1,2)
    guess = input("Heads or Tails: ")

    #Heads is thrown and guessed
    if number == 1 and guess == "heads":
        print("You flipped a heads and guessed a heads as well. GG Man")
        throw = input("Do you want to continue playng? ")


    #Tails is thrown and guessed
    elif number == 2 and guess == "tails":
        print("You flipped a tails and guessed tails as well.GGS Man")
        throw = input("Do you want to continue playing? ")


    #Heads is thrown and tails is guessed
    elif number == 1 and guess == "tails":
        print("You filpped a heads and guessed a tails. Tough luck.")
        throw = input("Do you want to continue playing? ")



    #Tails is thrown and heads is guessed
    elif number == 2 and guess == "heads":
        print("You flipped a tails and guessed a heads. Tough luck.")
        throw = input("Do you want to continue playing? ")


    #If neither Heads or tails is guessed
    else:
        print("Oops, you entered an incorrect value")
        throw = input("Do you want to try again? ")

    if throw == "yes":
        playing = True
    elif throw == "no":
         playing = False

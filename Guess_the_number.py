#Guess the number game ?
#read the range from the user for the number to be guessed between
import random
import math
print("\t\tGAME***GUESS THE NUMBER***GAME\n")
low=int(input("Enter lower range: "))
upper=int(input("Enter upper range: "))
key=random.randrange(low,upper)
#chances will be given for total of [log2(upper-lower+1)] times
chances=round(math.log2(upper-low+1))
print("\n\n\t\tYou will be given",chances,"chances to guess the number\n\n")
count=0
for i in range(chances):
    count+=1
    guess=int(input("\nGuess the number: "))
    if guess==key:
        print("\nCongrats you guessed the number in",count,"time")
        break
    if guess>key:
        print("\nguessed too high!")
    else:
        print("\nguessed too low!")
else:
    print("\nOops you lost the game!")
input('')

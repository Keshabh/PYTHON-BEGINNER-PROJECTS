#master-mind game
#2 player game: player 1 is computer, player 2 is the user.
#computer guess the number of 5 digits.
#player guesses the number
#if any digit mathes with the same position display it, else X.

import random
def Master_Mind():
    num=list(str(random.randrange(100,999)))
    l=['0']*3
    #player guesses the number
    count=0
    while True:
     try:
        count+=1
        inp=str(input("\n\nGuess the number: "))
        if ''.join(inp)==''.join(num) and count==1:
            print("Great! You guessed the number in just 1 try! You're a Mastermind!")
            break
        elif ''.join(inp)==''.join(num):
            print("\nYou've become a Mastermind.\nIt took you only {} tries.".format(count))
            break
        else:
            p=l.copy()
            for i in range(3):
                if inp[i]==num[i]:
                    l[i]=inp[i]
                else:
                    l[i]='X'
            if ''.join(p)==''.join(l):
                print("\nTry Hard\n")
            else:
                print("\nNot quite the number. But you did get some digits correct!\n\nAlso these numbers in your input were correct.\n")
            print(' '.join(l))
     except:
          continue



print("\n\t\t\t**Master Mind Game**\n")
print("Its a three number digit!")
Master_Mind()
input()

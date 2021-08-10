#21 number GAME
import random
#for instructions and permissions from the user
def Game_start():
    print("Player 2 is computer.")
    print("Do you want to start the Game?(Yes/No)")
    ans=input("> ")
    if ans.lower()=='no':
        return 0
    print("Enter 'F' to take the first chance.")
    print("Enter 'S' to take the second chance.")
    chance=input("> ")
    return chance.lower()
#main function
def Game():
        r=Game_start()
        if r==0:
            print("Better! Try it Next Time")
            return 0
        if r=='f':
            p=0 #if p==0 user will start the game
        else:
            p=1 # if p==1 computer will
        l=[0]
        #run it till anyone gets 21
        while True:
            #if user chose to start run this one first
            if p==0:
                print("\nYour Turn\n")
                print("How many numbers do you wish to enter?")
                n=int(input("> "))
                print("Enter your values")
                for i in range(n):
                    inp=int(input("> "))
                    #if input has 21, it means user has lost the Game.
                    if inp==21:
                        print("You Lost the Game.")
                        return 0
                    #check whether the input is consecutive to its previous input or not.
                    if inp==l[-1]+1:
                        l.append(inp)
                        continue
                    else:
                        print("Its not consecutive number, You Lost the Game.")
                        return 0
                #for alternate turn
                p=1
            elif p==1: #if user chose second to start
                ch=random.randrange(1,4)
                #add ch numbers of consecutive numbers in the list from l[-1]
                l1=list(range(l[-1]+1,l[-1]+ch+1))
                #if 21 in l1 by computer, it means user has won.
                if 21 in l1:
                    print("You Won the Match.")
                    return 0
                l=l+l1
                #display the list of numbers
                print("Order of inputs after computer's turn is:")
                print(l)
                #for alteernate turn
                p=0

Game()
input()

import random

def instructions():
    '''prints instructions'''
    print("\n\t\t*****Rock--Paper--Scissor--Game*****")
    print("\t\t--------------------------------------")
    print("\nwinning Rules of the Rock paper and scissor game as follows:\nrock vs paper -> paper wins\nrock vs scissors -> rock wins \npaper vs scissors -> scissors wins\n")
    print("Enter Choice\n1 for Rock\n2 for Paper\n3 for Scissor")

def read():
    '''takes input from user and computer'''
    global user_choice
    global comp_choice
    #take user input
    try:
        user_choice=int(input('\nUser Turn: '))
    except:
        print("**Enter a number b/w 1 and 3**\n")
        read()
    #take computer input
    comp_choice=random.choice([1,2,3])

def choice(n):
    if(n==1):
        return 'Rock'
    elif(n==2):
        return 'Paper'
    elif(n==3):
        return 'Scissor'
    else:
        read()

def game(user,comp):
    '''decides the winner'''
    print('User choice is',choice(user))
    print('\nNow its computer turn.......\n')
    print('computer choice is:',choice(comp))
    #decide
    if(user==1 and comp==2 or user==2 and comp==1):
        print("\n\tRock V/s Paper")
        print("\nPaper wins =>",end='')
        if(user==2):
            print('You win')
        else:
            print('Computer wins')
    elif(user==1 and comp==3 or user==3 and comp==1):
        print("\n\tRock V/s Scissor")
        print("\nRock wins =>",end='')
        if(user==1):
            print('You win')
        else:
            print('Computer wins')
    elif(user==2 and comp==3 or user==3 and comp==2):
        print("\n\tPaper V/s Scissor")
        print("\nScissor wins =>",end='')
        if(user==3):
            print('You win')
        else:
            print('Computer wins')
    else:
        print(choice(user),"V/s",choice(comp))
        print("\n* Its a Tie *")

def start():
    instructions()
    read()
    game(user_choice,comp_choice)
    again=input('\nDo u want to play again? (Y/N): ').lower()
    if again=='y':
        start()
    else:
        print('**Thank You**')


start()
input()

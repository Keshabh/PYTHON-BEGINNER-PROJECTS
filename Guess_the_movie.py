import random
def instructions():
    print("\n\t\t\t**Guess the word game**")
    name=input("Enter your name: ")
    print("\n\t\tYou will be given",turns,"chances to guess the word.")
    print("\nGood Luck",name)
    print('\nGuess movie name->',end=' ')

def print_word():
    print(' '.join(l))
words=[("sholay","Amitabh"),("lagaan","Aamir"),("barfi","Ranbir"),("queen","Kangana",),("devdas","Shahrukh"),("swadesh","shahrukh"),("nayak","Anil_Kapoor")]
word=random.choice(words)
hint=word[1]
word=word[0]
turns=len(word)+4
l=['_']*len(word)

instructions()
print_word()
print("Hint---",hint)
count=0
for i in range(turns):
    count+=1
    if '_' not in l:
       break
    letter=input("\nGuess a letter: ")
    #check for the letter in word
    u=0
    for j in range(len(word)):
        if word[j]==letter and l[j]=='_':
            l[j]=letter
            u+=1
    print_word()
    if u==0:
        print(' No such letter in the word!')
        print("chances left:",turns-count)
if '_' not in l:
    print("\n**Congrats You guessed the word**")
    print("\nNow Go and watch this movie ")
else:
    print("\nOops You Lost The Game !")
input('')

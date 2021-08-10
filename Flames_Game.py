#store flames
d={"F":"Friends","L":"Lovers","A":"Affection","M":"Marriage","E":"Enemies","S":"Sibling"}
f=['F','L','A','M','E','S']

def game(k):
    '''#finds one value from f list using k value returned by find_k function'''
    s=0
    for i in range(5):
       p=((s+k-1)%len(f))
       s=p%(len(f)-1)
       #pop element from f at index p
       f.pop(p)
    return f[0]

def find_k(s1,s2):
    '''returns length of uncommon letters'''
    s1=list(s1)
    s2=list(s2)
    c=s1.copy()
    for i in c:
        if i in s2:
            s1.remove(i)
            s2.remove(i)
    return len(s1+s2)

#main function
def start():
    '''takes user input'''
    print('\t\t\t***.F.L.A.M.E.S.***')
    print('\t\t-----------------------------------')
    s1=input("\nPlayer 1 name: ")
    s2=input("\nPlayer 2 name: ")
    result=d[game(find_k(s1,s2))]
    print('\nRelationship status: {}'.format(result))

start()
input()

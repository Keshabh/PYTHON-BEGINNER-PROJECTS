def display(a):
    mx=mn=a[0]
    print('Till Now Min.power\tTill Now Max.Power')
    for i in a:
        mx=max(i,mx)
        mn=min(i,mn)
        print('\t',mn,'\t\t\t',mx)

def game():
    print("\n\t\t\t*****P.O.K.E.M.O.N---T.R.A.I.N.I.N.G---G.A.M.E*****")
    print("\t\t--------------------------------------------------------------------")
    arr=list(map(int,(input("Enter pokemon powers in form of a an integer value: ").split())))
    print("Output: ")
    display(arr)

game()
input()

n=int(input("enter the number"))
for i in range(10,n+10,10):
    for j in range(i,10-10,-10):
        print(j,end=" ")
    print()
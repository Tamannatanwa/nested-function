i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end=" ")
        j=j+1
    k=1
    while k<i*2:
        print("*",end=" ")
        k=k+1
    i=i+1
    print()
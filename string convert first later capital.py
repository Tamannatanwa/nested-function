def str(b):
    i=0
    a=b.split()
    while i<len(a):
        j=0
        while j<len(a[i]):
            if j==0:
                print(a[i][j].upper(),end='')
            else:
                print(a[i][j],end="")
            j=j+1
        i=i+1
        print(end=" ")
b="my name is jyoti"
str(b)

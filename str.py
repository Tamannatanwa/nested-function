def num(a):
    b=a.split()
    i=0
    while i<len(b):
        j=0
        while j<len(b[i]):
            if j==0:
                print(b[i][j].upper(),end="")
            else:
                print(b[i][j],end="")
            j=j+1
        i=i+1
num("tamanna tanwar")
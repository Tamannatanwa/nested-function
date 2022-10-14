def a(x):
    i=0
    b=[]
    n=30
    while i<len(x):
        j=0
        c=[]
        while j<len(x):
            if x[i]+x[j]==30 and x[j]>x[i]:
                c.append(x[i])
                c.append(x[j])
                b.append(c)
            j=j+1
        i=i+1
    print(b)
list=[20,5,10,23,25,7]
a(list)
        
        

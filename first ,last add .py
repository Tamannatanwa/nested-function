def a():
    x=[5,4,0,1,9]
    y=x[::-1]
    i=0
    b=[]
    while i<len(x)/2:
        n=x[i]+y[i]
        b.append(n)
        i=i+1
    print(b)
a()
def sum(a,b):
    i=0
    c=[]
    sum=0
    while i<len(a):
        sum=a[i]+b[i]
        c.append(sum)
        i=i+1
    print(c)
a=[5,6,7]
b=[10,6,20]
sum(a,b)
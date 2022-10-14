a=[1,2,3,4]
i=-1
b=[]
while i>-len(a):
    num=[a[0],a[i]]
    b.append(num)
    i=i-1
print(b)


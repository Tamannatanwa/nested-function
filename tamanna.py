a=["p","q"]
i=0
b=[]
while i<len(a):
    j=1
    while j<=5:
        num=a[i]+str(j)
        b.append(num)
        j=j+1
    i=i+1
print(b)
a=[
    [8,3,4],
    [1,5,9],
    [6,7,2]
]
i=0
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum+=a[i][j]
        j=j+1
    i=i+1
print(sum)
i=0
while i<len(a):
    j=0
    num=0
    while j<len(a[i]):
        num+=a[j][i]
        j=j+1
    i=i+1
print(num)
i=0
index=0
count=0
while i<len(a) :
    j=2
    while j<len(a):
        count+=a[i][index]
        j=j+2
        index+=1
    i=i+1   
print(count)
i=0
index=2
so=0
while i<len(a):
    j=2
    while j<len(a):
        so+=a[i][index]
        j=j+2
        index-=1
    i=i+1
print(so)
        
        
if sum==num==count==so:
    print(a,"it is magic square")
else:
    print(a,"it is not a magic square")

    
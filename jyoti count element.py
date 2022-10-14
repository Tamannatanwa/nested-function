n=input("enter the name...")
a=["books","students",["books","students","books","students"]]
i=0
count=0
co=0
c=0
while i<len(a):
    if type (a[i])==list:
        j=0
        while j<len(a[i]):
            if a[i][j]==a[0]:
                count+=1
            elif a[i][j]==a[1]:
                co+=1
            j=j+1
    else:
        if a[i]==a[0]:
            count+=1
        elif a[i]==a[1]:
            co+=1
    c=c+1
    i=i+1
print(count,a[0])
print(co,a[1])
print(c,n)

a=[10,20,[30,40,[50,60],70],80]
# O/P [10,20,[30,40,[50,60,7000],70],80]
i=0
b=[]
while i<len(a):
    if type (a[i])==list:
        j=0
        n=[]
        while j<len(a[i]):
            if type (a[i][j])==list:
                k=0
                c=[]
                while k<len(a[i][j]):
                    c.append(a[i][j][k])
                    k=k+1
                c.append(7000)
                n.append(c)
            else:
                n.append(a[i][j])
            j=j+1
        b.append(n)
    else:
        b.append(a[i])
    i=i+1
print(b)



                    

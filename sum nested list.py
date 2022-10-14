def sum(x):
    i=0
    sum=0
    while i<len(x):
        j=0
        while j<len(x[i]):
            sum+=x[i][j]
            j=j+1
        i=i+1
    print(sum)
              
a=[[6,9,2]]
sum(a)
    
def count():
    a="ABCDCDCD"
    i=0
    b=[]
    count=0
    while i<len(a):
        if a[i] not in b:
            b.append(a[i])
            count+=1
        i=i+1
    print(count)
count()
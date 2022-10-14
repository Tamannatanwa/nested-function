def mul(a):
    i=0
    num=int(a[i])
    while i<len(a)-1:
        num*=int(a[i+1])
        i=i+1
    print(num)
a="1234567"
mul(a)

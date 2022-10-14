def num(a):
    i=0
    num=int(a[i])
    m=max(a)
    while i<len(a)-1:
        num*=int(a[i+1])
        i=i+1
    print(num)
a="1234567"
num(a)


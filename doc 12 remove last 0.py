def zeros(a):
    j=-10000
    while j<a:
        if a%10==0:
            a=a//10
        j=j+1
    print(j)
zeros(int(input("enter the number...")))

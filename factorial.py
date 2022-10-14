def power(x):
    fac=1
    while x>0:
        fac=fac*x
        x=x-1
    print(fac)
n=int(input("enter the number"))
power(n)


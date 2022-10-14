def fac(x):
    if x==1:
        return 1
    else:
        return(x*fac(x-1))
# n=int(input("enter the number........... "))
# z=fac(n)
z=fac(int(input("enter the number.....")))
print(z)

    

def power(x,y):
    if y==0:
        return 1
    else:
        return (x*power(x,y-1))
    
n=int(input("enter the number"))
v=int(input("enter the number"))
power(n,v)
print(power(n,v))





    
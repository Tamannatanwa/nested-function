
# def fun(a,b):
#     average=(a+b)/2
#     print(average)
# fun(5,7)
# def g(a,b):
#     average=(a+b)/2
#     fun(6,7)
#     return average
# n=g(5,7)
# print(n)



def rev(n,i):
    if i==0:
        print(n[0])
    else:
        print(n[i],end="")
        rev(n,i-1)
n=input("enter the character.....")
rev(n,len(n)-1)





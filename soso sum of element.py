# def a(n):
#     if n==1:
#         return 1
#     else:
#         return n+a(n-1)
# print(a(10))


def sum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return sum(n-1)+sum(n-2)
c=int(input("enter the number.."))
b=int(input("enter the number.."))
for n in range(c,b+1):
    print(sum(n))

   

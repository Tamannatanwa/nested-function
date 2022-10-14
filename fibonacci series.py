# x=0
# y=0
# z=1
# def a(n):
#     global x,y,z
#     if n>=0:
#         x=y
#         y=z
#         z=x+y
#         print(z)
#         return a(n-1)
# n=int(input("enter the number="))
# a(n)

# def sum(a):
#     if a==1:
#         return 1
#     else:
#         count=(a+sum(a-1))
#         return(a+sum(a-1))
# x=sum(int(input("enter the number=")))
# print(x)



# def a(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     return a(n-1)+a(n-2)
# n=int(input("enter the number.."))
# for i in range(n,n+1):
#     print(a(i))
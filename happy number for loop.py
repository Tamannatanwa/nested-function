# i=int(input("enter the number"))
# a=i
# while a>10:
#     sum=0
#     while a>0:
#         b=a%10
#         sum=sum+b**2
#         a=a//10
#     a=sum
# if sum==1:
#     print(i,"happy number")
# else:
#     print(i,"unhappy number")
    
    
    
i=int(input("enter the number."))
a=i
for i in range(10,a):
    sum=0
    for i in range (0,a):
        b=a%10
        sum=sum+b**2
        a=a//10
    a=sum
if sum==1:
    print(a,"happy number")
else:
    print(a,"not happy number")
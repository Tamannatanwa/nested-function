# a=50
# n=100
# for count in range (a,n+1):  
#     for i in range (2,count):  
#         if count%i==0:  
#             break
#     else:  
#         print("Prime number=",count)



def prime(a,b):
    while a<=b:
        j=1
        count=0
        while j<=a:
            if a%j==0:
                count+=1
            j=j+1
        if count==2:
            print(a,"prime")
        a=a+1
a=int(input("enter the number"))
b=int(input("enter the number"))
prime(a,b)
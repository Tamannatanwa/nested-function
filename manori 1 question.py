# i=0
# num=0
# def add(a,b):
#     global num
#     global i
#     if b==0:
#         return 1
#     else:
#         num+=int(a[i])
#         i=i+1
#     add(a,b-1)
# n=input("enter the number.")
# add(n,len(n))
# print(num)
# if num%2==0:
#     print("even number",num)
# else:
#     print("odd number",num)
        
        
        
num=0
sum=0
def add(n):
    global num
    global sum
    if n>0:
        num+=n%10
        return add(n//10)
    elif num>0:
        sum+=num%10
        num=num//10
        add(n)
add(int(input("enter the numnber...")))
if sum%2==0:
    print("even",sum)
else:
    print(sum,"odd numnber..")
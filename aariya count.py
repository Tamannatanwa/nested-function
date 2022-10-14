a=input("enter the number....")
i=0
b=[]
while i<len(a)-1:
    num=int(a[i])*int(a[i+1])
    b.append(num)
    i=i+1
print(max(b))
# j=0
# max=0
# while j<len(b):
#     sum=b[j]
#     if sum>max:
#         max=sum
#     j=j+1
# print(max)

a=input("enter the number...")
i=0
num=0
while i<len(a):
    num+=int(a[i])
    i+=1
if num>=1 and num<=9:
    if num%2==0:
        print("even number",num)
    else:
        print("odd number",num)
else:
    j=0
    c=str(num)
    sum=0
    while j<len(c):
        sum+=int(c[j])
        j=j+1
    if sum%2==0:
        print("even number" ,sum)
    else:
        print("odd number",sum)
        
  
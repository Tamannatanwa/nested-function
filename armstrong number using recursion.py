sum=0
def ams(n,i):
    global sum
    if n<=0:
        return 0
    else:
        r=n%10
        sum+=(r**i)
        ams(n//10,i)
n=int(input("enter the number.."))
ams(n,len(str(n)))
if n==sum:
    print(sum,"armstrong number..")
else:
    print(sum,"not armstrong number..")
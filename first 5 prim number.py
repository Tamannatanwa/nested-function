n=2
count=0
isprime=True
while count<10:
    i=2
    while i<n:
        if n%i==0:
            isprime=False
        i=i+1
    if isprime:
        print (str(n)+"is prim")
        count+=1
    n=n+1
        
        
# def sum(a,b):
          
#     ans=sum(5,6)+sum(2,3)
#     print(ans)



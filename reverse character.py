def rev(s,n):
   if n==0:
       print(s[0])
   else:
       print(s[n],end="")
       rev(s,n-1)
s=input("enter character.....")
rev(s,len(s)-1)





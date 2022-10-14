def password():
    a=0
    b=0
    c=0
    d=0
    s=input("enter the passsword:")
    capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets="abcdefghijklmnopqrstuvwxyz"
    specialcharacters="@&!_#?"
    digits="0123456789"
    if (len(s)>=6) and len(s)<=11:
        for i in s:
            if (i in capitalalphabets):
                a=a+1
            if (i in smallalphabets):
                b=b+1
            if (i in specialcharacters):
                c=c+1
            if (i in digits):
                d=d+1
    if (a>=1 and b>=1 and c>=1 and d>=1 and (a+b+c+d)==len(s)):
        print("strong paasword")
    else:
        print("weak password")
password()
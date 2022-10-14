def a(n):
    v=n*75
    return v
def b(m):
    b=m/75
    return b
def s():
    print("1. us $ to rupee")
    print("2.rupee to us $")
    choose=int(input("enter your choice."))
    if choose==1:
        print(a(int(input("enter the doller"))))
    else:
        print(b(int(input("enter the rupee"))))
s()

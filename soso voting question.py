# def a(name):
#     if name=="tamanna":
#         return name
#     else:
#         return False
# def b(age):
#     print(a(input("enter the name...")))
#     if age>=18:
#         return age
#     else:
#         return False
# def choose(n):
#     print(b(int(input("enter the age.."))))
#     c=int(input("enter your choice..."))
#     if c==n[1]:
#         return n[1]
#     else:
#         return n[0]
# n=["BJP","CONG"]
# print(choose(n))




def a(name):
    if name=="tamanna":
        return name
    else:
        return False
def b(age):
    if age>=18:
        return age
    else:
        return False
def choose(n):
    v=a(input("enter the name..."))
    if v=="tamanna":
        c=b(int(input("enter the age...")))
        if c>=18:
            choose=int(input("choose your party.."))
            if choose==0:
                print("congrats,eligible for voting")
                print(n[0])
            else:
                print("congrats ,eligible for voting")
                print(n[1])
        elif c==False:
            print("not eligible")
    elif v==False:
        print("enter valid name")
n=["BJP","CONG"]
choose(n)          



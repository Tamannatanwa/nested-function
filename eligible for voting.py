def a(name):
    if name=="tamanna":
        return True
    return False
def b(age):
    print(a(input("enter the name..")))
    if age>=18:
        return True
    return False
print(b(int(input("enter the age..."))))
m=input("enter the name..")
n=int(input("enter the age.."))
if m=="tamanna":
    if n>=18:
        print("eligible")
    else:
        print("not eligible")
else:
    print("enter correct name")
    



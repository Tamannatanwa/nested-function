def a(name):
    pass
def b(age):
    if name=="tamanna":
        if age>=18:
            print("1.BJp")
            print("2.CONG")
            choose=int(input("enter your choice.."))
            print("eligible for voiting")
            return "congrats"
        else:
            return "not eligible"
    else:
        return "invalid"
    
name=input("enter you name=")
age=int(input("enter the age="))
print(b(age))
print(a(name))







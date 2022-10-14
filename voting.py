# def num(name,age):
#     if name=="tamanna":
#         if age>=18:
#             print("1.BJP")
#             print("2.CONG")
#             print("3.AAP")
#             choose=int(input("enter the number...."))
#             print("congrates","you are eligible for voting")
#         else:
#             print(name,"not eligible for voting")
#     else:
#         print("invalid name")
# a=input("enter the name....")
# b=int(input("enter the age....."))
# num(a,b)




def a(name):
    def show(age):
        if name=="tamanna":
            if age>=18:
                print("1.BJP")
                print("2.CONG")
                print("3.AAP")
                print("4.ANOTHER")
                choose=int(input("enter your party..."))
                print("congrats",name)
                print("eligible for voting")
            else:
                vote=18-age
                print("not eligible")
                print(vote,"weight ")
        else:
            print("enter valid name")
    show(int(input("enter the age..")))
a(input("enter the name...."))





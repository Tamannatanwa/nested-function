print("WELCOME TO SBI BANK")
atm_pin=1234
amount=20000
def quite():
    a=input("press yes to quit")
    if a=="yes":
        print("thanks for visiting")
    else:
        print("choose transaction")
def transfer_money():
    a=int(input("enter the amount.."))
    if a>0:
        b=amount-a
        print("successfully transfer")
        print("present amount=",b)
        quit()
    else:
        print("enter valid amount")
def deposit():
    a=int(input("enter the deposit amount.."))
    if a>0:
        available=amount+a
        print(available,"total case")
        quit()
    else:
        print("enter valid amount")
def a():
    print("do you want using card")
    print("1.start")
    print("2.quit")
    choose=int(input("enter your choice.."))
    if choose==1:
        pin=int(input("enter the pin"))
        if pin==atm_pin:
            print("choose your transcation")
            print("1.transfer money")
            print("2.deposit money")
            print("3.quit")
            choice=int(input("enter the choice.."))
            if choice==1:
                m=transfer_money()
            elif choice==2:
                b=deposit()
            else:
                d=quite()
        else:
            print("enter valid ")
    else:
        q=a()
a()
        
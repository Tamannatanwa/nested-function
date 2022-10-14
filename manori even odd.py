def even_odd(a):
    if a==0:
        return 1
    else:
        if a%2==0:
            print(a,"even")
        else:
            print(a,"odd")
    even_odd(a-1)
even_odd(int(input("enter the number..")))





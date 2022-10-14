count=0
def sum(a):
    global count
    if a==0:
        return 1
    else:
        count+=a
        print(count)
    sum(a-1)
sum(int(input("enter the number..")))




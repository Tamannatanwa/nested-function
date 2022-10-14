def table(a):
    if a==1:
        return 1
    else:
        print(2*table(a-1))
table(10)
    
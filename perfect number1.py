def perfect(a):
    sum=0
    i=1
    while i<a:
        if a%i==0:
            sum+=i
        i=i+1
    if sum==a:
        print(sum,"it is perfect number")
    else:
        print(sum,"not perfect number")
perfect(int(input("enter the number")))
        
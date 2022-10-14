def max(n):
    firstmax=0
    secondmax=0
    thirdmax=0
    i=0
    while i<len(n):
        num=n[i]
        if num>firstmax:
            thirdmax=secondmax
            secondmax=firstmax
            firstmax=num
        elif num>secondmax:
            thirdmax=firstmax
            secondmax=num
        elif num>thirdmax:
            thirdmax=num
        
        i=i+1
    print(firstmax)
    print(secondmax)
    print(thirdmax)
n=[-1,-2,-3,4,5,6]
max(n)
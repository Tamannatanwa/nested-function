# def mul(n):
#     mul=1
#     for i in n:
#         mul*=i
#     return mul
# a=[2,3,4,5]
# print(mul(a))




# def mul(n):
#     mul=1
#     i=0
#     while i<len(n):
#         mul*=n[i]
#         i=i+1
#     return mul
# a=[2,3,4,5]
# print(mul(a))



def max(n):
    firstmax=0
    # secondmax=0
    i=0
    while i<len(n):
        secondmax=n[i]
        num=n[i]
        if num>firstmax:
            firstmax=num
        elif firstmax>secondmax:
            secondmax=firstmax
        i=i+1
    secondmax=firstmax
    print(firstmax)
    print(secondmax)
n=[-1,-2,-3,4,5,6]
max(n)








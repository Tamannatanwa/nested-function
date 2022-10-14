# def rec(a):
#     if a==1:
#         return 1
#     else:
#         return a*rec(a-1)
# x=rec(5)
# print(x)


def rec(a):
    if a==1:
        return 1
    else:
        return a+rec(a-1)
x=rec(5)
print(x)
# def a(num):
#     if num==1:
#         return 1
#     else:
#         return a(num-1)+3
# print(a(5))





def a(n):
    if n==1:
        return 10
    elif n%2==0:
        return a(n-1)+1
    else:
        return a(n-1)*10
n=[10,11,110,111,1110,1111,11110,11111,111110,111111]
print(a(n))









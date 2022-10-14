a=[10,50,60,80,90,5,45,65]
def x(n):
    if n>=60:
        return True
r=list(filter(x,a))
print(r)
for i in r:
    print(i)
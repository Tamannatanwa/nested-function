def product(i,num):
    if i==len(num)-1:
        return int(num[i])
    else:
        return int(num[i])*product(i+1,num)
name=input("enter the number:")
print(product(0,name))
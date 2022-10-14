# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# a=int(input("enter the num1..."))
# b=int(input("enter the num2..."))
# c=input("enter the oprator....")
# if c=="+":
#     print(add(a,b))
# elif c=="-":
#     print(sub(a,b))
# elif c=="*":
#     print(mul(a,b))
# elif c=="/":
#     print(div(a,b))





# def cal(a,b,op):
#     if op=="add":
#         a=add()
#     elif op=="sub":
#         a=sub()
#     elif op=="mul":
#         a=mul()
#     elif op=="div":
#         a=div()

# result=cal(2,6,add)
# print(result)
        
        
        
        
        
        
        
        
        
        
        
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def sum(a,b,c):
    if c=="+":
        v=add(a,b)
    elif c=="-":
        v=sub(a,b)
    elif c=="*":
        v=mul(a,b)
    elif c=="/":
        v=div(a,b)
sum(2,3,"+")

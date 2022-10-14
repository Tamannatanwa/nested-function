def disp(sh):
    print("disp function",sh())
def show():
    return "show function"
disp(show)



def a(n):
    return ("ram",n())
def b():
    return "sita"
print(a(b))
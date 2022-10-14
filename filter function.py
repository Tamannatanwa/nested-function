# def a(*num):
#     print(num)
# a(1,2,3,4)




def add(**nam):
    print(nam["a"]+nam["b"]+nam["c"])
add(a=5,b=2,c=4)
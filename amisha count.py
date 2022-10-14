# def a(count):
#     i=0
#     b=[]
#     c=[]
#     while i<len(count):
#         if i==0 or i==1:
#             b.append(count[i])
#         else:
#             c.append(count[i])
#         i=i+1
#     print([b]+c)
# count=[2,27,22,23,8,91,24,2]
# a(count)



def a(count):
    i=0
    while i<len(count):
       num=[count[i],count[i+1]]
       print(num)
       i=i+2
count=[2,27,22,23,8,91,24,2]
a(count)
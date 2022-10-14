# def table(a):
#     if a>0:
#         rev=2*table(a-1)
#         print(rev)
#     else:
#         rev=1
#     return rev
# table(10)



# def sum(a):
#     if a<=10:
#         rev=2*sum(a+1)
#         print(rev)
#     else:
#         rev=1
#     return rev
# sum(2)



def sum(a): 
    if a>1:

        # print(sum(a-1))
        sum(a-1)
    # return 2*a
    print(2,"*",a,"=",2*a)
sum(10)



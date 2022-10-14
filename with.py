# a=open("with.txt","w")
# try:
#     a.write("tamanna\naniket\namrita\npriya")
# finally:
#     a.close()



a=open("with.txt","w")
l =["priya\n","amrita"]
b=a.writelines(l)
print(b)
a.close()
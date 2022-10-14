a=["my name is tamana"]
i=0
b=""
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j]==" ":
            b+="-"
        else:
            b+=a[i][j]
        j=j+1
    i=i+1
print('"'+b+'"')
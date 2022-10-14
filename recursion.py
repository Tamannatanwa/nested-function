def a(k):
    if k>0:
        result=k+a(k-1)
        print(result)
    else:
        result=0
    return result
print("pagal")
a(6)
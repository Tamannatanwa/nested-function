def max(a):
    i=0
    maximum=0
    while i<len(a):
        num=a[i]
        if num>maximum:
            maximum=num
        i=i+1
    print(maximum)
max_2=[89,2,4,87,89,84,27,28]
max(max_2)
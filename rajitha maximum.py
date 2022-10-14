b=[50,9,2,3,7,45]
i=0
max=0 
smax=0
tmax=0
min=b[i]
smin=b[i]
tmin=b[i]
while i<len(b):
    if b[i]>max:
       tmax=smax
       smax=max
       max=b[i]
    elif b[i]>smax:
        tmax=smax
        smax=b[i]
    elif b[i]>tmax:
        tmax=b[i]
    if b[i]<min:
        tmin=smin
        smin=min
        min=b[i]
    elif b[i]<smin:
        tmin=smin
        smin=b[i]
    elif b[i]<tmin:
        tmin=b[i]
    i=i+1
print(max)
print(min)
print(smax)
print(smin)
print(tmax)
print(tmin)
a=max*min
b=smax*smin
c=tmax*tmin
print(a+b+c)



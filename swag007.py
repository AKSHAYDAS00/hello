c=("danger","ahead","man")
print(c)
print(len(c))
print(type(c))
d=(2,)
print(type(d))


f=("swipe",2,"get",8,"never","settle",4,5,9,6,2,4)
print(f)
print(f[2])
print(f[1:3])
print(f[2:])
print(f[2:8:2])
#k=[1,2,3,4,5]
print(f[::4])
#[start:end:step]
print(f[-8])
print(f[-11:-6])
x=list(f)
x[3]=9
print(x)
x[2:5]=(5,6,7)
print(x)
z=tuple(x)
print(z)
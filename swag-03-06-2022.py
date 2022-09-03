x=("sam","ram",3,"cam",9,"pam",7)
z=list(x)
z.remove("ram")
print(z)
del z[2]
print(z)
z.append(9)
print(z)


#UNPACKING
v=("bike","auto","car")
(a,b,c)=v  #unpacking
print(c)

l=("fan","belt","air","condition","gas","refill")
(a,b,*c,d)=l
print(d)

#join
z=(9,8,7)
y=(6,5,4)
x=z+y
print(x)
x=y+z
print(x)

a=("hello")
b=2
c=a*b
print(c)

x=(1,0)
y=x*3
print(y)

#count&index
o=(2,4,7,6,4,9,8,7,6,7,5,4,2,3,7,5,7,3,5,7,6,3,7)
print(o.count(7))
print(o.index(6))
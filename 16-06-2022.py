p = 50
t = "the prize of pen is {}".format(p)
print(t)

p = 20000
i = "car"
no = 2

#string
t = "the price of {} {} is {}Rs".format(no, i, p)
print(t)

#indexed string formating
t = "the price of {2} {0} is {1}Rs".format(i, p, no)
print(t)

#named index formating
t = "the price of {c} {b} is {a}Rs".format(a=p,b=i,c=no)
print(t)

#floating number formating
t = "the price of {:.2f} {} is {:.2f} Rs".format(no, i, p)
print(t)


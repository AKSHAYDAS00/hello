def h():
    print("hello world")
h()


def k():
    print(10+3)
k()



def bigb(teacher):
    print(teacher+"  " +"john")
bigb("bilal")
bigb("killadi")



def bigb(teacher,student):
    print(teacher+"  " +student)
bigb("bilal","john")
bigb("killadi","vasu")


def sum(num1,num2):
    print(num1+num2)
sum(5,7)



def function(*a):
    print("my name is"+"  "+a[1])
function("john","peter","abu")



def function(a,b):
    print("my name is"+"  "+a)
function(a="john",b="peter")


def function(**name):
    print("my name is"+"  "+name["a"])
function(a="sam",b="mery")


def taste(item):
    for i in item:
        print(i)
    f=["kiwi","mango","pineapple"]
taste(f)



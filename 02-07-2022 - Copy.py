#Raise an exception

n = int(input("enter the number"))
if n<1:
    raise Exception("NO NUMBER LESS THAN")


n=str(input("enter a string:"))
if not type(n) is int:
    raise TypeError("only integer allowed")


#CLASS & OBJECT

class Student:
     def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Anu",20)
print(s1.name)
print( s1.age)


class Car:
    def __init__(self,color,year):
        self.color=color
        self.year=year
c1=Car("red",2005)
c2=Car("blue",2009)
print(c1.color)
print(c1.year)
print(c2.color)
print(c2.year)


class Car:
    def __init__(love,color,year):
        love.color=color
        love.year=year
    def Method(love):
        print("color of car is"+"  "+love.color)
c=Car("red",2004)
c.Method()

#modify object propperties
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = Student("Anu", 20)
s1.age=25    #this is the modifying line
print(s1.name)
print(s1.age)


#delete object properties
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = Student("Anu", 20)
del s1.age      #deleting  line
print(s1.name)
print(s1.age)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = Student("Anu", 20)
del  s1   #deleting object
print(s1)




class Student:
    pass


class Text:
    def __init__(self,m):
        self.m=m
t1=Text("HELLO WORLD")
print(t1.m)


class abc:
    def fun(self):
        print("hello world")
obj=abc()
obj.fun()


#factorial of number using class function


#using while loop
class factorial:
    def factor(x):
        i=1
        fact=1
        n=int(input("enter a number :"))
        while i<=n:
            fact=fact*i
            i=i+1
        print(fact)
k1=factorial()
k1.factor()


#using for loop
class factorial:
    def factor(x):
        fact=1
        n=int(input("enter a number :"))
        for i in range(1,(n+1)):
            fact=fact*i
        print(fact)
k1=factorial()
k1.factor()


class Bank:
    def sbi(self):
        b=100000
        print("current balance is",b)
        n=str(input("DO YOU WANT TO WITHDRAW  :"))
        if(n=="yes"):
            a=int(input("amount :"))
            b=(b-a)
            print("current balance is :",b)
        else:
            x=str(input("DO YOU WANT TO DEPPOSIT :"))
            if(x=="yes"):
                    z=int(input("ENTER THE AMOUNT :"))
                    b=(b+z)
                    print("current balance is :",b)
            else:
                    print("thank you for banking with us")
d1=Bank()
d1.sbi()
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))


num = 4
print("factorial is ", (factorial(num)))


# sum of n natural _ student version
def sum(x):
    if x == 0:
        return 0
    else:
        return (x + sum(x - 1))


num = 8
print("the sum of n numbers is", sum(num))


# teachers version

def sum(x):
    if x <= 1:
        return x
    else:
        return x + sum(x - 1)


num = 4
if num < 0:
    print("enter positive number")
else:
    print("sum is", sum(num))

# Lambda function
n = lambda x: x + 10
print(n(5))

n = lambda a, b, c, d: a * b * c * d

print(n(2, 9, 3, 2))

n = lambda a, b: a % b
print(n(40, 3))


#lambda using function
def fun(c):
   return lambda a:a*c
y=fun(10)
print(y(20))


def sum(j):
   return lambda q:q+j
z=sum(10)
print(z(20))


#exception Handling

#try-except
try:
    print(x)
except:
    print("x is not defined")

#try-except-else
x=10
try:
    print(x)
except:
    print("error")
else:
    print("no error")



try:
    print(d)
except NameError:
    print("not defined")
except:
    print("something went wrong")
finally:
    print("completed")







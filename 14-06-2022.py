# conditional statement

# if statement

a, b = 10, 20
if b > a:
    print("hello")

c, d = 100, 100
if c == d:
    print("equal")

e, f = 20, 40
if e != f:
    print("not equal")

g, h = 12, 14
if h >= g:
    print("done")
# elif
k, l = 10, 20
if k == l:
    print("its equal")
elif (k != l):
    print("its not eqal")

# else statement

y, z = 40, 70
if y >= z:
    print("its greater or equal")
else:
    print("hello")

x = 2
y = 3
if x > y:
    pass

# short hand if
x = 1
y = 2
if y > x: print("hi")  # this technique is called Ternary Operators / Conditional Expression

a = 40
b = 20
c = 30
if a > b and c < a: print("condition 1")
if b > c or a > b: print("condition 2")

x = 10
y = 25
z = 10
a = 25
if a == y and x == z: print("condition 3")
if z == a or y == a: print("condition 4")

h = 2
i = 4
j = 2
if h >= j and i >= h: print("condition 5")
if j >= i or h >= j: print("condition 6")

# Q: largest of 2 numbers

a = 23483556767687694387546768965453539685754675435
b = 23483565786557875684567545567567623765756465755
if a > b:
    print("a is the largest number")
elif (a == b):
    print("a & b are equal")
else:
    print("b  is the largest number")

# ODD OR EVEN
x = 3465435
if (x % 2) == 1:
    print("the number is odd")
else:
    print("the number is even")

# NESTED IF

a = 75340
b = 4534456280
c = 645545657575752330
if (a > b):
    if (a > c):
        print("a is the largest number")
    else:
        print("c is the largest number")
elif (b > c):
       print("b is the largest number")
else:
    print("c is greater")




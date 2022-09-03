# in
f = {"iam", "enfforcing", "the", "army"}
print("arm" in f)

# update-set to set
a = {2, 5, 9, 5, 2}
b = {3, 7, 10, 6, 4}
a.update(b)
print(a)

#update- list to set
a = {2, 5, 9, 5, 2}
b = [3, 7, 10, 6, 4]
a.update(b)
print(a)
#update tuple to set
a = (2, 5, 9, 5, 2)
b = {3, 7, 10, 6, 4}
b.update(a)
print(b)

#remove
a = (2, 5, 9, 5, 2)
b = {3, 7, 10, 6, 4}
b.update(a)
b.remove(5)
print(b)

#discard    (does not out error)
b = {3, 7, 10, 6, 4}
b.discard(10)
print(b)
print(10 in b)

#pop
b.pop()
print(b)
b.pop()
print(b)
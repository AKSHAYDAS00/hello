# union
a = {2, 4, 6, 8}
b = {1, 3, 5, 7}
c = a.union(b)     #returns a set that contains all items from the original set, and all items from the specified set(s)
print(c)

# intersection
x = {1, 2, 3, 4, 5}
y = {2, 4, 6, 8}
z = x.intersection(y)     # returns a set that contains the similarity between two or more sets.
print(z)

# intersection-update
l = {1, 2, 3, 4, 5}
m = {2, 4, 6, 8}
l.intersection_update(m)    #The intersection of two or more sets is the set of elements which are common to all sets
print(l)

# difference
v = {"car", "bike", "troy", "buggy"}
w = {"bike", "troy"}
e = v.difference(w)     #returns a set that contains the difference between two sets.
print(e)

# difference_update()
i = {"car", "bike", "troy", "buggy"}
j = {"car", "buggy"}
i.difference_update(j)      # difference_update() method helps in an in-place way of differentiating the set
print(i)

# symmetric_difference()

q = {"ban", "can", "man", "pan"}
r = {"ban", "pan"}
s = q.symmetric_difference(r)
print(s)

# symmetric_difference_updte()
g = {"ban", "can", "man", "pan"}
h = {"man", "can"}
g.symmetric_difference_update(h)   # returns the symmetric difference of two sets
print(g)

# isdisjoint()
g = {"ban", "can", "man", "pan"}
h = {"mac"}
i = g.isdisjoint(h)     #do not have any common element in between them. Set A and set B are said to be disjoint sets as their intersection is null.
print(i)

# issubset
g = {"ban", "can", "man", "pan"}
h = {"man", "pan"}
b = h.issubset(g)                  # find the subset of a parent
print(b)

# issuperset
g = {"ban", "can", "man", "pan"}
h = {"man", "pan"}
x = g.issuperset(h)                # find the parent of a sub set
print(x)

#copy
p={"car",8,5,"fast","drop","meter",3}
q=p.copy()                       # similar to  ( q=p )
print(q)
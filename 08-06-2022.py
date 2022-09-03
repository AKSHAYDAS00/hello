car = {"model": "nano", "brand": "tata", "year": 2005}
x = car["brand"]  # find value using key
print(x)

o = len(car)  # length of dictionary
print(o)

x = car.keys()  # used to get the keys
print(x)

y = car.values()
print(y)  # used to get values

z = car.items()  # returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

print(z)
p = type(car)  # find the type
print(p)

cap = dict(addidas="white", puma="navy")  # construct dictionary using dict.
print(cap)
cap['addidas'] = "yellow"  # change items using key
print(cap)

car.update({"year":2003})  #change/ update the items
print(car)

car["color"]="blue"     # add new items
print(car)

car.update({"alignment":"done"})   #add new item using update method
print(car)

car.pop("model")   #erase one item
print(car)

car.popitem()  #delete the last item
print(car)

del car["year"] #delete a item
print(car)
#del car         #delete a entire  dict.
print (car)

car.clear() #clear
print(car)

car=cap.copy() #copy one to anoher
print(car)
x=car
print(x)

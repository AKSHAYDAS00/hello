details = {"no": 1, "name": "athira", "age": 22, "class": "bca", "college": "ihrd"}
print(details)

x=details.copy()
print(x)


details.update({"name":"Athira u r"})
print(details)

details.update({"age":21})
print(details)

z=dict(details)
print(z)

details.update({"name":"Athira k s"})
print(details)
print(z)

m={"student1":{"name":"athira","year":2000},
   "student2":{"name":"swag","year":2001},
   "student3":{"name":"aks", "year":2003}}
print(m)
print(m.get("student2"))
print(m.get("student2").get("name"))
print(m.get("student1").get("year"))     #getting access of a nested dict. key
print(m["student2"]["year"])

a = {"name": "swag", "death": 2022, "age": 43}
b = {"name": "athira", "death": 2020, "age": 21}
c = {"name": "aks", "death": 2021, "age": 20}

z={"student1":a,"student2":b,"student3":c}
print(z)
print(z.get("student2").get("age"))
print(z["student3"]["death"])


#fromkeys()  - same values for all key

x=("car","bike","lorry","auto")
y=(4)
vehicle=dict.fromkeys(x,y)
print(vehicle)

import platform,damn,datetime,calendar,time,sys    # import module
x=platform.system()   #import function
print(x)
z=dir(platform)
print(z)
d=dir(damn)
print(d)


#date time
g=datetime.datetime(2000,9,19)
print(g)
print(g.year)
print(g.strftime("%A"))
print(calendar.month(2022,11))
print(time.localtime())
a=sys.path
print(a)



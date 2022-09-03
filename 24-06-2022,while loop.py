#while loop
#:exicute the set of statement as long as the condition is true.

 #syntax  :  initialize while condition : statements  - increment/ decrement
#remember to increment i,or else statement will execute for ever



#FACTORIAL USING while loop

n=int(input('ENTER THE NUMBER:'))
k=1
f=1
while(k<=n):
    f=f*k
    k=k+1
print(f)


#add n natural numbers

n=int(input("ENTER A NUMBER  :"))
i=1
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
    print(sum)


i=0
while(i<5):
    print(i)
    if i==3:
        break
    i=i+1

i=1
while(i<=5):
    i = i + 1
    if i==2:
      continue
    print(i)

i=0
while i<5:
    print(i)
    i=i+1
else:
    print("end")

s=str(input("type here :"))
a=("A","a","E","e","I","i","O","o","U","u",)
while s in a:
    print("vowels")
    break
else:
    print("not vowels")


vowel="aeiouAEIOU"
while True:
    s=str(input("enter letter   :"))
    if s in vowel:
        break
    print("not vowel")
print("vowel")
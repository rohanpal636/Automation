a=[0,1,2,30,4,5,6,7,0.5]
for i in range(len(a)):
    if a[i]>=5:
        print("Good")
    else:
        print("Not eligible")
b=[0,1,2,30,4,5,6,7,0.5]
t=[]
for i in b:
    t.append(i)
print(t)

for i in range(1,10,11):
    print(i)

    #While loop
it= 10
while it>-1:
    if it ==6:
        it = it - 1
        continue
    if it ==1:
        break
    print(it)

    it = it - 1
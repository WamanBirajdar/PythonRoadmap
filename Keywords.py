print("break keyword")
for i in range(1,10):
    if i>5:
        break
    print(i)

print("continue keyword")
for i in range(1,10):
    if i==5:
        continue
    print(i)

print("pass keyword")
a=6
if a<10:
    pass#we can not keep indentation
else:
    print("a is smaller than 10")

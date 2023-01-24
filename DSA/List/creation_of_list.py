# creating list from user

lst=[]

n=int(input("Enter a string"))
# iterating till the range

for i in range(0,n):
    ele=int(input())
    lst.append(ele)

print(lst)

# with handling exception

try:
    list1=[]

    while True:
        list1.append(int(input()))
except:
    print(list1)


l1=[int(item) for item in input("Enter the list items").split()]
print(l1)

# list

# creating blank list
l1=[]

# creating list with some elements
l1=[1,2,3,4,5]

# adding new element to list 
# append() method we are using
# append() methods it can not return  any value adding element ot existing list 

l1.append(6)
print(f'list after appending new element: {l1}')

# extend() method
# extend method explode list and adding individual elements in list

l2=[10,20,30,40]
l1.extend(l2)
print(f'after using extend method list become: {l1}')


# accessing elements from list
# 1. without index 2. with index

# 1. without index
for i in l1:
    print(i)


# 2. with index
for i in range(0,len(l1)):
    print(f'at index {i} value is {l1[i]}')


# list having duplicate values
list=[11,22,33,44,55,[333,444]]
print(list)

# accessing using multi dimensional
print(list[5][0])


#taking string as input and split it 
name=input("Enter a name ")
print(name.split(sep="@"))


# old square 
od_square=[x ** 2 for x in range(1,10) if x % 2==1]
print(od_square)







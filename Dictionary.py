# dictionary data structure
# collection types which holds data in key value pair
# dictionary keys are immutable and no duplicates keys allow


# creating empty dict
d1={}
print(f'Empty dictionary: {d1}')
print()
# creating dictionary usign dict method
d2=dict()
print(f'creating empty dict using dic method: {d2}')
print()
d3=dict([(1,"waman"),(2,"kalpesh")])
print(f'dict with each pair: {d3}')
print()
# assigning keys and values to empty created dictionary
d1["name"]='waman'
d1['age']=22
d1["salary"]=50000
print(d1)

print()

# accessing keys and values from dictionary
for key,value in d1.items():
    print(f'keys: {key} and value is: {value}')

dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}


# copy method
dict2=dict1.copy()
print(dict2)

# get method
print(dict2.get(4))

# items
print(dict2.items())

# keys
print(dict2.keys())


# popitem
print(dict2.popitem())
print(dict2)




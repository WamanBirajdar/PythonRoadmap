# left rotation by d
# right rotation by d



def leftrotation(str1,d):
    temp=str1[d:]+str1[0:d]
    return temp
def rightrotation(str1,d):
    d=len(str1)-d
    temp=str1[d:]+str1[0:d]
    return temp

str1='waman'
print(leftrotation(str1,2))
print(rightrotation(str1,2))

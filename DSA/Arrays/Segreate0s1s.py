# You are given an array of 0s and 1s in random order. 
# Segregate 0s on left side and 1s on right side of the array [Basically you have to sort the array]. 
# Traverse array only once. 
# Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
# Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 


def Segreate(arr,n):
    count=0
    for i in range(n):
        if arr[i]==0:
            count+=1
        
    for i in range(0,count):
        arr[i]=0

    for i in range(count,n):
        arr[i]=1

def printArray(arr,n):
    print("Segreate array is: ",end="")
    for i in range(n):
        print(arr[i],end=" ")
arr=[0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
n=len(arr)
Segreate(arr,n)
printArray(arr,n)

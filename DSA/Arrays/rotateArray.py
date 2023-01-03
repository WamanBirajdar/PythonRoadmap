# Given an array of integers arr[] of size N and an integer, 
# the task is to rotate the array elements to the left by d positions.
#here we are using reversal algorithm for rotating array
# function to reverse an array[] from index start to end
def reversearray(arr,start,end):
    while start<end:
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp

        start+=1
        end=end-1

def LeftRotate(arr,d):

    d=d%n
    reversearray(arr,0,d-1)
    reversearray(arr,d,n-1)
    reversearray(arr,0,n-1)

# printing array
def printArray(arr):
    for i in range(0,len(arr)):
        print(arr[i],end="")

arr=[1,2,3,4,5,6,7]
n=len(arr)
d=2

LeftRotate(arr,d)
print(arr)


# Given an array arr[] of N+2 elements. All elements of the array are in the range of 1 to N. 
# And all elements occur once except two numbers which occur twice. 
# Find the two repeating numbers. 



def repeartingArray(arr,n):
    s=set()

    print("Repeating Elements are ",end="")
    for i in range(n):
        if len(s) and arr[i] in s:
            print(arr[i],end=" ")
        s.add(arr[i])



arr = [4, 2, 4, 5, 2, 3, 1]
n=len(arr)
repeartingArray(arr,n)

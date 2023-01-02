# Write a program to print all the LEADERS in the array. 
# An element is a leader if it is greater than all the elements to its right side. 
# And the rightmost element is always a leader. 

def LeadElement(arr,size):
    for i in range(0,size):
        for j in range(i+1,size):
            if arr[i]<=arr[j]:
                break
        if j==size-1:
            print(arr[i],end=" ")


arr=[16, 17, 4, 3, 5, 2]
LeadElement(arr,len(arr))

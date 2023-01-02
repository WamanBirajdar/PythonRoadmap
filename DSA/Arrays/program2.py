#Find the majority element in the array. 
#A majority element in an array A[] of size n is an element that appears more than n/2 times 
#(and hence there is at most one such element). 

def majoritycheck(arr,size):
    for i in range(size):
        count=0
        for j in range(size):
            if(arr[i]==arr[j]):
                count+=1

    #updating count
    maxcount=0
    index=-1
    if(count>maxcount):
        maxcount=count
        index=i

    #check maxcount is greater than count then return index
    if(maxcount>size//2):
        print(arr[index])
    else:
        print("no majority element")


#main driver code
if __name__=="__main__":
    arr=[1, 1, 2, 1, 3, 5, 1]
    size=len(arr)
    majoritycheck(arr,size)



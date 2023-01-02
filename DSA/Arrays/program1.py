#find 2 elements with given sum
#time compilixity O(n**2)
def checkpair(arr,size,x):
    for i in range(0,size-1):
        for j in range(i+1,size):
            if(arr[i]+arr[j]==x):
                return 1
    return 0

if __name__=="__main__":
    arr=[0, -1, 2, -3, 1]
    x=-2
    size=len(arr)

    if(checkpair(arr,size,x)):
        print("yes")
    else:
        print("no")
        
 #here w eare usnig hashing techniq to reduce time complexity and faster access
#hashing its  process of mapping keys and values in hash table usinng hash function 

def checkpair(arr,size,sum):
    
    #creating empty hash map and store indices 
    hashmap={}
    
    for i in range(0,size):
        temp=sum-arr[i]
        if(temp in hashmap):
            print("yes")
            return 
        hashmap[arr[i]]=i
    print("no")

arr=[0, -1, 2, -3, 1]
sum=-2
checkpair(arr,len(arr),sum)

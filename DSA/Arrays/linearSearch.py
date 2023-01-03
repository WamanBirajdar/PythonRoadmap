# linear search algorithm

def search(arr,n,x):
    for i in range(n):
        if arr[i]==x:
            return i
    return -1


if __name__=="__main__":
    arr = [2, 3, 4, 10, 40]
    print("given array is ",arr)
    x=int(input("Enter a element to search "))
    n=len(arr)
    
    result=search(arr,n,x)

    if result==-1:
        print("element not present in array")
    else:
        print("ELement present at index",result)

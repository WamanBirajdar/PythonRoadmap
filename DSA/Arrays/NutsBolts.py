# Nuts & Bolts Problem (Lock & Key problem) using Hashmap

def nutboltmatch(nuts,nolts,n):
    hash1={}


    #creating hashmap for nuts
    for i in range(n):
        hash1[nuts[i]]=i

    # searching bolts in hashmap
    for i in range(n):
        if bolts[i] in hash1:
            nuts[i]=bolts[i]

    # printing nuts and bolts

    for i in range(n):
        print(nuts[i],end=" ")
    print()
    for i in range(n):
        print(bolts[i],end=" ")


if __name__=="__main__":
    nuts = ['@', '#', '$','%', '^', '&']
    bolts = ['$', '%', '&','^', '@', '#']
    n=len(nuts)
    nutboltmatch(nuts,bolts,n)

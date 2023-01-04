# Find common elements in three sorted arrays



def commanelement(a,b,c,n1,n2,n3):
    uset1=set()
    uset2=set()
    uset3=set()


    for i in range(n1):
        uset1.add(a[i])

    for i in range(n2):
        uset2.add(b[i])

    for i in range(n3):
        if (c[i] in uset1 and c[i] in uset2):
            if( c[i] not in uset3):
                print(c[i],end=" ")
            uset3.add(c[i])
ar1 = [ 1, 5, 10, 20, 40, 80 ]
ar2 = [ 6, 7, 20, 80, 100 ]
ar3 = [ 3, 4, 15, 20, 30, 70, 80, 120 ]
n1=len(ar1)
n2=len(ar2)
n3=len(ar3)

print("Comman elments are: ",end=" ")
commanelement(ar1,ar2,ar3,n1,n2,n3)

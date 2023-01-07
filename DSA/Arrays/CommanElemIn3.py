'''Given three arrays sorted in non-decreasing order, 
print all common elements in these arrays.'''

import time
ar1= [1, 5, 10, 20, 40, 80] 
ar2= [6, 7, 20, 80, 100]
ar3= [3, 4, 15, 20, 30, 70, 80, 120] 


tick=time.time()
for i in range(len(ar1)):
    for j in range(len(ar2)):
        if ar1[i]==ar2[j]:
            for k in range(len(ar3)):
                if ar1[i]==ar3[k]:
                    print(ar1[i],end=" ")
                    break
tock=time.time()
time1=tock-tick
print(time1)
            

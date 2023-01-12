# we can add either or remove both sides queue

from collections import deque
queue = deque(['name','age','DOB'])
print(queue)

# operation perform on deque
queue.append("waman")
print(queue)
print()
queue.appendleft("leftitem")



# poping elements from queue
queue.pop()
print("it will pop right element from queue")
print(queue)
queue.popleft()
print("it will remove left elemtn frkm queue")
print(queue)


# accessing items in dqueue
import collections
de = collections.deque([1, 2, 3, 3, 4, 2, 4])

de.index(4)# index(ele,start,end)
print(de)

de.insert(0,10)# insert(i,a)
print(de)

de.remove(3)# remove(elem)remove first occurnece of lemen
print(de)

de.count(4)
print(de.count(4))

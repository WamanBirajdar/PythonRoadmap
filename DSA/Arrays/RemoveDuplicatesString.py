"""
remove all duplicats in given string
"""

# Method 1
# time complecxity is O(n*n)


string="geeksforgeeks"
new_string=""

for char in string:
    if char not in new_string:
        new_string+=char

print("FIst method result is {}".format(new_string))


# method 2 time complexity is O(n)
def removeDuplicate(str):
    s = set()
     
    # Create a set using String characters
    for i in str:
        s.add(i)
 
    # Print content of the set
    st = ""
    for i in s:
        st = st+i
    return st
 
 
# Driver code
str = "geeksforgeeks"
n = len(str)
print(removeDuplicate(str))



# method 3
s="abacdabd"
temp=""+s[0]
for i in range(1,len(s)):
    if s[i] not in temp:
        temp=temp+s[i]

print(temp)

# method I
def reverstring(s):
    new_list=[]
    for word in s:
        new_list.insert(0,word)
    return new_list


if __name__=='__main__':
    s='my name is waman'
    sl=s.split(' ')
    result=reverstring(sl)
    print(' '.join(result))
















# revers words in given string
'''
Input: s = “geeks quiz practice code” 
Output: s = “code practice quiz geeks”

Input: s = “i love programming very much” 
Output: s = “much very programming love i”

'''

# method one
def reverstring(s1):
    l=len(s1)

    if l%2==0:
        # find middle word
        j=int(l/2)

        # starting from middle and swapping words
        while j<=l-1:
            s1[j],s1[l-j-1]=s1[l-j-1],s1[j]
            j+=1
    else:
 
        # Find the middle word
        j = int(l/2 + 1)
 
        # Starting from the middle
        # start swapping the words
        # at jth position and l-1-j position
        while(j <= l - 1):
            s1[j], s1[l - 1 - j] = s1[l - j - 1], s1[j]
            j += 1
 
        # return the reversed sentence
    return s1

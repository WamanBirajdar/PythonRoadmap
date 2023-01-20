# remove characters from the first string which are present in the second string



def removeChars(s1,s2):
    n1=len(s1)
    n2=len(s2)

    for i in s2:
        while i in s1:
            itr=s1.find(i)
            print(itr)
            s1=s1.replace(i,'')
    return s1 

if __name__ == "__main__":
 
    string1 = "geeksforgeeks"
    string2 = "mask"
    print(removeChars(string1, string2))

# remove duplicates and sorted in alpahbetical order
# time complexity is: O(n)


def remove_duplicates(s):
    length=len(s)
    s1=""

    for i in range(length):
        c=s[i]
        if c not in s1:
            s1+=c

    return s1

if __name__ == "__main__":
 
    # Input string with repeating chars
    s = input("Enter a string")
    sorted_list=sorted(s)
    arange_str=''.join(sorted_list)
    print(remove_duplicates(arange_str))

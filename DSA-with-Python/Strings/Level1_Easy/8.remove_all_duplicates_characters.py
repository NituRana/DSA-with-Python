'''*******************************************************************************************************
In the given a string and we need to remove all duplicates from it

Input : "Hello here, I'm nitu rana"
Output : c


***********************************************************************************************************'''
# def removeDuplicates(s):
#     return ''.join(set(s))

# s = "Hello here, I'm nitu rana"
# print(removeDuplicates(s))

def removeDuplicates(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    result = ''
    for c in s:
        if counts[c] == 1:
            result += c
    return result

s = "Hello here, I'm nitu rana"
print(removeDuplicates(s)) 

   
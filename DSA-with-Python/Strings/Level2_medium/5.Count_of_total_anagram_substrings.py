'''*******************************************************************************************************
Count the total anagram substrings from the following string.

Input : "xyyx" 
Output : 4

Input : "abaabb" 
Output : 13
***********************************************************************************************************'''
def count_anagram_substrings(s):
    # Create an empty dictionary to store the frequency of each substring's sorted characters
    freq = {}
    count = 0
    n = len(s)
    # Iterate over all substrings of s
    for i in range(n):
        for j in range(i, n):
            # Sort the characters of the substring and count its frequency
            sorted_sub = ''.join(sorted(s[i:j+1]))
            freq[sorted_sub] = freq.get(sorted_sub, 0) + 1

    # Iterate over the frequency dictionary and count the number of anagram substrings
    for k, v in freq.items():
        if v > 1:
            count += (v * (v - 1)) // 2

    return count

s = 'xyyx'
print(count_anagram_substrings(s))
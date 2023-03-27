'''*******************************************************************************************************
Find K’th Non-repeating Character in the given string.

Input : "hello here I am nitu rana"
Output : I


***********************************************************************************************************'''
def kth_non_repeating_char(s, k):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    non_repeating_chars = [char for char in s if char_count[char] == 1]
    if len(non_repeating_chars) >= k:
        return non_repeating_chars[k - 1]
    else:
        return None

# Driver Code
def main():
    s = "hello here I am nitu rana"
    k = 2
    result = kth_non_repeating_char(s, k)
    print(result)
     
if __name__=="__main__":
    main()

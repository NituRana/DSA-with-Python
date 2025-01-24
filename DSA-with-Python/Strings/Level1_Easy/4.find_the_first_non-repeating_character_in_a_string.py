string = "I am in mumbai for the devils circuit event. Its day second of the bib distribution z."

def first_non_repeat(string):
    hash_of_string = {}
    for char in string:
        if char != " ":
            hash_of_string[char] = hash_of_string.get(char, 0) + 1
    for char in string:
        if char != " " and hash_of_string[char] == 1:
            return char
    return None

res = first_non_repeat(string)
print("------------------ first non-repeating character:", res)





















'''*******************************************************************************************************
Given n binary strings, return their sum (also a binary string).
Input:  arr[] = ["11", "1"]
Output: "100"


***********************************************************************************************************'''
# def addBinaryUtil(a, b):
     
#     result = ""; # Initialize result
#     s = 0;       # Initialize digit sum
 
#     # Traverse both strings
#     # starting from last characters
#     i = len(a) - 1;
#     j = len(b) - 1;
#     while (i >= 0 or j >= 0 or s == 1):
 
#         # Compute sum of last digits and carry
#         s += (ord(a[i]) - ord('0')) if(i >= 0) else 0;
#         s += (ord(b[j]) - ord('0')) if(j >= 0) else 0;
 
#         # If current digit sum is 1 or 3,
#         # add 1 to result
#         result = chr(s % 2 + ord('0')) + result;
 
#         # Compute carry
#         s //= 2;
 
#         # Move to next digits
#         i -= 1;
#         j -= 1;
 
#     return result;
 
# # function to add n binary strings
# def addBinary(arr, n):
#     result = "";
#     for i in range(n):
#         result = addBinaryUtil(result, arr[i]);
#     return result;
 
# # Driver code
# arr = ["1", "10", "11"];
# n = len(arr);
# print(addBinary(arr, n));
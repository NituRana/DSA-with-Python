'''*******************************************************************************************************
Least Frequent Character in String in python

Input : "Hello here, I'm nitu rana"
Output : o


***********************************************************************************************************'''
def least_frequent_char(string):
    # Create an empty dictionary to store character counts
    char_counts = {}
    
    # Count the frequency of each character in the string
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    # Get the least frequent character and its frequency
    least_common_char = min(char_counts, key=char_counts.get)
    
    return least_common_char

# Example usage
string = "hello here, I'm nitu rana"
least_frequent = least_frequent_char(string)
print("The least frequent character in '{}' is '{}'.".format(string, least_frequent))

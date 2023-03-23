'''*******************************************************************************************************
Find the frequencies of all the characters in that string and return a dictionary with key as the character and its value as its frequency in the given string.
Input : "Hello here, I'm nitu rana"
Output : o


***********************************************************************************************************'''
test_str = "Welcome to my data structure repo"
all_freq = {}
 
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
 
# printing result
print("Count of all characters count is :\n "
      + str(all_freq))

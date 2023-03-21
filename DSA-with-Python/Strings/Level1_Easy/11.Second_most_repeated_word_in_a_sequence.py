'''*******************************************************************************************************
Find the second most repeated word in a sequence in a given string,

Input : "Hello here, I'm nitu rana"
Output : o


***********************************************************************************************************'''
def second_most_repeated_word(strings):
    count = {}
    for string in strings:
        for word in string.split():
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_count) < 2:
        return None
    else:
        return sorted_count[1][0]

# Example usage
string = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
result = second_most_repeated_word(string)
print(result)

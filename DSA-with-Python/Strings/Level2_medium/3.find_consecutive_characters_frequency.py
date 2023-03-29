'''*******************************************************************************************************
Find consecutive characters frequency in the given string.

Input : "hello here I am nitu rana"
Output : [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


***********************************************************************************************************'''
input_str = '"hello here I am nitu rana"'
 
print("The original string is : " + input_str)
res = []
count = 1
for i in range(len(input_str)-1):
    if input_str[i] == input_str[i+1]:
        count += 1
    else:
        res.append(count)
        count = 1
res.append(count)
print("The Consecutive characters frequency : " + str(res))
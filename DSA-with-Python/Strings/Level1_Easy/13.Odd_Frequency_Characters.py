'''*******************************************************************************************************
Find the Odd Frequency Characters in a given string,

Input : "Hello here, I'm nitu rana"
Output : ['H', 'e', 'o', 'h', ',', 'I', "'", 'm', 'i', 't', 'u']


***********************************************************************************************************'''
from collections import defaultdict
 
def hlper_fnc(test_str):
    cntr = defaultdict(int)
    for ele in test_str:
        cntr[ele] += 1
    return [val for val, chr in cntr.items() if chr % 2 != 0]
 
test_str = "Hello here, I'm nitu rana"
print("The original string is : " + str(test_str))
 
res = hlper_fnc(test_str)
print("The Odd Frequency Characters are :" + str(res))

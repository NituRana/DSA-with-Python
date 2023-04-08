'''*******************************************************************************************************
find the maximum element using a stack:

Input : "Hello here, I'm nitu rana"
Output : l


***********************************************************************************************************'''
def max_element(lst):
    stack = []
    max_element = float('-inf')
    for num in lst:
        stack.append(num)
        if num > max_element:
            max_element = num
    return max_element

lst1 = (12, 43, 46 ,68, 93, 57, 69, 28, 91)
print(max_element(lst1))
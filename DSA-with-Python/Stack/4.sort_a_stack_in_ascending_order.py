'''*******************************************************************************************************
Sort a stack in ascending order.

Input : [5, 2, 8, 1, 3]
Output : [1, 2, 3, 5, 8]


***********************************************************************************************************'''
def sort_stack(stack):
    sorted_stack = []
    while len(stack) > 0:
        temp = stack.pop()
        while len(sorted_stack) > 0 and sorted_stack[-1] > temp:
            stack.append(sorted_stack.pop())
        sorted_stack.append(temp)
    return sorted_stack
stack_1 = [5, 2, 8, 1, 3]
print(sort_stack(stack_1))

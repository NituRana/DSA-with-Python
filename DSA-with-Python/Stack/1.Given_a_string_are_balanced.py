'''*******************************************************************************************************
Find the string of parentheses are balanced or not.

Input  : p1 = "((()))"
Output : True

Input  : p1 = "((())"
Output : False
p2 = "((())"

***********************************************************************************************************'''


def is_balanced(parentheses):
    stack = []
    for p in parentheses:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


p1 = "((()))"
p2 = "((())"
print(is_balanced(p1))
print(is_balanced(p2))

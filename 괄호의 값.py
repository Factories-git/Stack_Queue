string = input().strip()
string += ' '
re = 0
expression = []
stack = []
check = True
pass_ = set()
print(string, len(string))
for i in range(len(string)-1):
    m = string[i]
    if m == '(' or m == '[':
        stack.append(m)
        if m == '(' and string[i+1] == ')':
            expression.append(2)
            pass_.add(i+1)
        elif m == '[' and string[i+1] == ']':
            expression.append(3)
            pass_.add(i+1)
    elif m == ')':
        if stack and stack[-1] == '(':
            stack.pop()
            if i not in pass_:
                expression[-1] *= 2
            if (string[i+1] == '(' or string[i+1] == '[') and not stack:
                re += sum(expression)
                expression = []
        else:
            check = False
            break
    elif m == ']':
        if stack and stack[-1] == '[':
            stack.pop()
            if i not in pass_:
                expression[-1] *= 3
            if (string[i+1] == '(' or string[i+1] == '[') and not stack:
                re += sum(expression)
                expression = []
        else:
            check = False
            break
    print(expression, re)
re += sum(expression)
print(f'{re if check and not stack else 0}')
string = input().strip()
string += ' '
re = 0
expression = 0
stack = []
check = True
pass_ = set()
print(string, len(string))
for i in range(len(string)-1):
    m = string[i]
    if m == '(' or m == '[':
        stack.append(m)
        if m == '(' and string[i+1] == ')':
            expression += 2
            pass_.add(i+1)
        elif m == '[' and string[i+1] == ']':
            expression += 3
            pass_.add(i+1)
    elif m == ')':
        if stack and stack[-1] == '(':
            stack.pop()
            if i not in pass_:
                expression *= 2
            if (string[i+1] == '(' or string[i+1] == '[') and not stack:
                re += expression
                expression = 0
        else:
            check = False
            break
    elif m == ']':
        if stack and stack[-1] == '[':
            stack.pop()
            if i not in pass_:
                expression *= 3
            if (string[i+1] == '(' or string[i+1] == '[') and not stack:
                re += expression
                expression = 0
        else:
            check = False
            break

re += expression
print(f'{re if check and not stack else 0}')
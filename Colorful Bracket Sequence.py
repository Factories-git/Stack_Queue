s = input()
stack = []
for l in s:
    if l == '(':
        stack.append(l)
    elif l == '[':
        stack.append(l)
    elif l == '<':
        stack.append(l)

    if l == ')':
        if stack:
            if stack[-1] != '(':
                print('No')
                exit(0)
            stack.pop()
        else:
            print('No')
            exit(0)
    elif l == ']':
        if stack:
            if stack[-1] != '[':
                print('No')
                exit(0)
            stack.pop()
        else:
            print('No')
            exit(0)

    elif l == '>':
        if stack:
            if stack[-1] != '<':
                print('No')
                exit(0)
            stack.pop()
        else:
            print('No')
            exit(0)

if stack:
    print('No')
    exit(0)
print('Yes')
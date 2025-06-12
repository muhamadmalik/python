def isValid(s: str) -> bool:
    stack = []
    CloseToOpen = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in CloseToOpen:
            if stack and stack[-1] == CloseToOpen[c]:
                stack.pop()
        else:
            stack.append(c)
        
    return True if not stack else False
s = "([{}])["
result = isValid(s)
print(result)
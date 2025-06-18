def isValid(s: str) -> bool:
    
    stack = []
    closeToOpen = {")": "(", "}": "{", "]": "[", }
    for c in s: 
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                False
        else:
            stack.append(c)
    return True if not stack else False
s = "([{}]"
result = isValid(s)
print(result)
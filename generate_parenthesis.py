def generateParenthesis(n: int):
    res = []
    stack = []
    
    def BackTrack(openN, closeN):
        if openN == closeN == n:
            res.append(''.join(stack))
            return 
        if openN < n:
            stack.append('(')
            BackTrack(openN + 1, closeN)
            stack.pop()
        if closeN < openN:
            stack.append(')')
            BackTrack(openN, closeN + 1)
            stack.pop()
    
    BackTrack(0, 0)
    return res

n = 3
result = generateParenthesis(n)
print(result)
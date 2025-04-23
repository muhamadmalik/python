def reverseString(s):
    stack = []
    i = 0
    for c in s:
        stack.append(c) 
    while stack:
        s[i] = stack.pop()
        i = i + 1
    return s
    
    
# def reverseString(s):
#     l = 0
#     r = len(s) - 1
#     while l < r:
#         temp = s[l]
#         s[l] = s[r]
#         s[r] = temp
#         l += 1
#         r -= 1
#     return s

print(reverseString(['h', 'e', 'l', 'l', 'o']))
def minWindow(s: str, t: str) -> str:
    
    
    if s == t:
        return t
    if len(t) >= len(s):
        return ''
    l = 0
    res = ''
    resLength = float('infinity')
    countT = dict()
    window = dict()
    
    for c in t:
        countT[c] = countT.get(c, 0) + 1
    
    have = 0
    need = len(countT)
    
    for r in range(len(s)):
        
        window[s[r]] = window.get(s[r], 0) + 1
        
        if s[r] in countT and countT[s[r]] == window[s[r]]:
            have += 1
            
        while have == need:
            
            if r - l + 1 < resLength:
                res = s[l: r + 1]
                resLength = r - l + 1
            window[s[l]] -= 1
            
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            
            
            l += 1
            
    return res


s = "bbaa"
t = "aba"
expected = 'baa'
# s = "ADOBECODEBANC"
# t = "ABC"
result = minWindow(s, t)
print(result)
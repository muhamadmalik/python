def characterReplacement( s: str, k: int) -> int:
    res = 0
    maxF = 0
    l = 0
    hash = dict()
    for r in range(len(s)):
        hash[s[r]] = hash.get(s[r], 0) + 1
        maxF = max(maxF, hash[s[r]])
        
        if (r - l + 1) - maxF > k:
            hash[s[l]] -=  1
            l += 1
        res = max(res, r - l + 1)
    return res  

s = "ABAB"
k = 0
result = characterReplacement(s, k)
print(result)